'''
Author: zhouyuchong
Date: 2024-12-09 16:30:11
Description: 
LastEditors: zhouyuchong
LastEditTime: 2024-12-09 16:59:54
'''
import os
from llama_index.postprocessor.dashscope_rerank import DashScopeRerank

os.environ['DASHSCOPE_API_KEY'] = "sk-b9c2d6517ef648e190dcb4a6dad32708"


dashscope_rerank = DashScopeRerank(top_n=3,return_documents=True)
print(dashscope_rerank.__dict__)