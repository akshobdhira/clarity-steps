import streamlit as st
from dotenv import load_dotenv

load_dotenv()
from agents.runner import AgentRunner
from agents.profiler_agent import parent_profiler
from agents.plan_agent import plan_designer

# Create runners
profiler_runner = AgentRunner(parent_profiler)
plan_runner = AgentRunner(plan_designer)

st.title("AI Career Companion for Parents")

grade = st.selectbox("Child Grade", ["8", "9", "10", "11", "12"])
board = st.selectbox("Board", ["CBSE", "ICSE", "IGCSE", "IB"])
concern = st.text_area("What worries you most about your child’s future?")
behavior = st.text_area("How do you usually guide or pressure your child?")

if st.button("Generate Plan"):
    with st.spinner("Analyzing parenting patterns..."):
        profiler_output = profiler_runner.run(
            f"""
            Grade: {grade}
            Board: {board}
            Parent Concern: {concern}
            Parent Behavior: {behavior}
            """
        )

    st.subheader("🔍 Parenting Insights")
    st.write(profiler_output)

    with st.spinner("Designing 12-week plan..."):
        plan_output = plan_runner.run(
            f"""
            Insights:
            {profiler_output}

            Board: {board}
            """
        )

    st.subheader("📅 12-Week Action Plan")
    st.write(plan_output)
