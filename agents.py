from crewai import Agent

MAX_ITERATIONS = 1


class EmployeeAgents:
    """A class to create different types of employee agents."""

    def coder(self) -> Agent:
        """
        Create a Coder agent.

        Returns:
            Agent: An agent with the role of Coder, responsible for writing software.
        """
        return Agent(
            role="Coder",
            goal="Writes the software after consulting with the manager agent",
            backstory="A knowledgeable software engineer who has decades of experience building complex systems.",
            verbose=True,
            memory=True,
            max_iter=MAX_ITERATIONS,
        )

    def qa_engineer(self) -> Agent:
        """
        Create a QA Engineer agent.

        Returns:
            Agent: An agent with the role of QA Engineer, responsible for testing and verifying code.
        """
        return Agent(
            role="QA Engineer",
            goal="Test and verify the code written by the coder",
            backstory="""A knowledgeable QA engineer who can test and verify code
              written by other developers to make sure no bugs ever go out in production environment.""",
            verbose=True,
            memory=True,
            max_iter=MAX_ITERATIONS,
        )

    def manager(self) -> Agent:
        """
        Create a Manager agent.

        Returns:
            Agent: An agent with the role of Manager, responsible for coordinating between QA Engineer and Coder and ensuring proper code acceptance.
        """
        return Agent(
            role="Manager",
            goal="Helps Coder with their work. Coordinates between QA Engineer and Coder to make sure tests are run properly. Make sure all the code that is accepted is proper.",
            backstory="A knowledgeable software engineer who has decades of experience working on complex systems and now helps other engineers get better at their work.",
            verbose=True,
            memory=True,
            max_iter=MAX_ITERATIONS,
        )
