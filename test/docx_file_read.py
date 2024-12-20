'''
Author: zhouyuchong
Date: 2024-12-17 13:38:26
Description: 
LastEditors: zhouyuchong
LastEditTime: 2024-12-18 16:12:38
'''
import os
# 设置环境变量
os.environ['DASHSCOPE_API_KEY'] = "sk-b9c2d6517ef648e190dcb4a6dad32708"

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from openai import OpenAI

from util import load_ms_docx, get_titles, get_content_from_image, get_content_from_table, check_resize_image


def format_chunk_from_docx(file_path):
    # use docling load ms docx file first
    raw, doc_txt, doc_md = load_ms_docx(file_path)
    logging.info("Load doc success")

    # get all image in the file and get their content
    image_list = []
    for i in range(len(raw.pictures)):
        image_obj = raw.pictures[i].image
        base64_data = str(image_obj.uri)
        base64_data = check_resize_image(base64_data, scale_factor=5)
        image_list.append(base64_data)
    logging.info(f"Total image num: {len(image_list)}")

    # raw doc is hard to read and split, we first 
    # feed it into llm to summarize it and get titles
    
    client = OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"), 
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )   
    titles = get_titles(client, doc_txt).split("|")
    logging.info(f"Get titles: {titles}")
    product_name = titles[0].split(":")[1]
    
    logging.info("Start to chunk doc")
    title_start_index = 1
    lines = doc_md.split("\n")
    paragraphs = []
    recorder = []
    for index in range(title_start_index, len(titles)):
        print("get title: ", titles[index])
        for i in range(len(lines)):
            if titles[index] in lines[i] and len(lines[i])<=15:
                recorder.append(i+1)

    for i in range(len(recorder)-1):
        paragraphs.append(lines[recorder[i]:recorder[i+1]-1])
    paragraphs.append(lines[recorder[-1]:])

    chunks = []
    paragraph_index = 1
    image_index = 0
    for p in paragraphs:
        table_signal = False
        logging.info(f"Formating paragraph: {titles[paragraph_index]}")
        text = f'【{product_name}的{titles[paragraph_index]}: '
        for line in p:
            if line.startswith("|"):
                logging.info("Find table, will format later")
                text = text + "\n" + line
                table_signal = True
            elif '<!-- image -->' in line:
                logging.info("Find image, start to extract image content...")
                ocr_content = get_content_from_image(client=client, image_data=image_list[image_index])
                if "表格" in ocr_content and '|' in ocr_content:
                    table_signal =  True
                image_index += 1
                text += "\n" + f"此处配图例, 图例内容为: {ocr_content}\n"
            else:
                text += line
        paragraph_index += 1
        if table_signal:
            logging.info("Find table, start to extract table content...")
            text = get_content_from_table(client, text)
        # print(text)
        text = text.replace("\n", " ")
        chunks.append(text)

    return product_name, chunks


def main():
    doc_root_path = 'data'
    dst_root_path = 'File/Structured'
    files = os.listdir(doc_root_path)
    for file in files:
        if file.endswith(".docx"):
            file_path = os.path.join(doc_root_path, file)
            name, chunks = format_chunk_from_docx(file_path)
            dst_dir = os.path.join(dst_root_path, name)
            if not os.path.exists(dst_dir):
                os.mkdir(dst_dir)
            dst_file_path = os.path.join(dst_dir, name+".txt")
            with open(dst_file_path, "w") as f:
                for chunk in chunks:
                    f.write(chunk)
                    f.write("\n")

if __name__ == "__main__":
    main()
