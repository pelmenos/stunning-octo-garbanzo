def get_user_input():
    pass


def show_info():
    pass


def processed_result(result):
    match result:
        case "Пока":
            print("До свидания!")
        case "Привет":
            print("Здравствуйте!")
    return


def save_result(result):
    pass


if __name__ == '__main__':
    show_info()
    result = get_user_input()
    processed_result(result)
    save_result(result)