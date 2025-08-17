def is_isbn(isbn: str):
    return (len(isbn) == 17 and '--' not in isbn
            and isbn[0] != '-' and isbn[-1] != '-')
