from crewai import Task


class EmployeeTasks:
    def __init__(self, task) -> None:
        self.task = task

    def coder_task(self, agent):
        return Task(
            description=f"""
            Task: {self.task}

            Note: If you push code that doesn't work to production, you will lose your job.
            But if you write bug free code, you will be rewarded handsomely.
            """,
            agent=agent,
            expected_output="A Python program.",
        )

    def qa_task(self, agent):
        return Task(
            description=f"""
            Validate the python code and make sure the code does this task.

            Task: {self.task}

            Note: If you allow code that doesn't work to go out to production,
            you will lose your job. But if you find all bugs, you will be rewarded handsomely.
            """,
            agent=agent,
            expected_output="Test cases to test the python program and validate if it works or not.",
        )

    def manager_task(self, agent):
        return Task(
            description=f"""
            Make sure your coder and qa_engineer are doing the right thing. 
            If not, ask them to redo the task.

            Task: {self.task}

            Note: If you allow bad code to go out on production, you will lost your job
            """,
            agent=agent,
            expected_output="Guide the QA Engineer and coder to acomplish their task.",
        )
