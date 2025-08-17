from utils.users import *
from utils.library import *


def main_menu_text():
    return f'''Today: {date.date.get_now_date()} day!
    
Choice (0-4):
1. User management
2. Library
3. Borrow/return book
4. Jump to the next day
0. Exit'''


choice_exception_text = 'You need choice the one action. Only one number, please'


def user_menu_text():
    users_list = User.get_users_list()
    text = 'List of users:\n'
    num = 1
    select_user_id = User.get_select_user()
    user_type_selected = 'goat'
    for user_id in users_list:
        if isinstance(users_list[user_id], Student):
            user_type = 'student'
        elif isinstance(users_list[user_id], Faculty):
            user_type = 'faculty'
        else:
            user_type = 'guest'

        if user_id == select_user_id:
            user_type_selected = user_type
        user_short_info = f'ID: {user_id} - {user_type}'
        text += f'{user_short_info}\n'
        num += 1

    if num == 1:
        text = 'List of user is empty. Create a new user!\n'
    else:
        _, email, name = User.get_user(select_user_id).get_user_info()
        text = f'''Activity user: {name} - {user_type_selected}
email: {email}
ID: {select_user_id}\n\n''' + text

    text += '''\nChoice (0-3):
1. Create a new user
2. Delete a user
3. Choose an active user
0. Back to main menu'''
    text = '###### User Management ######\n' + text

    return text


create_user_step_1_text = '''Choice (1-3):
1. Guest
2. Student
3. Faculty'''

create_user_step_2_text = 'Enter your name'

create_user_step_2_format_exception_text = 'Your name must consist of one word'

create_user_step_3_text = 'Enter your email'

create_user_step_3_space_exception_text = 'Your email must consist of one word'

create_user_step_3_format_exception_text = 'Email need to have the symbol "@"'

create_user_step_3_old_account_exception_text = 'An account with this email has already been created'


def create_user_step_4_text(user_id):
    return f'You have successful created a new account (ID: {user_id})'


delete_user_step_1_text = 'Enter the user ID you want to delete'

delete_user_step_1_no_user_exception_text = 'A user with this ID was not found'

delete_user_step_1_format_exception_text = 'The user ID must be a natural number'

choose_user_step_1_text = 'Enter the user ID you want to delete'

choose_user_step_1_no_user_exception_text = 'A user with this ID was not found'

choose_user_step_1_format_exception_text = 'The user ID must be a natural number'

user_not_found_text = 'You can`t borrow a book from the library, because you didn`t create a user'

limit_count_books_text = 'You can`t borrow a book from the library, because you have many books'

expired_books_text = 'You can`t borrow a book from the library, because you have expired book'

start_search_text = '''Select the books search criteria

Choice (0-3):
1. ISBN
2. Name
3. Author
0. Back to books management menu'''

send_isbn_text = 'Send the book`s ISBN in format: 978-3-16-148412-0 (13 digits)'

send_name_text = 'Send the book`s name'

send_author_text = 'Send the book`s author'

search_book_by_isbn_exception_text = 'IBSN format is invalid'

no_found_books_text = 'Books were not found'


def found_books_text(books_list: List[Library]):
    text = 'Books list were found your search:\n'
    for book in books_list:
        isbn, author, name, count = book.get_book_info()
        text += f'ISBN: {isbn}; {author} - {name}; count: {count} \n'
    return text


def found_borrow_book_text(book: Library):
    isbn, author, name, _ = book.get_book_info()
    text = f'''{author} - {name}. ISBN: {isbn}

Choice (0-1):
1. Borrow a book
0. Back to Book management'''
    return text


borrow_book_end_text = 'You have successful borrow the book'

operation_with_books_menu_text = '''###### Books management ######

Choice (0-3):
1. Borrow a book
2. Return a book
3. Look library history
0. Back to main menu'''


def return_book_step_1_text():
    user = User.get_user(User.get_users_list())
    books_info = user.get_borrow_books()
    if len(books_info) == 0:
        return 'You haven`t books. Send "0" to go back'
    text = 'List of your books:\n'
    for i, (isbn, day) in enumerate(books_info):
        text += f'{i + 1}. ISBN: {isbn} - day {day}\n'

    text += '\nChoose a book and send a book number from this list or send "0", if you don`t want return a book'
    return text


return_book_end_text = 'You have successful return the book'


def library_history_text():
    text = '''Library history: \n\nBorrow day | Return day | isbn | user ID\n'''
    history = Library.get_history()
    if len(history) == 0:
        return 'Library history is empty'
    for (borrow_day, return_day, isbn, user_id) in history:
        if return_day == -1:
            return_day = '-'
        text += f'{borrow_day}\t{return_day}\t{isbn}\t{user_id}\n'
    text += '\n'
    return text


end_library_history_text = 'Send "0" to go back'

library_menu_text = '''###### Library ######

Choice (0-3):
1. Add Book
2. Delete Book
3. Search
0. Back to main menu'''

add_book_step_2_isbn_used_text = '''ISBN was used already. You can add copy this book

Choice (0-1):
1. Add copy
0. Back to library'''

send_count_text = 'Send a books count'

send_count_exception_text = 'Count must be a natural number'

add_book_end_text = 'You have successfully added books to the library'

isbn_not_found_text = 'This ISBN was not used'

delete_book_end_text = 'You have successfully delete books from the library'