import json
import os
import pprint

# 获取当前文件所在目录
current_dir = os.path.dirname(__file__)
# 拼接到上一级目录的 user_info.json
json_path = os.path.join(current_dir, "..", "user_info", "user_info.json")

class UserInfo:

    def user_info_loader():
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    

if __name__ == "__main__":
    user_info = UserInfo.user_info_loader()
    pprint.pprint(user_info)
