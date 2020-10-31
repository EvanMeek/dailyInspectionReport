import utils


class user:
    headers = {
        "Host": "student.wozaixiaoyuan.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "Referer": "https://servicewechat.com/wxce6d08f781975d91/147/page-frame.html",
        "token": None,
        "Content-Length": "360",
    }
    data = {
        "answers": '["0"]',
        "seq": utils.get_seq(),
        "temperature": utils.get_random_temprature(),
        "latitude": "23.0922820000",
        "longitude": "113.3541850000",
        "country": "中国",
        "city": "广州市",
        "district": "海珠区",
        "province": "广东省",
        "township": "江海街道",
        "street": "上冲中约新街一巷",
    }

    def __init__(self, token):
        if not (token is None or "".__eq__(token)):
            self.headers["token"] = token
        else:
            print("token为空，无法签到!")
