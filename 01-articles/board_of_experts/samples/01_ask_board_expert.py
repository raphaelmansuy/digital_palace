"""
Example using Litellm API to query experts.
"""

from typing import List, Dict
from litellm import completion


class Expert:
    """An expert agent that can be queried."""

    def __init__(self, name: str, description: str, books: List[Dict],
                 model: str = "gpt-3.5-turbo") -> None:
        self.name = name
        self.description = description
        self.model = model
        self.messages = []
        self.books = books

    def query(self, prompt: str) -> str:
        """Query the expert."""

        # for book in self.books: create a list of books in a string

        book_list = ""
        for index, book in enumerate(self.books):
            book_list += f"{index+1}. {book['name']} by authors: {book['authors']}, book description: {book['description']}\n"

        expert_prompt = f"""
        You are {self.name}.
        
        {self.description}
        
        You are equipped with a vast knowledge of these books:
        
        {book_list}
        
        {prompt}

        Take a deep breath and Reason through the question step by step.
        Please provide a detailed, thoughtful response summarizing "
        "your expertise and directly answering the question.
        """

        if (len(self.messages) == 0):
            self.messages.append({"content": expert_prompt, "role": "user"})
        else:
            self.messages.append({"content": prompt, "role": "user"})

        response = completion(model=self.model, messages=self.messages)
        # get content from response
        response_message = response["choices"][0]["message"]
        self.messages.append(response_message)

        return response


def create_experts(expert_profiles: List[Dict]) -> List[Expert]:
    """Create Expert instances from profiles."""

    experts = []

    for profile in expert_profiles:
        expert = Expert(profile["name"], profile["description"], profile["books"])
        experts.append(expert)

    return experts


def query_experts(experts: List[Expert], user_profile: str, user_question: str) -> None:
    """Query each expert and print their responses."""

    print(f"USER PROFILE: {user_profile}\n")
    print(f"USER QUESTION: {user_question}\n")

    for expert in experts:
        print(f"Asking {expert.name}...")
        response = expert.query(f"{user_profile}\n\n{user_question}")
        print(response)


