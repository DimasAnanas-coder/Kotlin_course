def is_isbn(isbn: str) -> bool:
    conditions = (
        len(isbn) == 17,
        '--' not in isbn,
        isbn[0] != '-',
        isbn[-1] != '-',
        isbn.count('-') == 4,
        isbn.replace('-', '').isdigit()
    )
    return all(conditions)


def is_russian_email(email: str) -> bool:
    for symbol in email:
        if symbol in 'абвгдеёжздийклмнопрстуфхцчшщъыьэюя':
            return True
    return False


def is_email_format(email: str) -> bool:
    if email.count('@') != 1:
        return False
    email_domain = email[email.find('@'):]
    conditions = (
        '..' not in email_domain,
        '@.' not in email,
        email[-1] != '.',
        '.' in email_domain
    )
    return all(conditions)
