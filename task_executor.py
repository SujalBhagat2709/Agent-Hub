from agent_manager import (
    AgentManager
)

import time


def execute_pdf_agent(
    task
):

    print(
        "\n📄 PDF Agent Activated"
    )

    time.sleep(1)

    print(
        "Extracting Text..."
    )

    time.sleep(1)

    print(
        "Generating Summary..."
    )

    print(
        "\n✅ summary.docx created"
    )


def execute_csv_agent(
    task
):

    print(
        "\n📊 CSV Agent Activated"
    )

    time.sleep(1)

    print(
        "Analyzing Dataset..."
    )

    time.sleep(1)

    print(
        "Generating Report..."
    )

    print(
        "\n✅ report.xlsx created"
    )


def execute_image_agent(
    task
):

    print(
        "\n🖼 Image Agent Activated"
    )

    time.sleep(1)

    print(
        "Processing Image..."
    )

    time.sleep(1)

    print(
        "\n✅ output.jpg created"
    )


def execute_file_agent(
    task
):

    print(
        "\n📁 File Agent Activated"
    )

    time.sleep(1)

    print(
        "Scanning Files..."
    )

    time.sleep(1)

    print(
        "\n✅ task completed"
    )


if __name__ == "__main__":

    print(
        "\n========================"
    )

    print(
        "      AGENT HUB"
    )

    print(
        "========================"
    )

    task = input(
        "\nEnter Task:\n"
    )

    manager = AgentManager()

    agent = manager.detect_agent(
        task
    )

    print(
        f"\nSelected Agent:"
        f" {manager.get_agent_name(agent)}"
    )

    if agent == "pdf":

        execute_pdf_agent(
            task
        )

    elif agent == "csv":

        execute_csv_agent(
            task
        )

    elif agent == "image":

        execute_image_agent(
            task
        )

    else:

        execute_file_agent(
            task
        )