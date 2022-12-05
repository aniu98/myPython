import os

# pip install PyPDF2 -i https://pypi.tuna.tsinghua.edu.cn/simple
from PyPDF2 import PdfFileMerger

target_path = r'E:\\workspace'  ## pdf目录文件
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
print(pdf_lst)
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]
print(pdf_lst)
file_merger = PdfFileMerger()
for pdf in pdf_lst:
    # print(pdf)
    file_merger.append(pdf)     # 合并pdf文件

file_merger.write(r"合并文件.pdf")
