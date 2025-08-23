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
    users_list = User.get_users_list_visible()
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
        select_user: User = User.get_user(select_user_id)
        text = f'''Activity user: 
ID: {select_user_id}
{select_user.name} - {user_type_selected}
email: {select_user.email}
Max borrow days: {select_user.max_borrow_days}
Max count books: {select_user.max_count_books}\n\n''' + text

    text += '''\nChoice (0-3):
1. Create a new user
2. Delete a user
3. Choose an active user
0. Back to main menu'''
    text = '###### User Management ######\n' + text

    return text


create_user_step_1_text = '''Choice (0-3):
1. Guest
2. Student
3. Faculty
0. Back to User Management'''

create_user_step_2_text = 'Enter your name. Send "0" to go back'

create_user_step_2_format_exception_text = 'Your name must consist of one word'

create_user_step_3_text = 'Enter your email. Send "0" to go back'

create_user_step_3_space_exception_text = 'Your email must consist of one word'

create_user_step_3_russian_exception_text = 'Your email can`t consist of russian characters'

create_user_step_3_format_exception_text = 'Email format is invalid'

create_user_step_3_old_account_exception_text = 'An account with this email has already been created'


def create_user_step_4_text(user_id):
    return f'You have successful created a new account (ID: {user_id})\n'


delete_user_step_1_text = 'Enter the user ID you want to delete. Send "0" to go back'

delete_user_step_1_no_user_exception_text = 'A user with this ID was not found'

delete_user_step_1_format_exception_text = 'The user ID must be a natural number'

choose_user_step_1_text = 'Enter the user ID you want to choose. Send "0" to go back'

choose_user_step_1_no_user_exception_text = 'A user with this ID was not found'

choose_user_step_1_format_exception_text = 'The user ID must be a natural number'

user_not_found_in_borrow_text = 'You can`t borrow a book from the library, because you didn`t create a user'

user_not_found_in_return_text = 'You can`t return a book from the library, because you didn`t create a user'

user_not_found_in_select_user_text = 'You can`t select a user, because you didn`t create a user'

book_not_found_in_delete_text = 'You can`t delete a book, because you didn`t create a book'

limit_count_books_text = 'You can`t borrow a book from the library, because you have many books'

expired_books_text = 'You can`t borrow a book from the library, because you have expired book'

start_search_text = '''Select the books search criteria

Choice (0-3):
1. ISBN
2. Name
3. Author
0. Back to books management menu'''

send_isbn_text = 'Send the book`s ISBN in format: 978-3-16-148412-0 (13 digits). Send "0" to go back'

send_name_text = 'Send the book`s name. Send "0" to go back'

send_author_text = 'Send the book`s author. Send "0" to go back'

search_book_by_isbn_exception_text = 'ISBN format is invalid'

no_found_books_text = 'Books were not found'


def found_books_text(books_list: List[Library]):
    text = 'Books list were found your search:\n'
    for book in books_list:
        text += f'ISBN: {book.isbn}; {book.author} - {book.name}; count: {book.count} \n'
    return text


def found_borrow_book_text(book: Library):
    text = f'''{book.author} - {book.name}. Count in library: {book.count}

Choice (0-1):
1. Borrow a book
0. Back to Book management'''
    return text


borrow_book_end_text = 'You have successful borrow the book\n'

borrow_book_already_text = 'You have this book already. Please, choose another book\n'

operation_with_books_menu_text = '''###### Books management ######

Choice (0-3):
1. Borrow a book
2. Look my books -> Return a book
3. Look library history
0. Back to main menu'''


def return_book_step_1_text():
    user = User.get_user(User.get_select_user())
    books_info = user.get_borrow_books()
    if len(books_info) == 0:
        return 'You haven`t books. Send "0" to go back'
    text = 'List of your books:\n'
    for i, (isbn, day) in enumerate(books_info):
        text += f'{i + 1}. ISBN: {isbn} - day {day}\n'

    text += '\nChoose a book and send a book number from this list or send "0", if you don`t want return a book'
    return text


return_book_end_text = 'You have successful return the book\n'


def library_history_text():
    text = '''Library history: \n\nBorrow day | Return day |       ISBN       | user ID\n'''
    history = Library.get_history()
    if len(history) == 0:
        return 'Library history is empty'
    for (borrow_day, return_day, isbn, user_id) in history:
        if return_day == -1:
            return_day = '-'
        text += f'{borrow_day}{" " * 16}{return_day}{" " * 8}{isbn}{" " * 3}{user_id}\n'
    return text


def look_all_books_text():
    text = '''Books: \n\n      ISBN       | Author | name | count\n'''
    books = Library.get_books_list()
    if len(books) == 0:
        return 'Library is empty'
    for isbn in books:
        book = books[isbn]
        text += f'{isbn} {book.author} {book.name} {book.count}\n'
    return text


end_library_history_text = 'Send "0" to go back'

library_menu_text = '''###### Library ######

Choice (0-4):
1. Add Book
2. Delete Book
3. Search
4. Look all books
0. Back to main menu'''

add_book_step_2_isbn_used_text = '''ISBN was used already. You can add copy this book

Choice (0-1):
1. Add copy
0. Back to library'''

send_count_text = 'Send a books count. Send "0" to go back'

send_count_exception_text = 'Count must be a natural number'

add_book_end_text = 'You have successfully added books to the library\n'

isbn_not_found_text = 'This ISBN was not used'

delete_book_end_text = 'You have successfully delete books from the library\n'

end_action_text = 'You have ended the action\n'

before_exit_text = '''Do you want to exit this program?

Choice (0-1):
1. Back to main menu
0. Exit'''

exit_text = 'Buy'
