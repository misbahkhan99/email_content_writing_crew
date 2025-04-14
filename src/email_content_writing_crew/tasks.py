from crewai import Task


class EmailContentTask:

    def EmailWriterTask(self, agent, topic):
        return Task(
            agent = agent,
            description = f"""wwrite email on the user mentioned topic 
            parameters:
            topic : {topic}
            """,
            expected_output = "A well-structured, engaging email",

        )
    

    def AnalyzeTargetAudienceTask(self, agent, context):
        return Task(
            agent = agent,
            description = f"""Analyze the target audience for the email""",
            expected_output = "A clear understanding of the target audience",
            context = context
        )
    
    def ComplianceCheckerTask(self, agent, context):
        return Task(
            agent = agent,
            description = " Review email content for compliance with legal requirements and company standards.",
            expected_output = " A compliant email ensuring all communications are appropriate and lawful.",
            context = context
        )