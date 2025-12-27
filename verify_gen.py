from dotenv import load_dotenv
load_dotenv()

from agents.runner import AgentRunner
from agents.profiler_agent import parent_profiler
print("Testing Agent Generation...")

runner = AgentRunner(parent_profiler)
try:
    response = runner.run("Hello, who are you?")
    print(f"Response received (len {len(response)}): {response[:50]}...")
except Exception as e:
    print(f"Error during generation: {e}")
