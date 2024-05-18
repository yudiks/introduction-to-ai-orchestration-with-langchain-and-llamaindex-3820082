# pip install langchain
# pip install langchain-community langchain-core
# pip install -U langchain-openai

from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

prompt_template_name = PromptTemplate(
    input_variables = ['cuisine'],
    template = "U want to open a restaurant for {cuisine} food. Suggest a restaurant name"
)
prompt_template_name.format(cuisine="Italian")


llm = OpenAI(temperature=0.6, 
    api_key="lm-studio",
    base_url="http://localhost:1234/v1"  # see chapter 1 video 3)
)

# chain = LLMChain(llm=llm, prompt=prompt_template_name)
chain = prompt_template_name | llm
print(chain.invoke("Mexican"))
