from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders.csv_loader import CSVLoader

loader = TextLoader("Chap05/nvda_news_1.txt")
data = loader.load()
print(data[0])

print(data[0].page_content)
print(data[0].metadata)


loader = CSVLoader("Chap05/movies.csv")
data = loader.load()
print(data)