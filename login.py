import requests
from bs4 import BeautifulSoup
import requests
import time

# 获取当前外部 IP 地址
def get_jizai_ddns_ip():
    # 创建一个会话对象
    session = requests.Session()

    # 定义登录页面的URL
    login_url = "https://bigchick.xyz/index.php/login"

    # 获取登录页面以提取CSRF令牌
    login_page = session.get(login_url)
    soup = BeautifulSoup(login_page.text, 'html.parser')

    # 提取CSRF令牌
    csrf_token = soup.find('input', {'name': 'token'})['value']

    # 定义用户名、密码和CSRF令牌
    payload = {
        "username": "exp.qq.com", #你的鸡仔云登录邮箱
        "password": "passwd", #你的密码
        "token": csrf_token
    }

    # 发送POST请求以登录
    response = session.post(login_url, data=payload)

    # 检查是否登录成功
    if "clientarea.php" in response.url:
        print("登录成功！")
    else:
        print("登录失败！状态码:", response.status_code)
        print(response.text)  # 打印响应内容以查看错误信息

    # 使用已登录的会话进行后续请求，这个是对应的某个IPV6-NAT VPS产品页面。
    protected_url = "https://bigchick.xyz/clientarea.php?action=productdetails&id=0000"
    protected_response = session.get(protected_url)

    # 检查访问受保护页面的结果
    if protected_response.status_code == 200:
        print("成功访问受保护的页面！")
        # print(protected_response.text)  # 打印页面内容
    else:
        print("无法访问受保护的页面！状态码:", protected_response.status_code)

    # 解析受保护页面的HTML
    protected_soup = BeautifulSoup(protected_response.text, 'html.parser')

    # 从response中提取DDNS地址
    ddns_address = None
    list_items = protected_soup.select('div.panel-body ul.list-group li.list-group-item-success')
    for item in list_items:
        if "DDNS地址" in item.text:
            ddns_address = item.find('span', class_='badge').text
            break

    if ddns_address:
        print(f"DDNS地址: {ddns_address}")
        return ddns_address
    else:
        print("未找到DDNS地址")
        return "1.1.1.1"