experts_definition = [
    {
        "name": "Industry Veteran",
        "description": "An experienced professional with a deep understanding of the company's specific industry, market trends, and competitive landscape.",
        "books": [
            {"name": "The Innovator's Dilemma", "authors": "Clayton Christensen",
                "description": "This classic book explores disruptive innovation and how industries evolve over time."},
            {"name": "Blue Ocean Strategy", "authors": "W. Chan Kim and Renée Mauborgne",
                "description": "It offers a strategic approach to creating uncontested market space and making competition irrelevant."},
            {"name": "Multipliers", "authors": "Liz Wiseman",
                "description": "How the Best Leaders Make Everyone Smarter."},
        ],
    },
    {
        "name": "Financial Expert",
        "description": "A certified accountant or financial analyst who can provide guidance on financial strategies, risk management, and investment decisions.",
        "books": [
            {"name": "Financial Intelligence", "authors": "Karen Berman and Joe Knight",
                "description": "A manager's Guide to Knowing What the Numbers Really Mean."},
            {"name": "The Intelligent Investor", "authors": "Benjamin Graham",
                "description": "A foundational book on value investing and long-term financial strategies."},
            {"name": "Security Analysis", "authors": "Benjamin Graham and David Dodd",
                "description": "A comprehensive guide to analyzing and valuing securities."},
        ],
    },
    {
        "name": "Legal Counsel",
        "description": "A seasoned attorney specializing in corporate law, contracts, and regulatory compliance to ensure the company operates within the bounds of the law.",
        "books": [
            {"name": "The Art of Lawyering", "authors": "Paul Lisnek",
                "description": "Essential Knowledge for Becoming a Great Attorney."},
            {"name": "Contracts: Cases and Doctrine", "authors": "Randy E. Barnett",
                "description": "A comprehensive textbook on contract law that covers the fundamentals of contract formation and interpretation."},
        ],
    },
    {
        "name": "Technology Guru",
        "description": "An expert in emerging technologies and digital trends who can advise on IT strategies, cybersecurity, and digital transformation.",
        "books": [
            {"name": "The Innovator's Dilemma", "authors": "Clayton Christensen",
                "description": "It discusses the impact of disruptive technologies on industries."},
            {"name": "The Lean Startup", "authors": "Eric Ries",
                "description": "This book introduces lean methodology and agile development, essential for technology innovation."},
        ],
    },
    {
        "name": "Marketing Maven",
        "description": "A marketing strategist with expertise in brand management, customer acquisition, and market positioning.",
        "books": [
            {"name": "Influence", "authors": "Robert B. Cialdini",
                "description": "A classic on understanding the psychology behind marketing and persuasion."},
            {"name": "Contagious", "authors": "Jonah Berger",
                "description": "It delves into why certain ideas and products go viral."},
            {"name": "The Sales Acceleration Formula", "authors": "Mark Roberge",
                "description": "Using Data, Technology, and Inbound Selling to Go from $0 to $100 Million"},
        ],
    },
    {
        "name": "Human Resources Specialist",
        "description": "An HR professional who can provide insights into talent management, recruitment, employee engagement, and organizational development.",
        "books": [
            {"name": "The Five Dysfunctions of a Team",
                "authors": "Patrick Lencioni", "description": "A leadership fable."},
            {"name": "Drive", "authors": "Daniel H. Pink",
                "description": "The Surprising Truth About What Motivates Us."},
            {"name": "The Alliance", "authors": "Reid Hoffman, Ben Casnocha, and Chris Yeh",
                "description": "Managing Talent in the Networked Age."},
        ],
    },
    {
        "name": "Supply Chain and Operations Expert",
        "description": "Someone well-versed in supply chain management, logistics, and operations efficiency to optimize processes and reduce costs.",
        "books": [
            {"name": "The Goal", "authors": "Eliyahu M. Goldratt",
                "description": "A Process of Ongoing Improvement."},
            {"name": "Supply Chain Management", "authors": "Sunil Chopra and Peter Meindl",
                "description": "Strategy, Planning, and Operation."},
        ],
    },
    {
        "name": "Environmental and Sustainability Advisor",
        "description": "An expert in sustainability practices and environmental impact assessment to help the company adopt eco-friendly and socially responsible policies.",
        "books": [
            {"name": "Cradle to Cradle", "authors": "William McDonough and Michael Braungart",
                "description": "Remaking the Way We Make Things."},
            {"name": "The Ecology of Commerce", "authors": "Paul Hawken",
                "description": "A Declaration of Sustainability."},
        ],
    },
    {
        "name": "Mergers and Acquisitions (M&A) Specialist",
        "description": "A seasoned professional who can guide the company through mergers, acquisitions, and strategic partnerships.",
        "books": [
            {"name": "Mergers and Acquisitions from A to Z", "authors": "Andrew J. Sherman",
                "description": "A practical guide to understanding the M&A process."},
            {"name": "The Art of M&A", "authors": "Stanley Foster Reed, Alexandra Lajoux, and H. Peter Nesvold",
                "description": "A Merger Acquisition Buyout Guide."},
        ],
    },
    {
        "name": "Customer Experience Strategist",
        "description": "An expert in customer satisfaction and user experience design, ensuring the company delivers products and services that meet customer expectations.",
        "books": [
            {"name": "Hooked", "authors": "Nir Eyal",
                "description": "How to Build Habit-Forming Products."},
            {"name": "Customer Experience 3.0", "authors": "John A. Goodman",
                "description": "High-Profit Strategies in the Age of Techno Service."},
        ],
    },
]

if __name__ == "__main__":
    # get subset of experts, take first 1 
    l = experts_definition[0:1]
    experts_list = create_experts(l)
    USER_PROFILE = "I am a startup founder looking to raise a seed round."
    USER_QUESTION = "What should I look for in a board of advisors?"
    query_experts(experts_list, USER_PROFILE, USER_QUESTION)
    query_experts(experts_list, USER_PROFILE, "What is the best way to raise a seed round?")
