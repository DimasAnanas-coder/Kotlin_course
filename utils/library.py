from typing import *
import date


class Library:
    __books_list: Dict[str, Any] = dict()  # ISBN, Book
    __history: List[Tuple[int, int, str, int]] = 0  # Day get, Day take, ISBN, user ID

    def __init__(self, author: str, isbn: str, name: str) -> None:
        self.__author: str = author
        self.__isbn: str = isbn
        self.__name: str = name
        self.__is_readable: bool = False

    @classmethod
    def add_new_book(cls, book):
        cls.__books_list[book.__isbn] = book

    def borrow_new_book(self, user) -> None:
        self.__is_readable = True
        user.borrow_new_book(self.__isbn)
        self.__history.append((date.date.get_now_date(), -1, self.__isbn, user.__user_id))

    def return_the_book(self, isbn, user) -> None:
        self.__is_readable = False
        user.return_book(isbn)
        for i in range(len(self.__history) - 1, -1, -1):
            (date_start, _, isbn_now_book, user_id) = self.__history
            if isbn_now_book == isbn:
                self.__history[i] = (date_start, date.date.get_now_date(), isbn_now_book, user_id)
                return

    @classmethod
    def get_book(cls, isbn: str):
        return cls.__books_list[isbn]

    def get_book_info(self):
        return self.__isbn, self.__author, self.__name

    @classmethod
    def get_books_list(cls):
        return cls.__books_list

    @classmethod
    def delete_book(cls, isbn: str) -> None:
        del cls.__books_list[isbn]
