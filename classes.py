from connect_database import Database
import regester_page
import admin_page
import user_page
import login_page


class Database_users:

    @staticmethod
    def create_users():
        query = f"""CREATE TABLE users(id SERIAL PRIMARY KEY, username VARCHAR(20), password VARCHAR(5));"""
        Database.connect(query, 'create')
        print("Jadval yaratildi:")

    @staticmethod
    def insert_users():
        username = input("Username ni kiriting: ")
        password = input("Password ni kiriting: ")
        query = f"""INSERT INTO users(username, password) VALUES ('{username}', '{password}');"""
        Database.connect(query, 'insert')
        print("Siz muvofaqqiyatli ro'yxatdan o'tdingiz:")
        return user_page.user_server()

    @staticmethod
    def select_users():
        quere = f"""SELECT * FROM users;"""
        print(Database.connect(quere, 'select'))
        return admin_page.admin_page()

    @staticmethod
    def update_users():
        username_1 = input("Avvalgi usernameni kiriting:")
        username = input("Yangi username ni kiriting: ")
        password = input("Yangi password ni kiriting: ")
        query = f"""UPDATE users SET username = '{username}', password = '{password}' WHERE username = '{username_1}';"""
        Database.connect(query, 'update')
        print("Muvofaqqiyatli o'zgartirildi>>>")
        return admin_page.admin_page()

    @staticmethod
    def delete_users():
        username = input("usernameni kiriting:")
        query = f"""DELETE FROM users WHERE username = '{username}';"""
        Database.connect(query, 'delete')
        print(f"{username} nomli user o'chirib yuborildi>>>")
        return admin_page.admin_page()


class Database_category:

    @staticmethod
    def create_category():
        query = "CREATE TABLE category(id SERIAL PRIMARY KEY, name VARCHAR(50));"
        Database.connect(query, 'create')
        print("Table yaratildi>>>")

    @staticmethod
    def insert_category():
        name = input("Kategoriya nomini kiriting:")
        query = f"""INSERT INTO category(name) VALUES('{name}');"""
        Database.connect(query, 'create')
        print("Kategorya yaratildi>>>")
        return admin_page.admin_page()

    @staticmethod
    def select_category():
        query = "SELECT * FROM category;"
        print(Database.connect(query, 'select'))
        return admin_page.admin_page()

    @staticmethod
    def delete_category():
        name = input("Kategoriya nomini kiriting:")
        query = f"""DELETE FROM category WHERE name = '{name}'"""
        Database.connect(query, 'delete')
        print(f"{name} bu kategoriya turi o'chirib tashlandi>>>")
        return admin_page.admin_page()

    @staticmethod
    def update_category():
        name_1 = input("Kategoriyaning avvalgi nomini kiriting:")
        name = input("Kategoriyaning yangi nomini kiriting:")
        query = f"""UPDATE category SET name = '{name}' WHERE name = '{name_1}'"""
        Database.connect(query, 'update')
        print("Katogoriya nomi o'zgartirildi>>>")
        return admin_page.admin_page()


class Databese_maxsulot:

    @staticmethod
    def create_maxsulot():
        query = """CREATE TABLE maxsulot(id SERIAL PRIMARY KEY, name VARCHAR(100), 
        narxi VARCHAR(100), category_id INT REFERENCES category(id));"""
        Database.connect(query, 'create')
        print("Table yatildi>>>")

    @staticmethod
    def insert_maxsulot():
        name = input("Maxsulot nomini kiriting:")
        narxi = input("Maxsulot narxini kiriting:")
        category_id = input("Cateroriya id sini kiriting:")
        query = f"""INSERT INTO maxsulot(name, narxi, category_id) VALUES('{name}', '{narxi}', {category_id})"""
        Database.connect(query, 'insert')
        print(f"{name} nomli maxsulot qo'shildi>>>")
        return admin_page.admin_page()

    @staticmethod
    def select_maxsulot():
        query = "SELECT m.id, m.name, m.narxi, c.name FROM maxsulot m INNER JOIN category c ON m.category_id = c.id;"
        print(Database.connect(query, 'select'))
        return admin_page.admin_page()

    @staticmethod
    def delete_maxsulot():
        name = input("Maxsulot nomini kiriting:")
        query = f"""DELETE FROM maxsulot WHERE name = '{name}';"""
        Database.connect(query, 'delete')
        print(f"{name} nomli maxsulot o'chirib yuborildi>>>")
        return admin_page.admin_page()

    @staticmethod
    def update_maxsulot():
        name_1 = input("Maxsulotning avvalgi nomini kiriting:")
        name = input("Maxsulotning yangi nomini kiriting:")
        narxi = input("Maxsulot narxini kiriting:")
        category_id = input("Category id ni kiriting:")
        query = f"""UPDATE maxsulot SET name = '{name}', narxi = '{narxi}', 
        category_id = '{category_id}' WHERE name = '{name_1}';"""
        Database.connect(query, 'update')
        print("Maxsulot o'zgartirildi>>>")
        return admin_page.admin_page()


