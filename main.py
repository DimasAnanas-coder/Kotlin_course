from texts import *
from utils.exceptions import *
from utils.users import *
from utils.library import *
from utils.check_conditions import *
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
        1: create_user_step_1_handle,
        2: delete_user_handler,
        3: choose_active_user_handle,
        0: main_menu_handle
    }
    choice_next_step[int(request)]()


def create_user_step_1_handle():
    print(create_user_step_1_text)
    request = input()
    if not request.isdigit() or not 0 <= int(request) <= 3:
        raise UserMenuException(choice_exception_text)
    if request == '0':
        raise UserMenuException(end_action_text)
    choice_user_type = {
        1: Guest,
        2: Student,
        3: Faculty
    }
    user_type = choice_user_type[int(request)]
    create_user_step_2_handle(user_type)


def create_user_step_2_handle(user_type):
    while True:
        print(create_user_step_2_text)
        name = input()
        if name == '0':
            create_user_step_1_handle()
            return
        else:
            break
    create_user_step_3_handle(user_type, name)


def create_user_step_3_handle(user_type, name):
    while True:
        print(create_user_step_3_text)
        email = input().lower()
        if email == '0':
            create_user_step_2_handle(user_type)
            return
        elif ' ' in email:
            print(create_user_step_3_space_exception_text)
        elif is_russian_email(email):
            print(create_user_step_3_russian_exception_text)
        elif '@' not in email:
            print(create_user_step_3_format_exception_text)
        elif User.is_email_used(email):
            print(create_user_step_3_old_account_exception_text)
        else:
            break

    user_id = len(User.get_all_users_list()) + 1
    user = user_type(user_id, email, name)
    User.add_new_user(user)

    print(create_user_step_4_text(user_id))
    user_menu_handle()


def delete_user_handler():
    while True:
        print(delete_user_step_1_text)
        request = input()
        if not request.isdigit():
            print(delete_user_step_1_format_exception_text)
        elif request == '0':
            raise UserMenuException(end_action_text)
        elif int(request) not in User.get_users_list_visible():
            print(delete_user_step_1_no_user_exception_text)
        else:
            break
    User.delete_user(int(request))
    user_menu_handle()


def choose_active_user_handle():
    while True:
        print(choose_user_step_1_text)
        request = input()
        if not request.isdigit():
            print(choose_user_step_1_format_exception_text)
        elif request == '0':
            raise UserMenuException(end_action_text)
        elif int(request) not in User.get_users_list_visible():
            print(choose_user_step_1_no_user_exception_text)
        else:
            break
    User.choose_active_user(int(request))
    user_menu_handle()


def library_menu_handle():
    print(library_menu_text)
    request = input()
    if not request.isdigit() or not 0 <= int(request) <= 4:
        raise LibraryException(choice_exception_text)
    choice_next_step = {
        1: add_book_step_1_handle,
        2: delete_book_handle,
        3: search_book_step_1_handle,
        4: look_all_history,
        0: main_menu_handle
    }
    choice_next_step[int(request)]()


def look_all_history():
    print()
    while True:
        print(end_library_history_text)
        num = input()
        if num != '0':
            print(choice_exception_text)
        else:
            break
    library_menu_handle()


def delete_book_handle():
    while True:
        print(send_isbn_text)
        isbn_search = input()
        if isbn_search == '0':
            raise LibraryException(end_action_text)
        elif not is_isbn(isbn_search):
            print(search_book_by_isbn_exception_text)
        else:
            for isbn in Library.get_books_list():
                if isbn == isbn_search:
                    Library.delete_book(isbn)
                    print(delete_book_end_text)
                    break
            else:
                print(isbn_not_found_text)
            break
    library_menu_handle()


def add_book_step_1_handle():
    while True:
        print(send_isbn_text)
        isbn_search = input()
        if isbn_search == '0':
            raise LibraryException(end_action_text)
        elif not is_isbn(isbn_search):
            print(search_book_by_isbn_exception_text)
        else:
            break
    for isbn in Library.get_books_list():
        if isbn == isbn_search:
            add_book_step_2_isbn_used_handle(isbn_search)
    else:
        add_book_step_2_handle(isbn_search)
        return


def add_book_step_2_handle(isbn):
    print(send_author_text)
    author = input()
    if author == '0':
        add_book_step_1_handle()
        return
    add_book_step_3_handle(isbn, author)


