import requests
import urllib3
import json

# 关闭ssl认证时，取消警告提示信息
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 接口测试的根目录和用户名-密码
base_url = "https://10.245.36.148/"
username = "root"
password = "0penBmc"


headers = {"Content-Type": "application/json"}

response = requests.get(base_url+"redfish/v1", headers=headers, auth=(username, password), verify=False)

# 获取响应的状态码
print(response.url, response.status_code)

"""
1. 从文件中读取，判断是什么请求
2. 发送对应的请求信息
3. 如果是get请求，那么返回状态码为200，则pass
4. patch
5. post
6. delete
"""

# patch
'''
当资源存在时：
    PATCH 用于资源的部分内容的更新
    PUT 用于更新某个资源较完整的内容
当资源不存在时
    PATCH 可能会去创建一个新的资源，像是 saveOrUpdate
    PUT 只对已有资源进行更新操作，所以是 update 操作
'''
paramdata = {"Boot": {"BootSourceOverrideEnabled": "Disabled", "BootSourceOverrideTarget": "Cd"}, "IndicatorLED": "On"}

paramdata = json.dumps(paramdata)
response = requests.patch(base_url+"redfish/v1/Systems/system", data=paramdata, auth=(username, password), verify=False)

# 获取响应内容,并转换格式
# result = json.dumps(json.loads(response.text), indent=4)
# print(result)

print(response.url, response.status_code)
# print(response.text)

# post


# delete
delete_name = "ymh"
response = requests.delete(base_url+"redfish/v1/AccountService/Accounts/"+delete_name, auth=(username, password), verify=False)

print(response.url, response.status_code)