class Database_ishchilar:

    @staticmethod
    def create_ishchilar():
        query = """CREATE TABLE ishchilar(id SERIAL PRIMARY KEY, first_name VARCHAR(50),
         last_name VARCHAR(50), age INT, maoshi VARCHAR(20), ISH_category_id INT REFERENCES ish_category(id));"""
        Database.connect(query, 'create')
        print("Jadval yaratildi>>>")

    @staticmethod
    def insert_ishchilar():
        first_name = input("Ismini kiriting:")
        last_name = input("Familyasini kiriting:")
        age = input("Ishchining yoshini kiriting:")
        maosh = input("Ishchining maoshini kiriting kiriting:")
        ish_category = input("Ish kategoriyasini kiriting:")
        query = f"""INSERT INTO ishchilar(first_name, last_name, age, maoshi, ish_category_id) VALUES('{first_name}',
         '{last_name}', '{age}', '{maosh}', '{ish_category}');"""
        Database.connect(query, 'insert')
        print(f"{first_name} ishchilar ro'yxatiga qo'shildi>>>")
        return admin_page.admin_page()


    @staticmethod
    def update_ishchilar():
        first_name_1 = input("Avvalgi ismini kiriting:")
        first_name = input("Ismini kiriting:")
        last_name = input("Familyasini kiriting:")
        age = input("Ishchining yoshini kiriting:")
        maosh = input("Ishchining maoshini  kiriting:")
        ish_category = input("Ish kategoriyasini kiriting:")
        query = f"""UPDATE ishchilar SET first_name = '{first_name}', last_name = '{last_name}',
        age = '{age}', maoshi = '{maosh}', ish_category_id = '{ish_category}' WHERE first_name = '{first_name_1}';"""
        Database.connect(query, 'update')
        print("Foydalanuvchi malumoti o'zgartirildi>>>")
        return admin_page.admin_page()

    @staticmethod
    def delete_ishchilar():
        first_name = input("Foydalanuvchi ismini kiriting:")
        query = f"""DELETE FROM ishchilar WHERE first_name = '{first_name}'"""
        Database.connect(query, 'delete')
        print(f"{first_name} nomli ishchi o'chirib yuborildi>>>")
        return admin_page.admin_page()

    @staticmethod
    def select_ishchilar():
        query = ("SELECT i.id, i.first_name, i.last_name, i.age, i.maoshi, "
                 "s.name FROM ishchilar i INNER JOIN ish_category s ON s.id = i.ish_category_id;")
        print(Database.connect(query, 'select'))
        return admin_page.admin_page()

class Database_ish_category:

    @staticmethod
    def create_ish_category():
        query = f"CREATE TABLE ish_category(id SERIAL PRIMARY KEY, name VARCHAR(50));"
        Database.connect(query, 'create')
        print("Jadval yaratildi>>>")

    @staticmethod
    def insert_ish_category():
        name = input("Categoriya nomini kiriting:")
        query = f"INSERT INTO ish_category(name) VALUES('{name}');"
        Database.connect(query, 'insert')
        print("Kategoriya yaratildi>>>")
        return admin_page.admin_page()

    @staticmethod
    def select_ish_category():
        query = "SELECT * FROM ish_category;"
        print(Database.connect(query, 'select'))
        return admin_page.admin_page()

    @staticmethod
    def delete_ish_category():
        name = input("Kategoriya nomini kiriting:")
        query = f"""DELETE FROM ish_category WHERE name = '{name}';"""
        Database.connect(query, 'delete')
        print(f"{name} nomli kategoriya o'chirib yuborildi>>>")
        return admin_page.admin_page()

    @staticmethod
    def update_ish_category():
        name_1 = input("Avvalgi kategoriya nomini kiriting:")
        name = input("Kategoriya nomini kiriting:")
        query = f"""UPDATE ish_category SET name = '{name}' WHERE name = '{name_1}';"""
        Database.connect(query, 'update')
        print("Malumot o'zgartirildi>>>")
        return admin_page.admin_page()

