from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent, tool, AgentType
from langchain_community.tools import TavilySearchResults
import datetime
import os

load_dotenv()

from pydantic import SecretStr

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-pro",  
    api_key=SecretStr(os.environ["GOOGLE_API_KEY"])
)

search_tool = TavilySearchResults(search_depth="basic")

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time


tools = [search_tool, get_system_time]

agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True,  handle_parsing_errors=True )

agent.invoke({"input": "When was SpaceX's last launch and how many days ago was that from this instant"})
