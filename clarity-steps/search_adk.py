import google.adk
import os

pkg_path = os.path.dirname(google.adk.__file__)
print(f"Package path: {pkg_path}")
for root, dirs, files in os.walk(pkg_path):
    for file in files:
        print(os.path.join(root, file))

print("\nSearch for AgentRunner:")
for root, dirs, files in os.walk(pkg_path):
    for file in files:
        if file.endswith('.py'):
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    if "class AgentRunner" in content:
                        print(f"Found AgentRunner in {file}")
            except: pass