def add_book_step_2_isbn_used_handle(isbn):
    while True:
        print(add_book_step_2_isbn_used_text)
        request = input()
        if not request.isdigit() or not 0 <= int(request) <= 1:
            print(choice_exception_text)
        else:
            break
    request = int(request)
    if request == 1:
        book = Library.get_book(isbn)
        add_book_step_4_handle(isbn, book.author, book.name, is_old=True)
    else:
        library_menu_handle()


def add_book_step_3_handle(isbn, author):
    print(send_name_text)
    name = input()
    if name == '0':
        add_book_step_2_handle(isbn)
        return
    add_book_step_4_handle(isbn, author, name)


def add_book_step_4_handle(isbn, author, name, is_old=False):
    while True:
        print(send_count_text)
        count = input()
        if not count.isdigit():
            print(send_count_exception_text)
        elif count == '0':
            add_book_step_3_handle(isbn, author)
        else:
            break
    if is_old:
        Library.get_book(isbn).add_old_book(int(count))
    else:
        book = Library(author, isbn, name, int(count))
        Library.add_new_book(book)
    print(add_book_end_text)
    library_menu_handle()


def search_book_step_1_handle():
    while True:
        print(start_search_text)
        request = input()
        if not request.isdigit() or not 0 <= int(request) <= 3:
            print(choice_exception_text)
        else:
            break
    choice_text = {
        1: send_isbn_text,
        2: send_name_text,
        3: send_author_text
    }
    if request == '0':
        library_menu_handle()
        return
    request = int(request)
    search_book_step_2_handle(request, choice_text[request])


def search_book_step_2_handle(request, text):
    while True:
        print(text)
        criteria = input()
        if criteria == '0':
            search_book_step_1_handle()
            return
        if request == 1:
            if not is_isbn(criteria):
                print(search_book_by_isbn_exception_text)
            else:
                break
        elif request == 2:
            break
        elif request == 3:
            break
    searched_books: List[Library] = []
    for isbn in Library.get_books_list():
        book = Library.get_book(isbn)
        if book.count == 0:
            continue
        conditions = (
            request == 1 and criteria == isbn,
            request == 2 and criteria.lower() in book.name.lower(),
            request == 3 and criteria.lower() in book.author.lower()
        )
        if any(conditions):
            searched_books.append(book)
    if len(searched_books) == 0:
        print(no_found_books_text)
        search_book_step_1_handle()
        return
    print(found_books_text(searched_books))
    library_menu_handle()


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
        raise BorrowException(user_not_found_in_borrow_text)
    user = User.get_user(choose_user)
    if user.is_limit_of_count_books(user):
        raise BorrowException(limit_count_books_text)
    if user.has_arrears_book(user):
        raise BorrowException(expired_books_text)
    borrow_book_step_1_handle()


def borrow_book_step_1_handle():
    while True:
        print(send_isbn_text)
        isbn_search = input()
        if isbn_search == '0':
            raise BorrowException(end_action_text)
        elif not is_isbn(isbn_search):
            print(search_book_by_isbn_exception_text)
        else:
            break
    searched_books: List[Library] = []
    for isbn in Library.get_books_list():
        book = Library.get_book(isbn)
        if book.count == 0:
            continue
        if isbn == isbn_search:
            searched_books.append(book)
            break
    if len(searched_books) == 0:
        print(no_found_books_text)
        borrow_book_step_1_handle()
        return
    borrow_book_step_2_handle(searched_books[0])


def borrow_book_step_2_handle(book):
    while True:
        print(found_borrow_book_text(book))
        num = input()
        if not num.isdigit() or not 0 <= int(num) <= 1:
            print(choice_exception_text)
        else:
            break
    if num != '0':
        user = User.get_user(User.get_select_user())
        book.borrow_new_book(user)
        print(borrow_book_end_text)
    operation_with_books_menu_handle()


def return_book_handle():
    if User.get_select_user() == 0:
        raise BorrowException(user_not_found_in_return_text)

    user = User.get_user(User.get_select_user())
    borrow_books = user.get_borrow_books()
    while True:
        print(return_book_step_1_text())
        num = input()
        if not num.isdigit() or not 0 <= int(num) <= len(borrow_books):
            print(choice_exception_text)
        else:
            break
    if num != '0':
        isbn = borrow_books[int(num) - 1][0]
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
    while True:
        print(before_exit_text)
        request = input()
        if request == '0':
            raise ExitException()
        elif request == '1':
            main_menu_handle()
        else:
            print(choice_exception_text)


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
