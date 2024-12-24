'''
Author: zhouyuchong
Date: 2024-12-09 16:30:11
Description: 
LastEditors: zhouyuchong
LastEditTime: 2024-12-09 16:59:54
'''
import os
from llama_index.postprocessor.dashscope_rerank import DashScopeRerank



dashscope_rerank = DashScopeRerank(top_n=3,return_documents=True)
print(dashscope_rerank.__dict__)