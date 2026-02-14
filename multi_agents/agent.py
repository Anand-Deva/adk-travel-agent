from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os
from dotenv import load_dotenv
import datetime
from zoneinfo import ZoneInfo


load_dotenv()

AGENT_MODEL = "openai/gpt-5-nano" 
#AGENT_MODEL= "gemini/gemini-2.5-flash-lite"

def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (f"Sorry, I don't have timezone information for {city}."),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    return {"status": "success", "report": report}

root_agent = Agent(
    name="travel_planner",
    model= LiteLlm(AGENT_MODEL),
    description="An agent the helps users plan their travel itineraries.",
    instruction="You are a travel planner agent. Help the user plan their trips effectively.",
    tools=[get_current_time]
    )