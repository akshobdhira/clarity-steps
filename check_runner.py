from google.adk import Runner, Agent
import inspect

print(f"Runner type: {type(Runner)}")
try:
    sig = inspect.signature(Runner.__init__)
    print(f"Runner init signature: {sig}")
except Exception as e:
    print(f"Could not get signature: {e}")

try:
    from google.adk.runner import AgentRunner
    print("Found AgentRunner in google.adk.runner")
except ImportError:
    print("Could not import AgentRunner from google.adk.runner")

try:
    from google.adk import AgentRunner
    print("Found AgentRunner in google.adk")
except ImportError:
    print("Could not import AgentRunner from google.adk")
