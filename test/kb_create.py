'''
Author: zhouyuchong
Date: 2024-12-19 13:27:04
Description: 
LastEditors: zhouyuchong
LastEditTime: 2024-12-24 15:03:29
'''
import os
# 设置环境变量
import chromadb

from llama_index.core import VectorStoreIndex,Settings,SimpleDirectoryReader, StorageContext
# from llama_index.vector_stores.chroma import ChromaVectorStore
# from llama_index.embeddings.dashscope import (
#     DashScopeEmbedding,
#     DashScopeTextEmbeddingModels,
#     DashScopeTextEmbeddingType,
# )
# from llama_index.core.schema import TextNode
# from upload_file import *
# DB_PATH = "VectorStore"
# STRUCTURED_FILE_PATH = "File/Structured"
# UNSTRUCTURED_FILE_PATH = "File/Unstructured"
# TMP_NAME = "tmp_abcd"
# EMBED_MODEL = DashScopeEmbedding(
#     model_name=DashScopeTextEmbeddingModels.TEXT_EMBEDDING_V3,
#     text_type=DashScopeTextEmbeddingType.TEXT_TYPE_DOCUMENT,
# )

# Settings.embed_model = EMBED_MODEL
def main():
    documents = []
    label = "云电脑"
    label_path = os.path.join(STRUCTURED_FILE_PATH,label)
    documents.extend(SimpleDirectoryReader(label_path).load_data())

    nodes = []
    for doc in documents:
        doc_content = doc.get_content().split('\n')
        for chunk in doc_content:
            # print(chunk, '\n\n')
            node = TextNode(text=chunk)
            node.metadata = {'source': doc.get_doc_id(),'file_name':doc.metadata['file_name']}
            print(node, '\n\n')
            nodes = nodes + [node]

    db = chromadb.PersistentClient(path="./chroma_db")
    collection_name = 'cloud_computer'
    chroma_collection = db.get_or_create_collection(collection_name)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex(nodes, storage_context=storage_context)

    # db_path = os.path.join(DB_PATH,label)
    # if not os.path.exists(db_path):
    #     os.mkdir(db_path)
    # index.storage_context.persist(db_path)

def chroma_load():
    prompt = "国密加密算法支持，安全有保障；便利备份及恢复，保护数据资产"
    db2 = chromadb.PersistentClient(path="./chroma_db")
    # collections = db2.list_collections()
    # # db2.get_or_create_collection("quickstart_2")

    print(db2.list_collections())
    # 打印集合名称
    # for collection_name in collections:
    #     print(collection_name)

    # db2.delete_collection(name='quickstart')

    # chroma_collection = db2.get_or_create_collection("quickstart")
    # vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    # index = VectorStoreIndex.from_vector_store(
    #     vector_store,
    #     # embed_model=embed_model,
    # )
    # print(index)
    # retriever_engine = index.as_retriever(
    #     similarity_top_k=20,
    # )
    # retrieve_chunk = retriever_engine.retrieve(prompt)

    # Query Data from the persisted index
    # query_engine = index.as_query_engine()
    # response = query_engine.query("What did the author do growing up?")
    # print(response)

if __name__ == '__main__':
    # main()
    chroma_load()