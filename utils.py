import random
import time
import os


user_cache_file = "users.json"


def get_random_temprature():
    "随机温度36.2-36.7"
    random.seed(time.ctime())
    return "{:.1f}".format(random.uniform(36.2, 36.7))


def get_seq():
    "获取当前时间，返回打卡时间类型"
    current_hour = time.localtime(time.time()).tm_hour
    if 0 < current_hour < 8:
        return "1"
    elif 11 < current_hour < 15:
        return "2"
    else:
        return "3"


def create_cache_file():
    "创建缓存文件"
    if not user_cache_file_exists_p():
        with open(user_cache_file, "w") as f:
            f.write("")
            f.close


def user_cache_file_exists_p() -> bool:
    "判断users.json是否存在"
    if os.path.exists(user_cache_file):
        return True
    else:
        return False
