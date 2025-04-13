from crewai import Agent, LLM
from dotenv import load_dotenv
load_dotenv()

llm = LLM(model = "gemini/gemini-1.5-flash")

class EmailContentWriter:

    def EmailWriter(self):
        return Agent(
            role = "EmailWriter",
            goal = "Write a strong email that connects with readers and gets them to click or buy.",
            backstory = "Skilled in crafting engaging and persuasive email content, with a focus on conversion and engagement",
            verbose = True,
            llm = llm
        )
    
    def AudienceAnalyst(self):
        return Agent(
            role = "Audience Analyst",
            goal = "Analyze the audience and tailor the email content to their needs and preferences",
            backstory = "Experienced in audience analysis and segmentation, with a focus on creating targeted and effective",
            verbose = True,
            llm = llm
        )

    
