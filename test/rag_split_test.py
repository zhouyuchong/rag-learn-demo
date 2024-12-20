'''
Author: zhouyuchong
Date: 2024-12-09 14:17:55
Description: 
LastEditors: zhouyuchong
LastEditTime: 2024-12-17 13:38:10
'''
import os
import shutil
import pandas as pd
from upload_file import upload_structured_file

def main():
    files = ["data.xlsx"]

    # for file in files:
        # print(file.name)
        # file_path = file.name
        # file_name = os.path.basename(file_path)
        # destination_file_path = os.path.join(STRUCTURED_FILE_PATH,label_name,file_name)
    # shutil.move(file_path,destination_file_path)
    destination_file_path = "data.xlsx"
    if os.path.splitext(destination_file_path)[1] == ".xlsx":
        df = pd.read_excel(destination_file_path, sheet_name=1)
    elif os.path.splitext(destination_file_path)[1] == ".csv":
        df = pd.read_csv(destination_file_path)

    df = df.fillna(method="ffill", axis=0)
    columns = df.columns
    with open('out.txt',"w") as file:
        for idx,row in df.iterrows():
            file.write("【")
            info = []
            for col in columns:
                info.append(f"{col}:{row[col]}")
            infos = ",".join(info)
            # print(infos)
            file.write(infos)
            if idx != len(df)-1:
                file.write("】\n")
            else:
                file.write("】")
    # os.remove(destination_file_path)

if __name__ == "__main__":
    main()