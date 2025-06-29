# Import AutoGen and other libraries  
from autogen import ResponsiveAgent, AssistantAgent, UserProxyAgent
import requests

# Define a custom agent that uses the page as context


class PageAgent(ResponsiveAgent):
    def __init__(self, page_url):
        # Initialize the agent with LLM as the default backend
        super().__init__(human_input_mode="NEVER")
        # Get the page content from the url
        response = requests.get(page_url)
        self.page_content = response.text
        # Set the system message to prompt LLM to use the page content
        self.system_message = f"This is a PageAgent that can use the page content from {page_url} as context. Please use the following text as context:\n{self.page_content}\n"

# Define a human agent that can provide feedback


class HumanAgent(UserProxyAgent):
    def __init__(self):
        # Initialize the agent with human as the default backend[^3^][3]
        super().__init__(human_input_mode="ALWAYS")
        # Set the system message to prompt human to give feedback
        self.system_message = "This is a HumanAgent that can provide feedback to other agents. Please give your feedback or type 'skip' to skip."


# Create an instance of PageAgent with a given url
page_agent = PageAgent("https://arxiv.org/pdf/2308.08155.pdf")

# Create an instance of AssistantAgent that can generate code
assistant_agent = AssistantAgent()
assistant_agent.system_message = "This is an AssistantAgent that can generate code based on natural language instructions. Please write code or function calls to solve the task."

# Create an instance of HumanAgent
human_agent = HumanAgent()

# Register auto-reply functions for each pair of agents
page_agent.register_auto_reply(assistant_agent, page_agent.reply_to_assistant)
assistant_agent.register_auto_reply(page_agent, assistant_agent.reply_to_page)
assistant_agent.register_auto_reply(
    human_agent, assistant_agent.reply_to_human)
human_agent.register_auto_reply(
    assistant_agent, human_agent.reply_to_assistant)

# Initiate a conversation between page_agent and assistant_agent
page_agent.initiate_chat(
    "How can I use AutoGen to create a multi-agent system?", assistant_agent)
