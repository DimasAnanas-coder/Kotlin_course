def is_isbn(isbn: str):
    return (
            len(isbn) == 17 and '--' not in isbn
            and isbn[0] != '-' and isbn[-1] != '-' and isbn.count('-') == 4
            and isbn.replace('-', '').isdigit()
    )


def is_russian_email(email: str):
    for symbol in email:
        if symbol in 'абвгдеёжздийклмнопрстуфхцчшщъыьэюя':
            return True
    return False
