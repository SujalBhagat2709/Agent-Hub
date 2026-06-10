import os


class AgentManager:

    def __init__(self):

        self.agents = {
            "pdf": "PDF Agent",
            "csv": "CSV Agent",
            "file": "File Agent",
            "image": "Image Agent"
        }

    def detect_agent(
        self,
        task
    ):

        task = task.lower()

        if (
            ".pdf" in task
            or
            "pdf" in task
            or
            "summarize"
            in task
        ):

            return "pdf"

        elif (
            ".csv" in task
            or
            "csv" in task
            or
            "dataset" in task
        ):

            return "csv"

        elif (
            ".jpg" in task
            or
            ".png" in task
            or
            "image" in task
        ):

            return "image"

        return "file"

    def get_agent_name(
        self,
        agent
    ):

        return self.agents.get(
            agent,
            "Unknown Agent"
        )


if __name__ == "__main__":

    manager = AgentManager()

    task = input(
        "Task: "
    )

    agent = manager.detect_agent(
        task
    )

    print(
        manager.get_agent_name(
            agent
        )
    )