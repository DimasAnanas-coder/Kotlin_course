import date
import users

def start_text():
    return f'''Today: {date.date.get_now_date()} day!
Choice (1-4):

1. User management
2. Library management
3. Take/get book
4. Jump to the next day'''


user_not_found_text = 'You can`t take a book from the library, because you didn`t create a user'

def users_text():
    users_list = users.users
    return '''
    
    
'''