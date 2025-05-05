from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('sample_docs\dl-curriculum.pdf')
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator= ''
) 

# there is no space, we get exact 100 chunk-size, but it may include partial words
#use ' ' to achieve chunks with whole words and slightly varying chunk size
# overlap as the name suggests, decides overlapping between two chunks
result = splitter.split_documents(docs)
print(result[2])