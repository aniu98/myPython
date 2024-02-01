import os
import hashlib

# 获取指定目录下所有文件的路径
def get_files_list(path):
    files_list = []
    for root, dirs, files in os.walk(path):
        for name in files:
            files_list.append(os.path.join(root, name))
    return files_list

# 计算文件的哈希值
def get_file_md5(file_path):
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        while True:
            data = f.read(1024)
            if not data:
                break
            md5obj.update(data)
        return md5obj.hexdigest()

def find_duplicate_files(path):
    file_md5_dict = {}
    duplicate_files = []
    files_list = get_files_list(path)
    for file_path in files_list:
        file_md5 = get_file_md5(file_path)
        print(file_md5,file_path)
        if file_md5 in file_md5_dict:
            duplicate_files.append(file_path)
        else:
            file_md5_dict[file_md5] = file_path
    return duplicate_files


find_duplicate_files("C:\\Users\\admin\\Downloads")