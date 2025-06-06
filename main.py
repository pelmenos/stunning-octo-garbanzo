choices = ['Привет', 'Пока']


def get_user_input():
    while True:
            res = input()
            if res not in choices:
                print("Неправильный ввод")
            return res


def show_info():
    pass


def processed_result(result):
    pass


def save_result(result):
    pass


if __name__ == '__main__':
    show_info()
    result = get_user_input()
    processed_result(result)
    save_result(result)