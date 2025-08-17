from typing import *
import date


class Library:
    __books_list: Dict[str, Any] = dict()  # ISBN, Book
    __history: List[Tuple[int, int, str, int]] = 0  # Day get, Day take, ISBN, user ID

    def __init__(self, author: str, isbn: str, name: str, count: int) -> None:
        self.__author: str = author
        self.__isbn: str = isbn
        self.__name: str = name
        self.__count: int = count

    @classmethod
    def add_new_book(cls, book):
        cls.__books_list[book.__isbn] = book

    def add_old_book(self, count) -> None:
        self.__count += count

    def borrow_new_book(self, user) -> None:
        self.__count -= 1
        user.borrow_new_book(self.__isbn)
        self.__history.append((date.date.get_now_date(), -1, self.__isbn, user.id))

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def count(self) -> int:
        return self.__count

    @classmethod
    def return_the_book(cls, book, user) -> None:
        book.add_count(1)
        user.return_book(book.isbn)
        for i in range(len(cls.__history) - 1, -1, -1):
            (date_start, _, isbn_now_book, user_id) = cls.__history
            if isbn_now_book == book.isbn:
                cls.__history[i] = (date_start, date.date.get_now_date(), isbn_now_book, user_id)
                return

    @classmethod
    def get_book(cls, isbn: str):
        return cls.__books_list[isbn]

    def get_book_info(self) -> Tuple[str, str, str, int]:
        return self.__isbn, self.__author, self.__name, self.__count

    @classmethod
    def get_books_list(cls) -> Dict[str, Any]:
        return cls.__books_list

    @classmethod
    def delete_book(cls, isbn: str) -> None:
        del cls.__books_list[isbn]

    @classmethod
    def get_history(cls) -> List[Tuple[int, int, str, int]]:
        return cls.__history
