
import hmac
import hashlib
import base64
import json
import tornado

from tornado.options import define, options
define('port', default=8000, help='default port',type=int)

class Robot(tornado.web.RequestHandler):

    async def post(self):


        timestamp = self.request.headers.get('timestamp', None)

        sign = self.request.headers.get('sign', None)
        app_secret = '钉钉机器人秘钥'
        app_secret_enc = app_secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, app_secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(app_secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        my_sign = base64.b64encode(hmac_code).decode('utf-8')
        if sign != my_sign:
            return self.finish({"errcode":1,"msg":"签名有误"})
        data = json.loads(self.request.body)
        text = data['text']["content"]
        atUsers = data.get("atUsers",None)
        uid = data.get("senderStaffId",None)
        return self.finish({"errcode":0,"msg":text})

urlpatterns = [
    (r"/robot_chat/",Robot),
]


# 创建Tornado实例
application = tornado.web.Application(urlpatterns,debug=True)




if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()