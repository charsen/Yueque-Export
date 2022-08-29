from glob import glob
from pathlib import Path
import os
 
dirs = [ d for d in glob("./**/")]
 
# 用在本文件夹内则调整为下列代码
# dirs = [ d for d in glob("./")]

print("\n start:")
 
# 提取所有的md文档路径
al1_file_pathes=[]
for dir in dirs:
    file_list=Path(dir).glob("*.md")
    for file in file_list:
        al1_file_pathes.append(".\\"+str(file))
        print(file)
 
         
# 批量转化所有的md文档为docx
for md_path in al1_file_pathes:
    doc_path=md_path.replace(".md",".docx")
    command_new="pandoc -s "+md_path+" -o "+doc_path 
    print(command_new)
    try:
        res=os.popen(command_new).readlines()
        if len(res)==0:
            print(md_path,"已经转化为",doc_path_2)
    except Exception as e:
        print(e)