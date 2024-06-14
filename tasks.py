from crewai import Agent, Task


class EmployeeTasks:
    """
    A class to create different tasks for employee agents.

    Attributes:
        task (str): The task description to be assigned to agents.
    """

    def __init__(self, task: str) -> None:
        """
        Initializes the EmployeeTasks class with a specific task.

        Args:
            task (str): The task description.
        """
        self.task = task

    def coder_task(self, agent: Agent) -> Task:
        """
        Create a task for the Coder agent.

        Args:
            agent (Agent): The Coder agent to whom the task is assigned.

        Returns:
            Task: A task assigned to the Coder agent with a description and expected output.
        """
        return Task(
            description=f"""
            Task: {self.task}

            Note: If you push code that doesn't work to production, you will lose your job.
            But if you write bug-free code, you will be rewarded handsomely.
            """,
            agent=agent,
            expected_output="A Python program.",
        )

    def qa_task(self, agent: Agent) -> Task:
        """
        Create a task for the QA Engineer agent.

        Args:
            agent (Agent): The QA Engineer agent to whom the task is assigned.

        Returns:
            Task: A task assigned to the QA Engineer agent with a description and expected output.
        """
        return Task(
            description=f"""
            Validate the Python code and make sure the code performs the task correctly.

            Task: {self.task}

            Note: If you allow code that doesn't work to go out to production,
            you will lose your job. But if you find all bugs, you will be rewarded handsomely.
            """,
            agent=agent,
            expected_output="Test cases to test the Python program and validate if it works or not.",
        )

    def manager_task(self, agent: Agent) -> Task:
        """
        Create a task for the Manager agent.

        Args:
            agent (Agent): The Manager agent to whom the task is assigned.

        Returns:
            Task: A task assigned to the Manager agent with a description and expected output.
        """
        return Task(
            description=f"""
            Make sure your Coder and QA Engineer are doing the right thing. 
            If not, ask them to redo the task.

            Task: {self.task}

            Note: If you allow bad code to go out to production, you will lose your job.
            """,
            agent=agent,
            expected_output="Guide the QA Engineer and Coder to accomplish their tasks.",
        )
