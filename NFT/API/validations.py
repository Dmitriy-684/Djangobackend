
def validate(email: str, password: str) -> tuple:
    is_valid_email = (False, "Invalid Email Format")
    is_valid_password = (False, "Password length at least 8 characters")
    if (email.count("@") == 1) and (email[-3] == "." or email[-4] == "."):
        if (not [s for s in email if s in "<>()[],;:\/\"*"]) and (not email.isspace()):
            if email[0].isalpha() or email[0].isdigit():
                if email.split("@")[0][-1].isalpha() or email.split("@")[0][-1].isdigit():
                    if not [s for s in email if s.lower() in "йцукенгшщзхъфывапролджэячсмитьбюё"]:
                        is_valid_email = (True, "Email is good")
    if len(password) >= 12:
        is_valid_password = (False, "Cyrillic characters are not allowed in the password")
        if not [s for s in password if s.lower() in "йцукенгшщзхъфывапролджэячсмитьбю"]:
            is_valid_password = (False, "The password must contain at least one Latin character")
            if len([s for s in password if s.isalpha()]) >= 1:
                is_valid_password = (False, "Password must contain at least one digit")
                if len([s for s in password if s.isdigit()]) >= 1:
                    is_valid_password = (False, "Password must contain at least one special character")
                    if [s for s in password if s in "!@#$%^&*()_+\"№;:?`~{}<>/.,|-="]:
                        is_valid_password = (False, "The password must contain at least one lowercase character")
                        if len([s for s in password if s.islower()]) >= 1:
                            is_valid_password = (False, "Password must contain at least one uppercase character")
                            if len([s for s in password if s.isupper()]) >= 1:
                                is_valid_password = (True, "Password is good")
    return is_valid_email, is_valid_password