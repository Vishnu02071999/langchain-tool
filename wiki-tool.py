from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain_community.utilities import WikipediaAPIWrapper

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

# Create the Wikipedia wrapper
wiki = WikipediaAPIWrapper()

# Define the tool
wikipedia_tool = Tool(
    name="Wikipedia",
    func=wiki.run,
    description="Useful for retrieving information about people, places, events, and historical topics."
)

# User query
query = "Who is Ada Lovelace?"

# Use the tool directly
result = wikipedia_tool.invoke(query)

print("User Query:")
print(query)

print("\nTool Output:")
print(result)