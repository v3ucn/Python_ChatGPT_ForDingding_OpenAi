# Python_ChatGPT_ForDingding_OpenAi

## 基于 https://github.com/rawandahmad698/PyChatGPT

## 启动server端接受C端的钉钉机器人返回的信息

```
python3 server.py
```

## 使用Dingding实例向C端发送信息

```
dingding = DingDing("appkey","appSecret")

chat = Chat(email="OpenAi邮箱", password="OpenAi密码",proxies="代理地址")

answer = chat.ask("你好")

# 单聊
#dingding.send_message('uid',answer)

# 群聊
#dingding.send_user('uid',answer)

print(answer)
```
