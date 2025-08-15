from texts import *
from exceptions import *
import date

def main_menu_handle():
    print(start_text)
    request = input()
    if not request.isdigit() or not 1 <= int(request) <= 4:
        raise MainMenuExceptions(user_not_found_text)
    choice_next_step = {
        1: user_menu_handle,
        2: library_menu_handle,
        3: operation_with_books_menu_handle,
        4: jump_to_the_next_day_handle
    }
    choice_next_step[int(request) - 1]()


def user_menu_handle():
    print(start_text)
    request = input()


def library_menu_handle():
    pass


def operation_with_books_menu_handle():
    pass


def jump_to_the_next_day_handle():
    date.date.jump_to_next_day()
    main_menu_handle()


def start(func=main_menu_handle):
    while True:
        try:
            func()
        except MainMenuExceptions as e:
            print(e)
            start()
        except


if __name__ == '__main__':
    start()
