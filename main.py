# import user
from user import *
from user_manage import *


def main():
    um = user_manage()
    um.create_user("97e83b58-f145-406f-98e5-1f64b0e829c4")
    um.create_user("9")
    um.create_user("8")
    um.create_user("7")
    um.create_user("6")
    # um.iter_users_info()
    # um.user_info("测试1")
    # print(um.user_exists_p("测试1"))
    # um.create_user("测试1")
    # um.create_user("测试1")
    # um.iter_users_info()
    # um.reload_user()
    # print(um.find_user_info("97e83b58-f145-406f-98e5-1f64b0e829c4"))
    # um.create_user("97e83b58-f145-406f-98e5-1f64b0e829c4A")
    # um.sign_in("97e83b58-f145-406f-98e5-1f64b0e829c4")
    um.sign_all()
    # test()


def test():
    with open("users.json", "r") as f:
        print(f.read() == "")


if __name__ == "__main__":
    main()
