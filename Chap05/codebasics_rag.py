from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders.csv_loader import CSVLoader

loader = TextLoader("Chap05/nvda_news_1.txt")
data = loader.load()
print(data[0])

# # print(data[0].page_content)
# # print(data[0].metadata)


# # loader = CSVLoader("Chap05/movies.csv", source_column="title")
# # data = loader.load()
# # print(data)

# # pip install unstructured libmagic python-magic python-magic-bin
# # from langchain.document_loaders import UnstructuredURLLoader
# from langchain_community.document_loaders import UnstructuredURLLoader

# loader = UnstructuredURLLoader(urls=[
#     "https://www.moneycontrol.com/europe/?url=https://www.moneycontrol.com/news/technology/nvidia-stock-climbs-as-cfo-says-new-chip-to-ship-in-2024-12487781.html"])

# data = loader.load()
# len(data)

####################
##  Text Splitter ##
####################
