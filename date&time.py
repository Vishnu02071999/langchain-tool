from datetime import datetime
from langchain_core.tools import tool


@tool
def current_datetime_tool() -> str:
    """
    Returns the current date and time.
    """

    now = datetime.now()

    return now.strftime("%A, %d %B %Y | %I:%M:%S %p")


# Example usage
result = current_datetime_tool.invoke({})

print(result)