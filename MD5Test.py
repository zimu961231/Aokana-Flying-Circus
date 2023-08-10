import requests
import hashlib
from io import BytesIO

# def calculate_md5(file_data):
#     md5_hash = hashlib.md5()
#     md5_hash.update(file_data)
#     return md5_hash.hexdigest()
#
# url = 'http://localhost:8111/map.img'
# response = requests.get(url)
#
# if response.status_code == 200:
#     file_data = response.content
#     md5_value = calculate_md5(file_data)
#     print("MD5:", md5_value)
# else:
#     print("Failed to download the file.")



def calculate_md5(file_path):
    with open(file_path, 'rb') as file:
        md5_hash = hashlib.md5()
        while True:
            data = file.read(4096)  # 以块的方式读取文件
            if not data:
                break
            md5_hash.update(data)
    return md5_hash.hexdigest()

# 示例用法
file_path = 'map/PyreneesMountains.img'
md5_value = calculate_md5(file_path)
print("MD5:", md5_value)