from typing import *
from . import date


class User:
    __users_list: Dict[int, Any] = dict()
    __users_list_visible: Dict[int, Any] = dict()
    __now_select_user: int = 0

    def __init__(self, user_id: int, email: str, name: str) -> None:
        self.__user_id: int = user_id
        self.__email: str = email
        self.__name: str = name
        self.__borrow_books: List[Tuple[str, int]] = []  # ISBN, day start borrow

    @classmethod
    def add_new_user(cls, user):
        cls.__users_list[user.__user_id] = user
        cls.__users_list_visible[user.__user_id] = user
        cls.__now_select_user = user.__user_id

    def borrow_new_book(self, isbn: str) -> None:
        self.__borrow_books.append((isbn, date.date.get_now_date()))

    def return_book(self, isbn: str) -> None:
        for i in range(len(self.__borrow_books) - 1, -1, -1):
            (isbn_now_book, day_start) = self.__borrow_books[i]
            if isbn_now_book == isbn:
                self.__borrow_books.pop(i)
                return

    @classmethod
    def get_user(cls, user_id: int):
        return cls.__users_list[user_id]

    @property
    def id(self) -> int:
        return self.__user_id

    @property
    def email(self) -> str:
        return self.__email

    @property
    def name(self) -> str:
        return self.__name

    @classmethod
    def get_users_list_visible(cls) -> Dict[int, Any]:
        return cls.__users_list_visible

    @classmethod
    def get_all_users_list(cls) -> Dict[int, Any]:
        return cls.__users_list

    def get_borrow_books(self) -> List[Tuple[str, int]]:
        return self.__borrow_books

    @classmethod
    def get_select_user(cls) -> int:
        return cls.__now_select_user

    @classmethod
    def is_email_used(cls, email: str) -> bool:
        users_list = cls.__users_list
        for user_id in users_list:
            if email == users_list[user_id].email:
                return True
        return False

    @classmethod
    def delete_user(cls, user_id: int) -> None:
        del cls.__users_list_visible[user_id]
        if cls.__now_select_user == user_id:
            for select_user_id in cls.__users_list_visible:
                cls.__now_select_user = select_user_id
                break

    @classmethod
    def choose_active_user(cls, user_id) -> None:
        cls.__now_select_user = user_id

    def has_arrears_book(self, user) -> bool:
        for (isbn, start_borrow_day) in self.__borrow_books:
            if date.date.get_now_date() - start_borrow_day > user.max_borrow_days:
                return True
        return False

    def is_limit_of_count_books(self, user) -> bool:
        return len(user.get_borrow_books()) == user.max_count_books


class Student(User):
    @property
    def max_borrow_days(self) -> int:
        return 14

    @property
    def max_count_books(self) -> int:
        return 3


class Guest(User):
    @property
    def max_borrow_days(self) -> int:
        return 7

    @property
    def max_count_books(self) -> int:
        return 1


class Faculty(User):
    @property
    def max_borrow_days(self) -> int:
        return 30

    @property
    def max_count_books(self) -> int:
        return 10
