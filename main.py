import agentops
from crewai import Crew, Task

from agents import EmployeeAgents


class CodeEngine:
    def run(self, task):
        agents = EmployeeAgents()

        coder = agents.coder()
        manager = agents.manager()
        qa_engineer = agents.qa_engineer()

        coder_task = Task(
            description=f"""
            Task: {task}

            Note: If you push code that doesn't work to production, you will lose your job.
            But if you write bug free code, you will be rewarded handsomely.
            """,
            agent=coder,
            expected_output="A numerical answer.",
        )
        qa_task = Task(
            description=f"""
            Validate the python code and make sure the code does this.

            Task: {task}

            Note: If you allow code that doesn't work to go out to production,
            you will lose your job. But if you find all bugs, you will be rewarded handsomely.
            """,
            agent=coder,
            expected_output="A numerical answer.",
        )

        manager_task = Task(
            description=f"""
            Make sure your coder and qa_engineer are doing the right thing. 
            If not, ask them to redo the task.

            Task: {task}

            Note: If you allow bad code to go out on production, you will lost your job
            """,
            agent=coder,
            expected_output="A numerical answer.",
        )

        crew = Crew(
            agents=[coder, manager, qa_engineer],
            tasks=[coder_task, qa_task, manager_task],
            verbose=True,
        )

        return crew.kickoff()


if __name__ == "__main__":
    # task = input("What task do you want to get done today?")
    task = "Given a postfix expression, the task is to write a python program to evaluate the postfix expression."

    agentops.init()
    code_engine = CodeEngine()
    result = code_engine.run(task)

    print(result)
