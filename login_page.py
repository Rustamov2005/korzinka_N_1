import classes
import user_page


def login():
    print("Login pg ga xush kelibsiz>>>")
    username = input("Usernamingizni kiriting:")
    password_2 = input("Passwordingizni kiriting:")
    return classes.Database_check_user.check_user(username, password_2)
