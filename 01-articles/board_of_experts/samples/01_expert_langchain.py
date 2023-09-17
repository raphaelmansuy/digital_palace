"""
A simple example of how to use the Litellm API to ask a question to 
a list of experts.
"""
from litellm import completion


expert_list = [
    {
        "name": "Industry Veteran",
        "description": "An experienced professional with a deep understanding"
        "of the company's specific industry, market trends, and competitive "
        "landscape.",
    },
    {
        "name": "Financial Expert",
        "description": "A certified accountant or financial analyst who can "
        "provide guidance on financial strategies, risk management, and "
        "investment decisions.",
    },
    {
        "name": "Legal Counsel",
        "description": "A seasoned attorney specializing in corporate law, "
        "contracts, and regulatory compliance to ensure the company operates"
        " within the bounds of the law.",
    },
    {
        "name": "Technology Guru",
        "description": "An expert in emerging technologies and digital trends "
        "who can advise on IT strategies, cybersecurity, and digital"
        " transformation.",
    },
    {
        "name": "Marketing Maven",
        "description": "A marketing strategist with expertise in brand "
        "management, customer acquisition, and market positioning.",
    },
    {
        "name": "Human Resources Specialist",
        "description": "An HR professional who can provide insights into "
        "talent management, recruitment, employee engagement, and "
        "organizational development.",
    },
    {
        "name": "Supply Chain and Operations Expert",
        "description": "Someone well-versed in supply chain management, "
        "logistics, and operations efficiency to optimize processes and reduce"
        " costs.",
    },
    {
        "name": "Environmental and Sustainability Advisor",
        "description": "An expert in sustainability practices and "
        "environmental impact assessment to help the company adopt"
        " eco-friendly and socially responsible policies.",
    },
    {
        "name": "Mergers and Acquisitions (M&A) Specialist",
        "description": "A seasoned professional who can guide the company "
        "through mergers, acquisitions, and strategic partnerships.",
    },
    {
        "name": "Customer Experience Strategist",
        "description": "An expert in customer satisfaction and user experience"
        " design, ensuring the company delivers products and services that"
        " meet customer expectations.",
    },
]


class Agent:
    """
    An agent is a person who is an expert in a particular field.
    """

    def __init__(self, name: str, description: str, model="gpt-3.5-turbo"):
        self.name = name
        self.description = description
        self.model = model

    def query(self, user_prompt: str):
        """
        This method queries the system with a user prompt and returns
        a response.
        """
        messages = [
            {"content": f"You are a {self.name}."
             "You act an expert assistant."
             "You provide the best advices."
             "You Use your knowledge and field of expertise to answer."
             f"Your field of expertise is: {self.description}."
             "When you answer the question, you first start by "
             "describing your field of expertise."
             "Before ansewerinh take a deep breath and you reason"
             " step by step."
             f"The question is: '{user_prompt}'",
             "role": "user"},
        ]
        response = completion(model=self.model, messages=messages)
        return response


def create_agents():
    """
    This function creates a list of agents.
    """
    agents = []
    for expert in expert_list:
        agent = Agent(expert["name"], expert["description"])
        agents.append(agent)
    return agents


def create_query(your_pesonna: str, your_question: str):
    """
    Create a query for the agent.
    """
    return f"""## Your pesonna: {your_pesonna}\r\n
           ## Question: {your_question}"""


def main():
    """
    The main function is the entry point of the program.
    """
    personna = """
      As the CEO of a small consulting firm specialized
      in Microsoft technology,
      you have a background in technology and a deep understanding
      of Microsoft products and services.

      Your expertise lies in providing IT solutions and consulting
       services to clients,
      helping them optimize their use of Microsoft technologies.

      Your goals include expanding your client base, increasing revenue,
      and staying up-to-date with the latest developments
      in Microsoft technology.
      
      You aim to provide exceptional consulting services to your clients,
       helping them leverage Microsoft products to achieve
        their business objectives.

      However, you face challenges in navigating the rapidly evolving
      landscape of Microsoft technology. Keeping up with the latest updates,
      understanding licensing models, and identifying the right solutions
      for your clients can be overwhelming.
      
    """

    question = """
        
      My goals include expanding your client base, increasing revenue,
        and staying up-to-date with the latest developments in Microsoft
         technology.
        You aim to provide exceptional consulting services to your clients,
        helping them leverage Microsoft products to achieve their business
         objectives.

        However, you face challenges in navigating the rapidly evolving
         landscape
        of Microsoft technology. Keeping up with the latest updates,
         understanding
        licensing models, and identifying the right solutions for your clients
        can be overwhelming.
        
      You ask the expert: How can I overcome these challenges?
      """

    agents = create_agents()

    for agent in agents:
        query = f"USER: {personna}.\r\n QUESTION: {question}"
        print(f"Query agent: {agent.name} ...")
        response = agent.query(query)
        print(response)


if __name__ == "__main__":
    main()
