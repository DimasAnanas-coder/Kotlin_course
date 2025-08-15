from typing import *
import date


class User:
    users_list: Dict[int, Any] = dict()

    def __init__(self, user_id: int, email: str, name: str) -> None:
        self.__user_id: int = user_id
        self.__email: str = email
        self.__name: str = name
        self.__start_borrow_day: int = date.date.get_now_date()
        self.__borrow_books: List[int] = []

    def get_start_borrow_day(self) -> int:
        return self.__start_borrow_day

    def get_user(self, user_id: int):
        return User.__users_list[user_id]

    def get_user_info(self):
        return self.__user_id, self.__email, self.__name

    def get_users_list(self):
        return users_list
class Student(User):
    @staticmethod
    def get_max_borrow_days(self) -> int:
        return 14
    @staticmethod
    def get_max_count_books(self) -> int:
        return 3
