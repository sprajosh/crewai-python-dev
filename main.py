import os

import agentops
from crewai import Crew
from crewai.process import Process
from dotenv import load_dotenv

from agents import EmployeeAgents
from tasks import EmployeeTasks

load_dotenv()

AGENTOPS_API_KEY = os.environ["AGENTOPS_API_KEY"]


class CodeEngine:
    """A class to run a code evaluation engine using different employee agents."""

    def run(self, task: str) -> str:
        """
        Execute the code evaluation process with the given task.

        Args:
            task (str): The task description to be assigned to agents.

        Returns:
            str: The result of the crew's task execution.
        """
        agents = EmployeeAgents()
        tasks = EmployeeTasks(task)

        coder = agents.coder()
        manager = agents.manager()
        qa_engineer = agents.qa_engineer()

        coder_task = tasks.coder_task(coder)
        qa_task = tasks.qa_task(qa_engineer)
        manager_task = tasks.manager_task(manager)

        crew = Crew(
            agents=[coder, qa_engineer],
            tasks=[manager_task, coder_task, qa_task],
            verbose=True,
            process=Process.hierarchical,
            manager_agent=manager,
        )

        return crew.kickoff()


def main():
    """Main function to initialize the code engine and run the task."""
    task = (
        "Write a python program to add 2 numbers. "
        "Do not take more than 1 chance at this."
    )

    agentops.init(AGENTOPS_API_KEY)

    code_engine = CodeEngine()
    result = code_engine.run(task)
    agentops.end_session("Success")
    print(result)


if __name__ == "__main__":
    main()
