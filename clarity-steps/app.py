import streamlit as st
from dotenv import load_dotenv
from fpdf import FPDF

load_dotenv()
from agents.runner import AgentRunner
from agents.profiler_agent import parent_profiler
from agents.plan_agent import plan_designer

# Create runners
profiler_runner = AgentRunner(parent_profiler)
plan_runner = AgentRunner(plan_designer)

def create_pdf(profiler_out, plan_out):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Parenting Insights", ln=1, align='L')
    
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, profiler_out.encode('latin-1', 'replace').decode('latin-1'))
    
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="12-Week Action Plan", ln=1, align='L')
    
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, plan_out.encode('latin-1', 'replace').decode('latin-1'))
    
    return pdf.output(dest='S').encode('latin-1')

st.title("Clarity Steps - Turn parental concern into clear weekly action")

grade = st.selectbox("Child Grade", ["8", "9", "10", "11", "12"])
board = st.selectbox("Board", ["CBSE", "ICSE", "IGCSE", "IB"])
concern = st.text_area("What worries you most about your child’s future?")
behavior = st.text_area("How do you usually guide or pressure your child?")

if "profiler_output" not in st.session_state:
    st.session_state.profiler_output = None
if "plan_output" not in st.session_state:
    st.session_state.plan_output = None

if st.button("Generate Plan"):
    with st.spinner("Analyzing parenting patterns..."):
        st.session_state.profiler_output = profiler_runner.run(
            f"""
            Grade: {grade}
            Board: {board}
            Parent Concern: {concern}
            Parent Behavior: {behavior}
            """
        )

    with st.spinner("Designing 12-week plan..."):
        st.session_state.plan_output = plan_runner.run(
            f"""
            Insights:
            {st.session_state.profiler_output}

            Board: {board}
            """
        )

if st.session_state.profiler_output and st.session_state.plan_output:
    st.subheader("🔍 Parenting Insights")
    st.write(st.session_state.profiler_output)

    st.subheader("📅 12-Week Action Plan")
    st.write(st.session_state.plan_output)

    pdf_bytes = create_pdf(st.session_state.profiler_output, st.session_state.plan_output)
    st.download_button(
        label="Download Report as PDF",
        data=pdf_bytes,
        file_name="parenting_plan.pdf",
        mime="application/pdf"
    )
