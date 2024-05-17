# pip install llama-index-llms-openai-like
from llama_index.llms.openai_like import OpenAILike
from llama_index.core.llms import ChatMessage
from llama_index.core.readers import SimpleDirectoryReader

application_prompt = """Summarize the following doc

    DOCUMENT:
"""

llm = OpenAILike(
    is_chat_model=True,
    model="local",
    api_key="lm-studio",
    api_base="http://localhost:1234/v1",
    temperature=0.7,
)

documents = SimpleDirectoryReader("handbook").load_data()

# documents will be a list of Documents

fulltext = "<join together docs into one string>"
textlen = len(fulltext)
print(f"Document text size is {textlen}")
if textlen > 100000:
    print("Too much text to fit in context window")
    exit()

messages = [
    ChatMessage(role="system", content=application_prompt),
    ChatMessage(role="user", content=fulltext),
]
results = llm.chat(messages)

with open("summary.txt", "w") as f:
    f.write(results.message.content)
