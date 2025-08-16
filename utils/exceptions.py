class ApplicationException(Exception):
    pass


class MainMenuException(ApplicationException):
    pass


class UserMenuException(ApplicationException):
    pass


class LibraryException(ApplicationException):
    pass


class BorrowException(ApplicationException):
    pass


class ExitException(ApplicationException):
    pass