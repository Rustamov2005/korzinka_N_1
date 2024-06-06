import classes


def add_staff():
    print("Yangi ishchi olishingiz mumkun:")
    return classes.Database_ishchilar.insert_ishchilar()


def change_category():
    print('Categoriya jadvalini ozgartirish:')
    cste = input("""
        1.insert
        2.delete
        3.select
        4.update
        5.Orqaga
            >>>""")
    if cste == '1':
        return classes.Database_category.insert_category()
    elif cste == '2':
        return classes.Database_category.delete_category()
    elif cste == '3':
        return classes.Database_category.select_category()
    elif cste == '4':
        return classes.Database_category.update_category()
    elif cste == '5':
        return jadvallarni_ozgartirish()
    else:
        print("Bunday xizmat macjud emas!!!")
        return change_category()


def change_ish_category():
    print('ish_ategoriya jadvalini ozgartirish:')
    ish_cate = input("""
           1.insert
           2.delete
           3.select
           4.update
           5.Orqaga
               >>>""")
    if ish_cate == '1':
        return classes.Database_ish_category.insert_ish_category()
    elif ish_cate == '2':
        return classes.Database_ish_category.delete_ish_category()
    elif ish_cate == '3':
        return classes.Database_ish_category.select_ish_category()
    elif ish_cate == '4':
        return classes.Database_ish_category.update_ish_category()
    elif ish_cate == '5':
        return jadvallarni_ozgartirish()
    else:
        print("Bunday xizmat macjud emas!!!")
        return change_ish_category()


def change_maxsulot():
    print('maxsulot jadvalini ozgartirish:')
    ish_cate = input("""
              1.insert
              2.delete
              3.select
              4.update
              5.Orqaga
                  >>>""")
    if ish_cate == '1':
        return classes.Databese_maxsulot.insert_maxsulot()
    elif ish_cate == '2':
        return classes.Databese_maxsulot.delete_maxsulot()
    elif ish_cate == '3':
        return classes.Databese_maxsulot.select_maxsulot()
    elif ish_cate == '4':
        return classes.Databese_maxsulot.update_maxsulot()
    elif ish_cate == '5':
        return jadvallarni_ozgartirish()
    else:
        print("Bunday xizmat macjud emas!!!")
        return change_maxsulot()


def change_user():
    print('users jadvalini ozgartirish:')
    ish_cate = input("""
                  1.insert
                  2.delete
                  3.select
                  4.update
                  5.Orqaga
                      >>>""")
    if ish_cate == '1':
        return classes.Database_users.insert_users()
    elif ish_cate == '2':
        return classes.Database_users.delete_users()
    elif ish_cate == '3':
        return classes.Database_users.select_users()
    elif ish_cate == '4':
        return classes.Database_users.update_users()
    elif ish_cate == '5':
        return jadvallarni_ozgartirish()
    else:
        print("Bunday xizmat macjud emas!!!")
        return change_user()


def change_ishchilar():
    print('ishchilar jadvalini ozgartirish:')
    ish_cate = input("""
                     1.insert
                     2.delete
                     3.select
                     4.update
                     5.Orqaga
                         >>>""")
    if ish_cate == '1':
        return classes.Database_ishchilar.insert_ishchilar()
    elif ish_cate == '2':
        return classes.Database_ishchilar.delete_ishchilar()
    elif ish_cate == '3':
        return classes.Database_ishchilar.select_ishchilar()
    elif ish_cate == '4':
        return classes.Database_ishchilar.update_ishchilar()
    elif ish_cate == '5':
        return jadvallarni_ozgartirish()
    else:
        print("Bunday xizmat macjud emas!!!")
        return change_ishchilar()


def change_chegirma():
    print('chegirma jadvalini ozgartirish:')
    ish_cate = input("""
                         1.insert
                         2.delete
                         3.select
                         4.update
                         5.Orqaga
                             >>>""")
    if ish_cate == '1':
        return classes.Database_chegirma_product.insert_chegirma_product()
    elif ish_cate == '2':
        return classes.Database_chegirma_product.delete_chegirma_product()
    elif ish_cate == '3':
        return classes.Database_chegirma_product.select_chegirma_product()
    elif ish_cate == '4':
        return classes.Database_chegirma_product.update_chwgirma_product()
    elif ish_cate == '5':
        return jadvallarni_ozgartirish()
    else:
        print("Bunday xizmat macjud emas!!!")
        return change_chegirma()


