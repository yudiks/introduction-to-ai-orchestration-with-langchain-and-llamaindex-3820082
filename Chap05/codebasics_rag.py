from langchain_community.document_loaders import TextLoader

loader = TextLoader("Chap05/nvda_news_1.txt")
data = loader.load()
print(data[0])

