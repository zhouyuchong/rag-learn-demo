'''
Author: zhouyuchong
Date: 2024-12-18 11:02:59
Description: 
LastEditors: zhouyuchong
LastEditTime: 2024-12-18 15:49:24
'''
import json
from langchain.prompts import ChatPromptTemplate
from docling.document_converter import DocumentConverter
from PIL import Image
import base64
from io import BytesIO


def load_ms_docx(file_path):
    """use docling load ms docx file first, return raw_doc, text and markdown
    """
    converter = DocumentConverter()
    raw_doc = converter.convert(file_path).document
    return raw_doc, raw_doc.export_to_text(), raw_doc.export_to_markdown()

def get_titles(client, doc):
    template = """你是一个AI助手, 你的任务是对于给定的文章进行总结, 稍后会根据你返回的标题列表对文章进行划分。 
            总结的内容应该包含以下内容: 产品名称和标题, 所有内容应该都来自于原文，不需要除了标题以外的其他内容, 尤其注意只需要一级标题而不需要二级标题。 
            返回的格式应该如下: "产品名称:xxx|标题一|标题二|标题三...." 
            文章原文: {doc}"""
    prompt_perspectives = ChatPromptTemplate.from_template(template)
    prompt_content = prompt_perspectives.format(doc=doc)

    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt_content},
        ]
    )
    return completion.choices[0].message.content

def get_content_from_image(client, image_data, doc=""):
    """use multimodal llm to understand the image and return content
    Params:
        image_data: base64 encoded image data, format: data:image/png;base64,iVBORw0KGgoAAAANS...
        prompt: prompt for multimodal llm to understand the image
    Returns:
        content: content extracted from the image
    """
    template = "你是一个AI助手, 现在你需要对一张图片里面的文字进行识别，注意不需要对除文字外的内容进行描述。\
            然后将识别出来的文字进行逻辑上的梳理，不需要进行内容上的扩展发散和联想。"

    response = client.chat.completions.create(
        model="qwen-vl-plus",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": template},
                    {
                        "type": "image_url",
                        "image_url": {"url": image_data,}
                    },
                ],
            }
        ],
        temperature=0,
    )
    content = json.loads(response.model_dump_json())['choices'][0]['message']['content']
    return content


def get_content_from_table(client, doc):
    template = """你是一个AI助手, 现在有一段含有markdown表格格式的文本, 
            你的任务是将文本中的markdown表格转换为可阅读的文本内容, 除此之外的任何内容都不要更改" 
            文本原文: {doc}"""
    prompt_perspectives = ChatPromptTemplate.from_template(template)
    prompt_content = prompt_perspectives.format(doc=doc)

    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt_content},
        ],
        temperature=0
    )
    return completion.choices[0].message.content


def check_resize_image(base64_str, scale_factor=2):
    base64_data = base64_str.split(",")[-1]
    prefix = base64_str.split(",")[0]
    image_data = base64.b64decode(base64_data)
    
    # Create a BytesIO object from the decoded image data
    image_stream = BytesIO(image_data)
    
    image = Image.open(image_stream)
    original_width, original_height = image.size
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)
    resized_image = image.resize((new_width, new_height), resample=0)
    output_stream = BytesIO()
    resized_image.save(output_stream, format=image.format)
    
    base64_encoded_image = base64.b64encode(output_stream.getvalue()).decode('utf-8')
    return f"{prefix};base64,{base64_encoded_image}"
    