
def validate(email: str, password: str) -> tuple:
    is_valid_email = {"Valid": False, "Message": "Неверный формат Email"}
    is_valid_password = {"Valid": False, "Message": "Длина пароля должна составлять минимум двенадцать символов"}
    if (email.count("@") == 1) and (email[-3] == "." or email[-4] == "."):
        if (not [s for s in email if s in "<>()[],;:\/\"*"]) and (not email.isspace()):
            if email[0].isalpha() or email[0].isdigit():
                if email.split("@")[0][-1].isalpha() or email.split("@")[0][-1].isdigit():
                    if not [s for s in email if s.lower() in "йцукенгшщзхъфывапролджэячсмитьбюё"]:
                        is_valid_email["Valid"], is_valid_email["Message"] = True, ""
    if len(password) >= 12:
        is_valid_password["Message"] = "В пароле не допускается использование кириллицы"
        if not [s for s in password if s.lower() in "йцукенгшщзхъфывапролджэячсмитьбю"]:
            is_valid_password["Message"] = "В пароле должен быть минимум один символ латинского алфавита"
            if len([s for s in password if s.isalpha()]) >= 1:
                is_valid_password["Message"] = "В пароле должна быть минимум одна цифра"
                if len([s for s in password if s.isdigit()]) >= 1:
                    is_valid_password["Message"] = "В пароле должен быть минимум один спецсимвол"
                    if [s for s in password if s in "!@#$%^&*()_+\"№;:?`~{}<>/.,|-="]:
                        is_valid_password["Message"] = "В пароле должен быть минимум один символ нижнего регистра"
                        if len([s for s in password if s.islower()]) >= 1:
                            is_valid_password["Message"] = "В пароле должен быть минимум один символ верхнего регистра"
                            if len([s for s in password if s.isupper()]) >= 1:
                                is_valid_password["Valid"], is_valid_password["Message"] = True, ""
    return is_valid_email, is_valid_password
