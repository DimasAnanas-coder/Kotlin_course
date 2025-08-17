from texts import *
from utils.exceptions import *
from utils.users import *
from utils.library import *
from typing import *


def main_menu_handle():
    print(main_menu_text())
    request = input()
    if not request.isdigit() or not 0 <= int(request) <= 4:
        raise MainMenuException(choice_exception_text)
    choice_next_step = {
        1: user_menu_handle,
        2: library_menu_handle,
        3: operation_with_books_menu_handle,
        4: jump_to_the_next_day_handle,
        0: exit_handle
    }
    choice_next_step[int(request)]()


def user_menu_handle():
    print(user_menu_text())
    request = input()
    if not request.isdigit() or not 0 <= int(request) <= 3:
        raise UserMenuException(choice_exception_text)
    choice_next_step = {
        1: create_user_handle,
        2: delete_user_handler,
        3: choose_active_user_handle,
        0: main_menu_handle
    }
    choice_next_step[int(request)]()


def create_user_handle():
    print(create_user_step_1_text)
    request = input()
    if not request.isdigit() or not 1 <= int(request) <= 3:
        raise UserMenuException(choice_exception_text)
    choice_user_type = {
        1: Guest,
        2: Student,
        3: Faculty
    }
    user_type = choice_user_type[int(request)]

    while True:
        print(create_user_step_2_text)
        name = input()
        if ' ' in name:
            print(create_user_step_2_format_exception_text)
        else:
            break

    while True:
        print(create_user_step_3_text)
        email = input()
        if ' ' in email:
            print(create_user_step_3_space_exception_text)
        elif '@' not in email:
            print(create_user_step_3_format_exception_text)
        elif User.is_email_used(email):
            print(create_user_step_3_old_account_exception_text)
        else:
            break

    user_id = len(User.get_users_list()) + 1
    user = user_type(user_id, email, name)
    User.add_new_user(user)

    print(create_user_step_4_text(user_id))
    user_menu_handle()


def delete_user_handler():
    while True:
        print(delete_user_step_1_text)
        request = input()
        if not request.isdigit() or int(request) < 1:
            print(delete_user_step_1_format_exception_text)
        elif int(request) > len(User.get_users_list()):
            print(delete_user_step_1_no_user_exception_text)
        else:
            break
    User.delete_user(int(request))
    user_menu_handle()


def choose_active_user_handle():
    while True:
        print(choose_user_step_1_text)
        request = input()
        if not request.isdigit() or int(request) < 1:
            print(choose_user_step_1_format_exception_text)
        elif int(request) > len(User.get_users_list()):
            print(choose_user_step_1_no_user_exception_text)
        else:
            break
    User.choose_active_user(int(request))
    user_menu_handle()


def library_menu_handle():
    pass


def operation_with_books_menu_handle():
    print(operation_with_books_menu_text)
    request = input()
    if not request.isdigit() or not 0 <= int(request) <= 3:
        raise BorrowException(choice_exception_text)
    choice_next_step = {
        1: start_borrow_book_handle,
        2: return_book_handle,
        3: look_library_history_handle,
        0: main_menu_handle
    }
    choice_next_step[int(request)]()


def start_borrow_book_handle():
    choose_user = User.get_select_user()
    if choose_user == 0:
        raise BorrowException(user_not_found_text)
    user = User.get_user(choose_user)
    if user.is_limit_of_count_books(user):
        raise BorrowException(limit_count_books_text)
    if user.has_arrears_book(user):
        raise BorrowException(expired_books_text)
    borrow_book_step_1_handle()


def borrow_book_step_1_handle():
    print(start_borrow_text)
    request = input()
    if not request.isdigit() or not 0 <= int(request) <= 3:
        raise BorrowException(choice_exception_text)
    choice_text = {
        1: send_isbn_text,
        2: send_name_text,
        3: send_author_text
    }
    request = int(request)
    if request == 0:
        operation_with_books_menu_handle()
        return
    borrow_book_step_2_handle(request, choice_text[request])


def borrow_book_step_2_handle(request, text):
    while True:
        print(text)
        criteria = input()
        if request == 1:
            if not (len(criteria) == 17 and '--' not in criteria
                    and criteria[0] != '-' and criteria[-1] != '-'):
                print(borrow_book_by_ibsn_exception_text)
            else:
                break
        elif request == 2:
            break
        elif request == 3:
            break
    searched_books: List[Library] = []
    book: Library
    for (isbn, book) in Library.get_books_list():
        _, author, name, is_readable = book.get_book_info()
        if not is_readable:
            continue
        conditions = (
            request == 1 and isbn == criteria,
            request == 2 and name == criteria,
            request == 3 and author == criteria
        )
        if any(conditions):
            searched_books.append(book)
    if len(searched_books) == 0:
        print(no_found_books_text)
        borrow_book_step_1_handle()
        return
    borrow_book_step_3_handle(searched_books)


def borrow_book_step_3_handle(searched_books):
    while True:
        print(found_books_text(searched_books))
        num = input()
        if not num.isdigit() or not 0 <= int(num) <= len(searched_books):
            print(choice_exception_text)
        else:
            break
    num = int(num)
    if num != 0:
        user = User.get_user(User.get_select_user())
        searched_books[num - 1].borrow_new_book(user)
        print(borrow_book_end_text)
    operation_with_books_menu_handle()


def return_book_handle():
    user = User.get_user(User.get_select_user())
    borrow_books = user.get_borrow_books()
    while True:
        print(return_book_step_1_text())
        num = input()
        if not num.isdigit() or not 0 <= int(num) <= len(borrow_books):
            print(choice_exception_text)
        else:
            break
    num = int(num)
    if num != 0:
        isbn = borrow_books[-1][0]
        book = Library.get_book(isbn)
        Library.return_the_book(book, user)
        print(return_book_end_text)
    operation_with_books_menu_handle()


def look_library_history_handle():
    print(library_history_text())
    while True:
        print(end_library_history_text)
        num = input()
        if num != '0':
            print(choice_exception_text)
        else:
            break
    operation_with_books_menu_handle()


def jump_to_the_next_day_handle():
    date.date.jump_to_next_day()
    main_menu_handle()


def exit_handle():
    raise ExitException('Buy')


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