class Database_new_product:

    @staticmethod
    def create_new_product():
        query = """CREATE TABLE new_product(id SERIAL PRIMARY KEY, name VARCHAR(50),
         narxi VARCHAR(50), category_id INT REFERENCES category(id));"""
        Database.connect(query, 'create')
        print("Jadval yaratildi>>>")

    @staticmethod
    def insert_new_product():
        name = input("Maxsulot nomini kiriting:")
        narxi = input("Maxsulot narxini kiriting:")
        category_id = input("Cateroriya id sini kiriting:")
        query = f"""INSERT INTO new_product(name, narxi, category_id) VALUES('{name}', '{narxi}', {category_id})"""
        Database.connect(query, 'insert')
        print(f"{name} nomli maxsulot qo'shildi>>>")
        return admin_page.admin_page()

    @staticmethod
    def select_new_product():
        query = """SELECT n.id, n.name, n.narxi, 
        c.name FROM new_product n INNER JOIN category c ON n.category_id = c.id;"""
        print(Database.connect(query, 'select'))
        return admin_page.admin_page()

    @staticmethod
    def delete_new_product():
        name = input("Maxsulot nomini kiriting:")
        query = f"""DELETE FROM new_product WHERE name = '{name}';"""
        Database.connect(query, 'delete')
        print(f"{name} nomli maxsulot o'chirib yuborildi>>>")
        return admin_page.admin_page()

    @staticmethod
    def update_new_product():
        name_1 = input("Maxsulotning avvalgi nomini kiriting:")
        name = input("Maxsulotning yangi nomini kiriting:")
        narxi = input("Maxsulot narxini kiriting:")
        category_id = input("Category id ni kiriting:")
        query = f"""UPDATE new_product SET name = '{name}', narxi = '{narxi}', 
            category_id = '{category_id}' WHERE name = '{name_1}';"""
        Database.connect(query, 'update')
        print("Maxsulot o'zgartirildi>>>")
        return admin_page.admin_page()


class Database_chegirma_product:

    @staticmethod
    def create_chegirma_product():
        query = """CREATE TABLE chegirma_product(id SERIAL PRIMARY KEY, name VARCHAR(50),
         narxi VARCHAR(50), category_id INT REFERENCES category(id));"""
        Database.connect(query, 'create')
        print("Jadval yaratildi>>>")

    @staticmethod
    def insert_chegirma_product():
        name = input("Maxsulot nomini kiriting:")
        narxi = input("Maxsulot narxini kiriting:")
        category_id = input("Cateroriya id sini kiriting:")
        query = f"""INSERT INTO chegirma_product(name, narxi, category_id) VALUES('{name}', '{narxi}', {category_id})"""
        Database.connect(query, 'insert')
        print(f"{name} nomli maxsulot qo'shildi>>>")
        return admin_page.admin_page()


    @staticmethod
    def select_chegirma_product():
        query = """SELECT c.id, c.name, c.narxi, 
        k.name   FROM chegirma_product c INNER JOIN category k ON c.category_id = k.id;"""
        print(Database.connect(query, 'select'))



    @staticmethod
    def delete_chegirma_product():
        name = input("Maxsulot nomini kiriting:")
        query = f"""DELETE FROM chegirma_product WHERE name = '{name}';"""
        Database.connect(query, 'delete')
        print(f"{name} nomli maxsulot o'chirib yuborildi>>>")
        return admin_page.admin_page()

    @staticmethod
    def update_chwgirma_product():
        name_1 = input("Maxsulotning avvalgi nomini kiriting:")
        name = input("Maxsulotning yangi nomini kiriting:")
        narxi = input("Maxsulot narxini kiriting:")
        category_id = input("Category id ni kiriting:")
        query = f"""UPDATE chegirma_product SET name = '{name}', narxi = '{narxi}', 
            category_id = '{category_id}' WHERE name = '{name_1}';"""
        Database.connect(query, 'update')
        print("Maxsulot o'zgartirildi>>>")
        return admin_page.admin_page()


