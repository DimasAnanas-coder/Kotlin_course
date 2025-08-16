from typing import *
import date


# users_list: Dict[int, Any] = dict()


class User:
    __users_list: Dict[int, Any] = dict()
    __now_select_user: int = -1

    def __init__(self, user_id: int, email: str, name: str) -> None:
        self.__user_id: int = user_id
        self.__email: str = email
        self.__name: str = name
        self.__borrow_books: List[Tuple[str, int]] = []

    @classmethod
    def add_new_user(cls, user):
        cls.__users_list[user.__user_id] = user
        cls.__now_select_user = user.__user_id

    def borrow_new_book(self, isbn: str) -> None:
        self.__borrow_books.append((isbn, date.date.get_now_date()))

    @classmethod
    def get_user(cls, user_id: int):
        return cls.__users_list[user_id]

    def get_user_info(self):
        return self.__user_id, self.__email, self.__name

    @classmethod
    def get_users_list(cls):
        return cls.__users_list

    def get_borrow_books(self):
        return self.__borrow_books

    @classmethod
    def get_select_user(cls):
        return cls.__now_select_user

    @classmethod
    def is_email_used(cls, email):
        users_list = cls.__users_list
        for user_id in users_list:
            if email == users_list[user_id].get_user_info()[1]:
                return True
        return False


class Student(User):
    @staticmethod
    def get_max_borrow_days(self) -> int:
        return 14

    @staticmethod
    def get_max_count_books(self) -> int:
        return 3


class Guest(User):
    @staticmethod
    def get_max_borrow_days(self) -> int:
        return 7

    @staticmethod
    def get_max_count_books(self) -> int:
        return 1


class Faculty(User):
    @staticmethod
    def get_max_borrow_days(self) -> int:
        return 30

    @staticmethod
    def get_max_count_books(self) -> int:
        return 10
