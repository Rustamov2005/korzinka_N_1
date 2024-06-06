import classes


def maxsulot_xaridlari():
    serveses = input("""
        Xizmat turini tanlang:
            1.sotib olingan maxsulotlar
            2.maxsulot sotib olish
            3.Orqaga
                >>>""")
    if serveses == "1":
        return classes.Database_xarid.select_xarid()
    elif serveses == "2":
        return classes.Database_xarid.insert_xarid()
    elif serveses == "3":
        return user_server()
    else:
        print("Bunday xizmat mavjud emas!!!")
        return user_server()


def korzinka_cards():
    serves = input("""
        Xizmat turlari:
            1.Card balance
            2.Korzinka karta olish
            3.Orqaga
             >>>""")
    if serves == "1":
        print("Sizning kard balansingiz:")
        return classes.Database_korzinka_card.select_2()
    elif serves == "2":
        print("Korzinka karta olishingiz mumkun:")
        return classes.Database_korzinka_card.insert_card()
    elif serves == "3":
        return user_server()
    else:
        print("Bunday xizmat mavjud emas:")
        return korzinka_cards()


def izlash():
    return classes.Database_izlash.select_izlash()


def commintari():
    serveses = input("""
        Xizmatlar:
            1.Commint qoldirish.
            2.Commintlarni ko'rish
            3.Orqaga
           >>>""")
    if serveses == "1":
        return classes.Database_commint.insert_commint()
    elif serveses == "2":
        return classes.Database_commint.select_commint()
    elif serveses == "3":
        return user_server()
    else:
        print("Bunday xizmat macjud emas!!!")
        return commintari()


def user_server():
    servesesa = input("""
        Xizmat turini tanlang:
            1.Maxsulot sotib olish.
            2.korzinka karta.
            3. Maxsulot qidirish.
            4.Comintariya qoldirish.
            5.Chegirmadagi tovarlar.
            6.maxsulot sotin olish.
           >>>""")
    if servesesa == "1":
        return maxsulot_xaridlari()
    if servesesa == "2":
        return korzinka_cards()
    if servesesa == "3":
        return izlash()
    elif servesesa == "4":
        return commintari()
    elif servesesa == "5":
        return classes.Database_chegirma_product.select_chegirma_product()
    else:
        print("Bunday xizmat mavjud emas!!!")
        return user_server()


if __name__ == "__main__":
    user_server()