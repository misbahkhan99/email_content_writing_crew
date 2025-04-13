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