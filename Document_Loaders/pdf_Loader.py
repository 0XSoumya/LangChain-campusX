from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader
# pypdf is only good for text based pdf with single columns
# for tables\columns pdfplumberloader
# for scanned docs unstructuredloader or amazontextract
# for layouts or image pymupdfloader
# for best structure extraction unstructuredloader

loader = PyPDFLoader('sample_docs/peft.pdf')
docs = loader.load()
print(docs[0].page_content,'\n')
print(docs[1].metadata)

