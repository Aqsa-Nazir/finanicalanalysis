# converting the data into model readable json files (converting into indexed data)
# wish to create new json files then empty the storage folder and then run it
import os, config
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

os.environ['OPENAI_API_KEY'] = config.OPENAI_API_KEY

documents = SimpleDirectoryReader('articles').load_data()

index = GPTVectorStoreIndex.from_documents(documents)

index.storage_context.persist()
