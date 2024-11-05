import requests
def get_jizai_ddns_ip():
    # 定义API请求的URL  官方还没给
    url = "https://baidu.com/api"

    # 定义请求参数
    params = {
        'email': 'l@live.com',  # 请输入邮箱
        'passwd': 'password',          # 请输入服务器密码
        'ipaddr': '11.1.1.1'         # 请输入服务器内网IP
    }

    # 发送GET请求
    response = requests.get(url, params=params)

    # 解析返回的JSON响应
    data = response.json()

    # 根据返回的代码处理结果
    if data['code'] == 200:
        print(f"请求成功！前置IP: {data['ip']}, 已使用流量: {data['traffic_used']}, 总流量: {data['traffic_all']}")
        return data['ip']
    else:
        print(f"请求失败，错误信息: {data['message']}")
