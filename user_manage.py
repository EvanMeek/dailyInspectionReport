from user import *
import json
import os
import requests
import utils


class user_manage:
    def __init__(self):
        self.users = []
        utils.create_cache_file()
        self.reload_user()

    def create_user(self, token):
        if not self.user_exists_p(token):
            self.users.append(token)
            with open("users.json", "w") as f:
                json.dump(self.users, f)
        else:
            print("{} 用户已存在无需重新添加!".format(token))

    def delete_user(self, token):
        self.users.remove(token)
        with open("users.json", "w") as f:
            json.dump(self.users, f)
        self.reload_user()
        print("{} 用户已被删除.".format(token))

    def reload_user(self):
        with open("users.json", "r") as f:
            if os.path.getsize("users.json") != 0:
                self.users = json.load(f)

    def user_exists_p(self, token):
        if not (self.users == []):
            for i, u in enumerate(self.users):
                if self.users[i] == token:
                    return True
                else:
                    return False
        else:
            return False

    def iter_users_info(self):
        self.reload_user()
        for i, u in enumerate(self.users):
            print(self.users[i])

    def find_user_info(self, token):
        self.reload_user()
        return self.users[self.users.index(token)]

    def sign_in(self, token):
        "为单个用户进行签到"
        u = user(token)
        response = requests.post(
            "https://student.wozaixiaoyuan.com/heat/save.json",
            headers=u.headers,
            data=u.data,
        ).json()
        status_code = response["code"]
        # 如果状态码为未登录(失效token)状态，则删除此用户
        if not status_code:
            print(
                u.headers["token"]
                + "{:=>10}".format("打卡成功")
                + "\tcode:{}".format(status_code)
            )
        else:
            print(
                u.headers["token"]
                + "{:=>10}\n错误信息: {}".format("打卡失败", response["message"])
                + "\nSTATUS_CODE: {}".format(status_code)
            )
            if status_code == -10:
                self.delete_user(token)

    def sign_all(self):
        "为所有用户进行签到"
        for token in self.users:
            self.sign_in(token)
