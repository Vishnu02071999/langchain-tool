from langchain_core.tools import tool
import requests


@tool
def weather_tool(city: str) -> str:
    """
    Returns the current weather for a given city.
    """
    url = f"https://wttr.in/{city}?format=3"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception:
        return "Unable to fetch weather information."


# Example usage
query = "Bangalore"

result = weather_tool.invoke(query)

print("City:", query)
print("Weather:", result)