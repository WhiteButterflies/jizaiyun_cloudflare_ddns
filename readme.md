# 基于cf-ddns的鸡仔云ipv4动态更新脚本

1、cf-ddns.conf

修改domains.host.name为你的动态DDNS二级域名，如域名全长为ddns.example.com，则填写ddns

修改domains.name，为example.com

修改user.api_key为你的cloudflare global API token的值

修改user.email为你注册cf的邮箱

其余的可以空白，在第一次成功执行脚本后会自动更新。

2、login.py
12行的地址可以改成售后群最新的地址，无cf盾。
22行的payload中修改你在鸡仔云的用户名和密码

在39行中，protected_url修改为你购买的鸡仔云产品的具体页面（需要预先登录）

3、本脚本仅对ipv4 DDNS做了设置，ipv6和如何定期循环执行请自行修改代码。

4、python3.11，requirements.txt，运行cf-ddns.py即可。
