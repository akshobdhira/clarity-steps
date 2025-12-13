import google.generativeai as genai
import os

# Configure the API key
if "GOOGLE_API_KEY" in os.environ:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

class AgentRunner:
    def __init__(self, agent):
        self.agent = agent
        # Assuming agent.model is something like "gemini-1.5-pro"
        # We might need to map it if the names differ slightly, but usually they match.
        self.model = genai.GenerativeModel(
            model_name=agent.model,
            system_instruction=agent.instruction
        )

    def run(self, input_text):
        """
        Runs the agent with the given input text.
        """
        try:
            response = self.model.generate_content(input_text)
            return response.text
        except Exception as e:
            return f"Error running agent {self.agent.name}: {e}"
