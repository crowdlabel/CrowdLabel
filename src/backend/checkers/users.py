import re
from email_validator import validate_email

from schemas.users import USER_TYPES


from models.user import MAX_USERNAME_LENGTH


MIN_USERNAME_LENGTH = 3
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 64

USERNAME_CHARS = r'A-Za-z0-9_\.\_' # alphanumeric + dash, underscore, and period
PASSWORD_CHARS = r'\x20-\x7e'# printable chars excluding delete
USERNAME_PATTERN = fr'[{USERNAME_CHARS}]{{{MIN_USERNAME_LENGTH},{MAX_USERNAME_LENGTH}}}'
PASSWORD_PATTERN = fr'[{PASSWORD_CHARS}]{{{MIN_USERNAME_LENGTH},{MAX_USERNAME_LENGTH}}}'


   
def check_username_format(username: str) -> bool:
     
    is_valid = re.fullmatch(USERNAME_PATTERN, username)
    return bool(is_valid)

def check_password_format(password: str) -> bool:
    
    is_valid = re.fullmatch(PASSWORD_PATTERN, password)
    return bool(is_valid)


def check_email_format(email: str) -> bool:
    try:
        is_valid = validate_email(
            email=email,
            check_deliverability=False,
        )
        return bool(is_valid)
    except:
        return False

def check_user_type_format(user_type: str) -> bool:
    return user_type in USER_TYPES

def check_verification_code_format(verification_code:str )->bool:
    return re.fullmatch(r'\d{6}',verification_code)

format_checkers = {
    'username': check_username_format,
    'password': check_password_format,
    'email': check_email_format,
    'user_type': check_user_type_format,
    'verification_code':check_verification_code_format
}

if __name__ == '__main__':
    pass
