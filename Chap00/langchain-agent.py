# pip install wikipedia
# pip install numexpr
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_openai import OpenAI


llm = OpenAI(temperature=0.6, 
    api_key="lm-studio",
    base_url="http://localhost:1234/v1"  # see chapter 1 video 3)
)
tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = initialize_agent(
    tools,
    llm,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True,
    handle_parsing_errors=True,
)

agent.run("When was Elon Mush born? what is his age right now in 2023")
