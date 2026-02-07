"""
request 请求
GET
"""
import os

import requests
import json
from _04_env_load import load_env

load_env("local")

print(os.getenv("HTTP_PROXY"))
print(os.getenv("HTTPS_PROXY"))

# =============Get 请求=====================#
# 禁用代理（解决代理连接问题）
#response = requests.get("https://api.github.com", proxies={"http": None, "https": None})

#print(f"状态码：{response.status_code}")
#print(f"内容:\n{json.dumps(response.json(), indent=2, ensure_ascii=False)}")


#user_response = requests.get("https://api.github.com/user",auth="", proxies={"http": None, "https": None})
#print(f"状态码：{user_response.status_code}")
#print(f"内容:{user_response.text}")


# =============带参数的Get 请求=====================#

params: dict[str, str] = {
    "q": "python",
    "sort": "start",
    "order": "desc"
}

response_search = requests.get("https://api.github.com/search/repositories", params=params,
                               proxies={"http": None, "https": None})
data = response_search.json()
# print(f"data = \n{json.dumps(data, indent=2, ensure_ascii=False)}")
print(f"data = {data['total_count']}")

# =============带请求头的Get 请求=====================#

github_token: str = f"Bearer {os.getenv('GIT_HUB_TOKEN')}"
headers: dict[str, str] = {
    "Authorization": github_token,
    "Accept": "application/json"
}

response = requests.get(
    "https://api.github.com/user",
    headers=headers,
    proxies={"http": None, "https": None}
)

user = response.json()
print(f"用户: {user['login']}")
print(f"用户: {json.dumps(user, indent=2, ensure_ascii=False)}")

#============响应处理==================
response = requests.get("https://api.github.com", proxies={"http": None, "https": None})

# 文本内容
text: str = response.text
print(f"响应体文本内容={text}")

# json 内容
json = response.json()
print(f"响应体json内容={json}")

# 二进制内容
binary = response.content
print(f"响应体二进制内容={binary}")

# 响应头
headers = response.headers
print(f"Content-Type: {headers['Content-Type']}")

#========错误处理===============
try:
    response = requests.get("https://api.github.com/invalid", timeout=5)
    # 非 2xx 状态码会抛出异常
    response.raise_for_status()
except requests.Timeout:
    print("请求超时")
except requests.ConnectionError:
    print("连接错误")
except requests.HTTPError as e:
    print(f"HTTP 错误: {e}")
except requests.RequestException as e:
    print(f"请求异常: {e}")
