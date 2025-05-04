# code to demonstrate the usage of text loaders in langchain
# used to load and standardize data for processing

from langchain_community.document_loaders import TextLoader

loader = TextLoader('sample_docs/s1.txt', encoding='utf-8')

doc=loader.load()
print (len((doc)))
print (type(doc))
print(doc[0])

# we can use this doc however we want, like creating a chain