from django.core.exceptions import ValidationError
import re

def validate_email(email):
    EMAIL_REGEX = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(EMAIL_REGEX, email) is None:
        raise ValidationError("EMAIL_INVALIDATION")
                           
def validate_password(password):
    PASSWORD_REGEX = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[?!@#$%*&])[A-Za-z\d?!@#$%*&]{8,}$'
    if re.match(PASSWORD_REGEX, password) is None:
        raise ValidationError("PASSWORD_INVALIDATION")