from handlers import *


def start(func):
    try:
        func()
    except MainMenuException as e:
        print(e)
        start(func=main_menu_handle)
    except UserMenuException as e:
        print(e)
        start(func=user_menu_handle)
    except LibraryException as e:
        print(e)
        start(func=library_menu_handle)
    except BorrowException as e:
        print(e)
        start(func=operation_with_books_menu_handle)
    except ExitException as e:
        print(e)


if __name__ == '__main__':
    start(func=main_menu_handle)