def commints():
    serveses = input("""
        Xizmat turini tanlamg:
            `1.select commint
            2.insert commint
            3.delete commint
            4. Orqaga
          >>>""")
    if serveses == '1':
        return classes.Database_commint.select_commint()
    elif serveses == '2':
        return classes.Database_commint.insert_commint()
    elif serveses == '3':
        return classes.Database_commint.delete_commint()
    elif serveses == '4':
        return admin_page()
    else:
        print("Bunday xizmat macjud emas!!!")
        return commints()


def new_productse():
    print('Yangi tovar buyritma qilish:')
    ish_cate = input("""
                             1.insert
                             2.delete
                             3.select
                             4.update
                             5.Orqaga
                                 >>>""")
    if ish_cate == '1':
        return classes.Database_new_product.insert_new_product()
    elif ish_cate == '2':
        return classes.Database_new_product.delete_new_product()
    elif ish_cate == '3':
        return classes.Database_new_product.select_new_product()
    elif ish_cate == '4':
        return classes.Database_new_product.update_new_product()
    elif ish_cate == '5':
        return admin_page()
    else:
        print("Bunday xizmat macjud emas!!!")
        return change_chegirma()


def korzinka_cardse():
    servese = input("""
        Xizmat turini tanlang:
            1.insert 
            2.delete
            3.select
            4.Orqaga
           >>>""")
    if servese == '1':
        return classes.Database_korzinka_card.insert_card()
    elif servese == '2':
        return classes.Database_korzinka_card.delete_card()
    elif servese == '3':
        return classes.Database_korzinka_card.select_card()
    elif servese == '4':
        return jadvallarni_ozgartirish()
    else:
        print("Bunday xizmat macjud emas!!!")
        return jadvallarni_ozgartirish()


def jadvallarni_ozgartirish():
    jadvallar = input("""
        Qaysi jadvalni o'zgartirirmoqchisiz:
            1.categoriya
            2.ish_categoriya
            3.maxsulot
            4.users
            5.ishchilar
            6.chegirma_product
            7.Orqaga
            8.commintni ko'rish
            9.korzinka card
            10.new product buyritma qilish
            11. Xarid
            
                 >>>""")
    if jadvallar == "1":
        return change_category()
    elif jadvallar == "2":
        return change_ish_category()
    elif jadvallar == "3":
        return change_maxsulot()
    elif jadvallar == "4":
        return change_user()
    elif jadvallar == "5":
        return change_ishchilar()
    elif jadvallar == "6":
        return change_chegirma()
    elif jadvallar == "7":
        return admin_page()
    elif jadvallar == "8":
        return commints()
    elif jadvallar == "9":
        return change_user()
    elif jadvallar == "10":
        return new_productse()
    elif jadvallar == "11":
        return change_maxsulot()
    else:
        print("Bunday xizmat turi mavjud emas:")
        return jadvallarni_ozgartirish()


def chegirma_qoshish():
    print("Chegirmaga maxsulot qo'shish:")
    return classes.Database_chegirma_product.insert_chegirma_product()


def admin_page():
    serveses = input("""
        Xizmat turini tanlang:
            1.Jadvallani o'zgartirish.
            2.Yangi ishchi qo'shish.
            3.Yangi maxsulot buyirtirish.
            4.Chegirmaga maxsulotlar qo'shish.
        >>>""")
    if serveses == '1':
        return jadvallarni_ozgartirish()
    elif serveses == '2':
        return add_staff()
    elif serveses == '3':
        return new_productse()
    elif serveses == '4':
        return chegirma_qoshish()
    else:
        print("Bunday xizmat mavjud emas:")
        return admin_page()


if __name__ == '__main__':
    admin_page()