from .agents import EmailContentWriter
from .tasks import EmailContentTask
from crewai import Crew


agents = EmailContentWriter()
tasks = EmailContentTask()

#obj 
EmailWriter = agents.EmailWriter()
AudienceAnalyst = agents.AudienceAnalyst()


#task
EmailWriterTask = tasks.EmailWriterTask(
    agent = EmailWriter,
    topic = "Write email for leaving one weak from office for personal work"
)
AnalyzeTargetAudienceTask = tasks.AnalyzeTargetAudienceTask(
    agent = AudienceAnalyst,
    context = [EmailWriterTask]
)


#crew
crew = Crew(
    agents = [EmailWriter,AudienceAnalyst],
    tasks = [EmailWriterTask, AnalyzeTargetAudienceTask],
    verbose = True
)

def main():
    result = crew.kickoff()
    print(f"final result: {result}")