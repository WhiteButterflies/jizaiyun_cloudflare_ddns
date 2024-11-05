# 基于cf-ddns的鸡仔云ipv4动态更新脚本
0、原理

使用鸡仔云官方API获取动态公网IP地址，然后使用现有的CF DDNS脚本。注意，当前黄鸡官方尚未完成API的部署。

1、cf-ddns.conf

修改domains.host.name为你的动态DDNS二级域名，如域名全长为ddns.example.com，则填写ddns

修改domains.name，为example.com

修改user.api_key为你的cloudflare global API token的值

修改user.email为你注册cf的邮箱

其余的可以空白，在第一次成功执行脚本后会自动更新。

2、login.py

7-11行按照鸡仔云产品页面的的API接口补充。

3、本脚本仅对ipv4 DDNS做了设置，ipv6和如何定期循环执行请自行修改代码。

4、python3.11，requirements.txt，运行cf-ddns.py即可。
