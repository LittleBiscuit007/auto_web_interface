import requests

# 接口测试的根目录
base_url = "https://10.245.22.445/"


# url = "redfish/v1"
# response = requests.get(base_url+"/redfish/v1")
response = requests.get("https://www.baidu.com")

# 获取响应的状态码
print(response.status_code)

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
response_p = requests.patch()

