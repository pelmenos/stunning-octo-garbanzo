import datetime


def get_user_input():
    pass


def show_info():
    pass


def processed_result(result):
    pass


def save_result(result):
    with open("history.txt", mode='a', encoding='utf-8') as f:
        f.write(f"{datetime.datetime.now()}:{result}")


if __name__ == '__main__':
    show_info()
    result = get_user_input()
    processed_result(result)
    save_result(result)