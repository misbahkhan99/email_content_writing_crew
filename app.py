import streamlit as st
from src.email_content_writing_crew.agents import EmailContentWriter
from src.email_content_writing_crew.tasks import EmailContentTask
from crewai import Crew

# Initialize agents and tasks
agents = EmailContentWriter()
tasks = EmailContentTask()

# Create instances of the agents
EmailWriter = agents.EmailWriter()
AudienceAnalyst = agents.AudienceAnalyst()
ComplianceChecker = agents.ComplianceChecker()

# Create instances of the tasks
EmailWriterTask = tasks.EmailWriterTask(
    agent = EmailWriter,
    topic = "Write email for leaving one week from office for personal work"
)
AnalyzeTargetAudienceTask = tasks.AnalyzeTargetAudienceTask(
    agent = AudienceAnalyst,
    context = [EmailWriterTask]
)
ComplianceCheckerTask = tasks.ComplianceCheckerTask(
    agent = ComplianceChecker,
    context = [AnalyzeTargetAudienceTask]
)

# Crew setup
crew = Crew(
    agents = [EmailWriter, AudienceAnalyst, ComplianceChecker],
    tasks = [EmailWriterTask, AnalyzeTargetAudienceTask, ComplianceCheckerTask],
    verbose = True
)

# Streamlit app layout
def main():
    st.title("Email Content Writer Agent")

    # Input section for user to specify the topic of the email
    topic = st.text_input("Enter the email topic:", " ")

    if st.button("Generate Email"):
        # Update the task with the new topic
        EmailWriterTask = tasks.EmailWriterTask(
            agent = EmailWriter,
            topic = topic
        )
        
        # Recreate the task dependencies
        AnalyzeTargetAudienceTask = tasks.AnalyzeTargetAudienceTask(
            agent = AudienceAnalyst,
            context = [EmailWriterTask]
        )
        ComplianceCheckerTask = tasks.ComplianceCheckerTask(
            agent = ComplianceChecker,
            context = [AnalyzeTargetAudienceTask]
        )

        # Update crew with new tasks
        crew = Crew(
            agents = [EmailWriter, AudienceAnalyst, ComplianceChecker],
            tasks = [EmailWriterTask, AnalyzeTargetAudienceTask, ComplianceCheckerTask],
            verbose = True
        )
        
        # Run the crew's task
        result = crew.kickoff()

        # Display result to the user
        st.write(f"Final result: {result}")

# Run the app
if __name__ == "__main__":
    main()