class Database_commint:

    @staticmethod
    def create_commint():
        query = """CREATE TABLE commint(id SERIAL PRIMARY KEY, commint TEXT, users_id INT REFERENCES users(id),
         maxsulot_id INT REFERENCES maxsulot(id));"""
        Database.connect(query, 'create')
        print("Jadval yaratildi>>>")

    @staticmethod
    def select_commint():
        query = """SELECT c.id, c.commint, u.username, 
        m.name FROM commint c INNER JOIN maxsulot m ON c.maxsulot_id = m.id INNER JOIN users u ON c.users_id = u.id ;"""
        print(Database.connect(query, 'select'))

    @staticmethod
    def insert_commint():
        commint = input("Komintariyani kiriting:")
        users_id = input("Users id ni kiriting:")
        maxsulot_id = input("Maxsulot id ni kiriting:")
        query = f"""INSERT INTO commint(commint, users_id, maxsulot_id) VALUES('{commint}', '{users_id}', '{maxsulot_id}')"""
        Database.connect(query, 'insert')
        print("Sizning komintaryangiz qoldirildi>>>")

    @staticmethod
    def delete_commint():
        idsi = input("Komintariya id sini kiriting:")
        query = f"""DELETE FROM commin WHERE id = '{idsi}'"""
        Database.connect(query, 'delete')
        print(f"Id si {idsi} ga teng bo'lgan commin o'chirildi>>>")


class Database_xarid:

    @staticmethod
    def creste_xarid():
        query = """CREATE TABLE xarid(id SERIAL PRIMARY KEY, maxsulot_id INT REFERENCES maxsulot(id));"""
        Database.connect(query, 'create')
        print("Jadval yaratildi>>>")

    @staticmethod
    def insert_xarid():
        idsi = input("Maxsulot id sini kiriting:")
        query = f"""INSERT INTO xarid(maxsulot_id) VALUES('{idsi}');"""
        Database.connect(query, 'insert')
        print("Xarid amalga oshirildi>>>")
        return user_page.user_server()

    @staticmethod
    def select_xarid():
        query = """SELECT x.id, m.name FROM xarid x INNER JOIN maxsulot m ON x.maxsulot_id = m.id;"""
        print("Sizning xaridingiz:")
        print(Database.connect(query, 'select'))
        return user_page.user_server()


class Database_korzinka_card:

    @staticmethod
    def create_card():
        query = """CREATE TABLE korzinka_card(id SERIAL PRIMARY KEY, users_id INT REFERENCES users(id),
         balanse VARCHAR(100));"""
        Database.connect(query, 'create')
        print("Jadval yaratildi>>>")

    @staticmethod
    def insert_card():
        users_id = input("Users id ni kiriting:")
        query = f"""INSERT INTO korzinka_card(users_id, balanse) VALUES('{users_id}', '0');"""
        Database.connect(query, 'insert')
        print("Siz korzinka kartaga ega bo'ldingiz>>>")
        return user_page.user_server()

    @staticmethod
    def select_card():
        query = """SELECT c.id, u.username, c.balanse FROM korzinka_card c INNER JOIN users u ON c.users_id = u.id ;"""
        print(Database.connect(query, 'select'))
        return admin_page.admin_page()

    @staticmethod
    def delete_card():
        idsi = input("Karta id sini kiriting:")
        query = f"""DELETE FROM korzinka_card WHERE id = '{idsi}';"""
        Database.connect(query, 'delete')
        print(f"{idsi} li card o'chirib yuborildi:")
        return admin_page.admin_page()

    @staticmethod
    def select_2():
        idsi = input("Users idingizni kiriting:")
        query = f"""SELECT balanse FROM korzinka_card WHERE users_id = '{idsi}';"""
        print(Database.connect(query, 'select'))
        return user_page.korzinka_cards()


class Database_izlash:

    @staticmethod
    def select_izlash():
        name_1 = input("Maxsulot nomini kiriting:")
        query = f"""SELECT  m.id, m.name, m.narxi, 
        c.name FROM maxsulot m INNER JOIN category c ON m.category_id = c.id WHERE m.name LIKE '%{name_1}%';"""
        print(Database.connect(query, 'select'))
        return Database_xarid.insert_xarid()


class Database_check_user:

    @staticmethod
    def check_user(username, password_2):
        query = f"""SELECT * FROM users WHERE username = '{username}' and password = '{password_2}';"""
        databas = Database.connect(query, 'select')
        if databas:
            if f'{username}' == "rustamov":
                return admin_page.admin_page()
            else:
                return user_page.user_server()
        else:
            print("password yoki username xato tekshirib qayta urining!!!")
            return login_page.login()


if __name__ == '__main__':
    Databese_maxsulot.select












    _maxsulot()

