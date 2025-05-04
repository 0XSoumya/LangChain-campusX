from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path = 'C:\Users\soumy\OneDrive\Desktop\DSAI Meta',
    glob = '*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()
print(len(docs))