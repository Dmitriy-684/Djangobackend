
def validate(email: str, password: str) -> tuple:
    is_valid_email, is_valid_password = False, False
    if (email.count("@") == 1) and (email[-3] == "." or email[-4] == "."):
        if (not [s for s in email if s in "<>()[],;:\/\"*"]) and (not email.isspace()):
            if email[0].isalpha() or email[0].isdigit():
                if email.split("@")[0][-1].isalpha() or email.split("@")[0][-1].isdigit():
                    if not [s for s in email if s.lower() in "йцукенгшщзхъфывапролджэячсмитьбюё"]:
                        is_valid_email = True
    if (len(password) >= 12) and (not [s for s in password if s.lower() in "йцукенгшщзхъфывапролджэячсмитьбю"]):
        if (len([s for s in password if s.isalpha()]) >= 1) and (len([s for s in password if s.isdigit()]) >= 1):
            if [s for s in password if s in "!@#$%^&*()_+\"№;:?`~{}<>/.,|-="]:
                if (len([s for s in password if s.islower()]) >= 1) and (len([s for s in password if s.isupper()]) >= 1):
                    is_valid_password = True

    return is_valid_email, is_valid_password
