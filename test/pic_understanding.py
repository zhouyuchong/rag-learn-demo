'''
Author: zhouyuchong
Date: 2024-12-09 11:37:58
Description: 
LastEditors: zhouyuchong
LastEditTime: 2024-12-24 15:03:53
'''
import os
# 设置环境变量
from openai import OpenAI
from langchain.prompts import ChatPromptTemplate
import base64
import json

def get_content_from_image(client, image_data, prompt="概括描述这张图片"):
    """use multimodal llm to understand the image and return content
    Params:
        image_data: base64 encoded image data, format: data:image/png;base64,iVBORw0KGgoAAAANS...
        prompt: prompt for multimodal llm to understand the image
    Returns:
        content: content extracted from the image
    """
    response = client.chat.completions.create(
        model="qwen-vl-plus",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": image_data,}
                    },
                ],
            }
        ],
    )
    print(response)
    content = json.loads(response.model_dump_json())['choices'][0]['message']['content']
    return content


if __name__ == "__main__":
    image_path = "data/out_0.png"
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    content_return = get_content_from_image(encoded_image)
    print(content_return)

