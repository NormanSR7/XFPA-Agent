from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from dotenv import load_dotenv
import os



# Connect local SQLite database
db = SQLDatabase.from_uri("sqlite:///xfpa.db")

# Pull API key from env
load_dotenv()

# Create a ChatOpenAI model
llm = ChatOpenAI(temperature=0, model="gpt-4")

# Create the SQL Agent
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db,llm=llm),
    verbose=True
)

# Ask the agent a question
question = "What is the most expensive product and its price?"
response = agent_executor.invoke({"input":question})

# Print the final answer
print("\n Agent's response:")
print(response['output'])