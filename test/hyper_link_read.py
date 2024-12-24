'''
Author: zhouyuchong
Date: 2024-12-23 09:19:05
Description: 
LastEditors: zhouyuchong
LastEditTime: 2024-12-23 11:38:28
'''
from docx import Document
from langchain.prompts import ChatPromptTemplate
from docling.document_converter import DocumentConverter


doc = Document("data/iot_charger.docx")

# print(type(doc.text))
# print(doc.__dict__)

# print(doc.hyperlinks)

# count = 0
# for paragraph in doc.paragraphs:
#     # print(paragraph.hyperlinks)
#     # print(count, paragraph.text)
#     print(count, paragraph._p.xml)

#     count += 1

import zipfile
import os

docx_file = 'data/iot_charger.docx'
extract_folder = 'extracted_files'

with zipfile.ZipFile(docx_file, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)
#     for run in paragraph.runs:
        # print(run.text)
        # if run._r.isCT_Hyperlink:
        #         # 获取超链接的锚点（即链接地址）
        #         hyperlink = run._r.hyperlink
        #         anchor = hyperlink.get('anchor')
        #         print(anchor)
        # try:
        #     print(run.hyperlink.address)
        # except Exception:
        #     print("this paragraph has no hyperlink")

# converter = DocumentConverter()
# raw = converter.convert("data/iot_charger.docx").document
# # md = raw_doc.export_to_markdown()
# # print(md)
# # print(raw_doc)
# for i in range(len(raw.pictures)):
#     # image_obj = raw.pictures[i].image
#     # print(raw.pictures[i].self_ref)
#     print(raw.pictures[i])