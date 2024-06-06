from login_page import login
import regester_page


def kirish_():
    kirish = input("""
        Korzinka plarformasiga xush kelibsiz:
            1.Login
            2.Regester
          >>>""")
    if kirish == "1":
        return login()

    elif kirish == "2":
        return regester_page.regester()

    else:
        print("Siz noto'g'ri tugmani tanladingiz !!!")
        return kirish_()


if __name__ == "__main__":
    kirish_()