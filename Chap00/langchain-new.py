# pip install langchain
# pip install langchain-community langchain-core
# pip install -U langchain-openai

from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers.list import CommaSeparatedListOutputParser

prompt_template_name = PromptTemplate(
    input_variables = ['cuisine'],
    template = "U want to open a restaurant for {cuisine} food. Suggest a restaurant name",
)

output_parser = CommaSeparatedListOutputParser()
prompt_template_items = PromptTemplate(
    input_variables = ['restaurant_name'],
    template = "Suggest some menu for {restaurant_name}.",
    partial_variables={"format_instructions":  output_parser.get_format_instructions()}
)

llm = OpenAI(temperature=0.6, 
    api_key="lm-studio",
    base_url="http://localhost:1234/v1"  # see chapter 1 video 3)
)

chain = prompt_template_name | prompt_template_items | llm |  output_parser
output =chain.invoke({"cuisine" : "indonesia"})

print(type(output))
print(output)