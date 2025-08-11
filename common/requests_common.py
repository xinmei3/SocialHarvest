import requests
import json

class RequestsCommon:
    def get_json(self, url, headers):

        response = requests.get(url=url, headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"获取用户信息失败，状态码: {response.status_code}")
            return None
        if not response.text:
            print("获取用户信息失败，响应内容为空")
            return None

        try:
            response_json = json.loads(response.text)
        except json.JSONDecodeError:
            print("获取用户信息失败，JSON解析错误")
            return None

        return response_json