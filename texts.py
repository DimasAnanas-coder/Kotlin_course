import date
from users import *


def main_menu_text():
    return f'''Today: {date.date.get_now_date()} day!
    
Choice (0-4):
1. User management
2. Library management
3. Take/get book
4. Jump to the next day
0. Exit'''


user_not_found_text = 'You can`t take a book from the library, because you didn`t create a user'

choice_exception_text = 'You need choice the one action. Only one digit, please'


def user_menu_text():
    users_list = User.get_users_list()
    text = 'List of users\n\n'
    num = 1
    select_user_id = User.get_select_user()
    for user_id in users_list:
        if isinstance(users_list[user_id], Student):
            user_type = 'student'
        elif isinstance(users_list[user_id], Faculty):
            user_type = 'faculty'
        else:
            user_type = 'guest'
        user_short_info = f'ID: {user_id} - {user_type}'
        if user_id == select_user_id:
            user_short_info = f'<{user_short_info}>'
        text += f'{user_short_info}\n'
        num += 1
    if num == 1:
        text = 'List of user is empty. Create a new user!\n'
    text += '''\nChoice (0-3):
1. Create a new user
2. Delete a user
3. Choose an active user
0. Back to main menu'''

    return text


create_user_step_1_text = '''Choice (1-3):
1. Guest
2. Student
3. Faculty'''

create_user_step_2_text = 'Enter your name'

create_user_step_2_format_exception_text = 'Your name must consist of one word'

create_user_step_3_text = 'Enter your email'

create_user_step_3_format_exception_text = 'Email need to have the symbol "@"'

create_user_step_3_old_account_exception_text = 'An account with this email has already been created'


def create_user_step_4_text(user_id):
    return f'You have successful created a new account (ID: {user_id})'
