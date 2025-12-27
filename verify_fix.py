from agents.runner import AgentRunner
from agents.profiler_agent import parent_profiler
from agents.plan_agent import plan_designer

print("Imports successful!")

# Test run with dummy input (just to check if init works)
try:
    profiler_runner = AgentRunner(parent_profiler)
    print("Profiler runner initialized.")
    plan_runner = AgentRunner(plan_designer)
    print("Plan runner initialized.")
except Exception as e:
    print(f"Initialization error: {e}")
