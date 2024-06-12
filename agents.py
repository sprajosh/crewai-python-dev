from crewai import Agent

MAX_ITERATIONS = 1


class EmployeeAgents:
    def coder(self):
        return Agent(
            role="Coder",
            goal="Writes the software after consulting with the manager agent",
            backstory="A knowledgeable software engineer who has decades of experience building xomplex systems.",
            verbose=True,
            memory=True,
            max_iter=MAX_ITERATIONS,
        )

    def qa_engineer(self):
        return Agent(
            role="QA Engineer",
            goal="Test and verify the code written by the coder",
            backstory="""A knowledgeable QA engineer who can test and verify code
              written by other developers to make sure no bugs ever go out in production environment.""",
            verbose=True,
            memory=True,
            max_iter=MAX_ITERATIONS,
        )

    def manager(self):
        return Agent(
            role="Manager",
            goal="Helps Coder with their work. Coordinates between QA Engineer and Coder to make sure tests are run properly. Make sure all the code that is accepted is proper.",
            backstory="A knowledgeable software engineer who has decades of experience working on complex systems and now helps other engineers get better at their work.",
            verbose=True,
            memory=True,
            max_iter=MAX_ITERATIONS,
        )
