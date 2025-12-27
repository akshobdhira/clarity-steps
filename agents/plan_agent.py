from google.adk import Agent

plan_designer = Agent(
    name="PlanDesigner",
    model="gemini-2.5-flash",
    instruction="""
You are a career coaching planner for Indian parents.

Generate a 12-week micro-action plan.
Each week must include:
- One conversation
- One activity
- One habit or boundary
"""
)
