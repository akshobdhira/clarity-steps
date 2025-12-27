from google.adk import Agent
import inspect

print(f"Agent methods: {[m for m in dir(Agent) if not m.startswith('__')]}")

if hasattr(Agent, 'run'):
    print("Agent has 'run' method")
    try:
        print(f"Agent.run signature: {inspect.signature(Agent.run)}")
    except: pass
else:
    print("Agent does NOT have 'run' method")
