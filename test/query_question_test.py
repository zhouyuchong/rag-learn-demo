'''
Author: zhouyuchong
Date: 2024-12-11 11:13:26
Description: 
LastEditors: zhouyuchong
LastEditTime: 2024-12-11 14:35:20
'''
import os

import chromadb
from langchain.prompts import ChatPromptTemplate
from llama_index.postprocessor.dashscope_rerank import DashScopeRerank
from llama_index.core import StorageContext,load_index_from_storage,Settings
from llama_index.embeddings.dashscope import (
    DashScopeEmbedding,
    DashScopeTextEmbeddingModels,
    DashScopeTextEmbeddingType,
)
from openai import OpenAI

EMBED_MODEL = DashScopeEmbedding(
    model_name=DashScopeTextEmbeddingModels.TEXT_EMBEDDING_V2,
    text_type=DashScopeTextEmbeddingType.TEXT_TYPE_DOCUMENT,
)
# 若使用本地嵌入模型，请取消以下注释：
# from langchain_community.embeddings import ModelScopeEmbeddings
# from llama_index.embeddings.langchain import LangchainEmbedding
# embeddings = ModelScopeEmbeddings(model_id="modelscope/iic/nlp_gte_sentence-embedding_chinese-large")
# EMBED_MODEL = LangchainEmbedding(embeddings)

# 设置嵌入模型
Settings.embed_model = EMBED_MODEL

DB_PATH = 'VectorStore/'
db_name = "data"
def main():
    prompt = "5G"

    dashscope_rerank = DashScopeRerank(top_n=5,return_documents=True)
    storage_context = StorageContext.from_defaults(persist_dir=os.path.join(DB_PATH,db_name))
    index = load_index_from_storage(storage_context)
    print("index获取完成")
    retriever_engine = index.as_retriever(
        similarity_top_k=20,
    )

    # print(retriever_engine.map("价格"))
    retrieve_chunk = retriever_engine.retrieve("5G")
    # print(f"原始chunk为：{retrieve_chunk}\n")
    for node in retrieve_chunk:
        print(node.score, node.text)

    print("\n\n\n")

    results = dashscope_rerank.postprocess_nodes(retrieve_chunk, query_str=prompt)
    for node in results:
        print(node.score, node.text)
    # pass

if __name__ == '__main__':
    main()