"""1-misol"""
# 1.	Postgresql bazaga python yordamida ulaning
#  Product nomli jadval yarating
# (id,name,price, color,image)

import psycopg2

db_params = {
    'database': 'new_list',
    'user': 'postgres',
    'password': '1',
    'host': 'localhost',
    'port': '5432'

};

try:
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    print("Connected to PostgreSQL")

    create_query = '''
    CREATE TABLE IF NOT EXISTS Product(    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price INTEGER NOT NULL,
    color VARCHAR(255) NOT NULL,    
    image VARCHAR(255) NOT NULL
    );
    '''

    cur.execute(create_query)
    conn.commit()
    print("Table created successfully")

except (Exception, psycopg2.DatabaseError) as error:
    print(error)


finally:
    if conn is not None:
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")

# '''2-misol'''
#
#
# # 2.	Insert_product , select_all_products , update_product,
# # delete_product nomli funksiyalar yarating.
#
# def insert_product():
#     conn = psycopg2.connect(**db_params)
#     cur = conn.cursor()
#
#     name = input("Enter product name: ")
#     price = float(input("Enter product price: "))
#     color = input("Enter product color: ")
#     image = input("Enter product image URL: ")
#
#     cur.execute("INSERT INTO Product( name,price,color,image)"
#                 " VALUES(%s,%s,%s,%s);", )
#     conn.commit()
#     conn.close()
#     cur.close()
#
#
# if __name__ == '__main__':
#     insert_product()

#
# def select_product():
#     conn = psycopg2.connect(**db_params)
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM Product")
#     rows = cur.fetchall()
#
#     for row in rows:
#         print(row)
#
#
# def update_product(product_id=None):
#     conn = psycopg2.connect(**db_params)
#     cur = conn.cursor()
#
#     name = input("Enter product name: ")
#     price = input("Enter product price: ")
#     color = input("Enter product color: ")
#     image = input("Enter product image URL: ")
#
#     cur.execute("""
#                 UPDATE Product
#                 SET name = %s, price = %s, color = %s, image = %s
#                 WHERE id = %s;
#             """, (name, price, color, image, product_id))
#
#     conn.commit()
#     print("Product updated successfully")
#     cur.close()
#     conn.close()
# update_product()
#
# def delete_product(product_id=None):
#     conn = psycopg2.connect(**db_params)
#     cur = conn.cursor()
#
#     cur.execute('DELETE FROM Product WHERE id = %s', (product_id,))
#     conn.commit()
#     print("Product deleted successfully")
#
#     cur.close()
#     conn.close()
# delete_product(1)
#

#	Alphabet nomli class yozing .class obyektlarini
# #	iteratsiya qilish imkoni   bo’lsin (iterator).
# #	obyektni for sikli orqali iteratsiya qilinsa 26 ta alifbo xarflari chiqsin
#
#
# class Alphabet:
#     def __init__(self):
#         self.harf=[
#             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
#             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
#             'Y', 'Z', 'Sh', 'Ch'
#         ]
#         self.index=0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index<len(self.harf):
#             harf=self.harf[self.index]
#             self.index+=1
#             time.sleep(1)
#             return harf
#         else:
#             raise StopIteration
#
# if __name__=="__main__":
#     alphabet=Alphabet()
#     for harf in alphabet:
#         print(harf)


# 4.	print_numbers va print_leters nomli funksiyalar yarating.
# prit_numbers funksiyasi (1,5) gacha bo’lgan sonlarni ,
# print_letters esa  ‘’ABCDE” belgilarni loop da bitta dan time sleep(1) qo’yib ,
# parallel 2ta thread yarating.Ekranga parallel ravishda itemlar chiqsin.
#
# import time
# import threading
#
# def print_numbers():
#     for number in range(1, 6):
#         print(number)
#         time.sleep(1)
#
# def print_letters():
#     letters = "ABCDE"
#     for letter in letters:
#         print(letter)
#         time.sleep(1)
#
# if __name__ == "__main__":
#     thread1 = threading.Thread(target=print_numbers)
#     thread2 = threading.Thread(target=print_letters)
#
#     thread1.start()
#     thread2.start()
#
#     thread1.join()
#     thread2.join()
#
#
#
# """6-mmisol"""
#
# #	DbConnect nomli ContextManager yarating.
# #	Va uning vazifasi python orqali PostGresqlga
# #	ulanish (conn,cur)
#
# import psycopg2
#
# db_params = {
#     'database': 'new_list',
#     'user': 'postgres',
#     'password': '1',
#     'host': 'localhost',
#     'port': 5432
# }
#
# class DbConnect:
#     def __enter__(self):
#         self.conn = psycopg2.connect(**db_params)
#         self.cursor = self.conn.cursor()
#         return self.conn, self.cursor
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is not None:
#             self.conn.rollback()
#         else:
#             self.conn.commit()
#             self.cursor.close()
#             self.conn.close()
#
# if __name__ == '__main__':
#     with DbConnect()as (conn, cursor):
#         cursor.execute('select * from users')
#         for row in cursor.fetchall():
#             print(row)
#
"""5-misol"""
#    .Product nomli class yarating (1 – misoldagi Product ).
# # Product classiga save() nomli object method yarating. Uni
# vazifasi object attributelari orqali bazaga saqlasin.

class Product:
    def __init__(self, name, price, color, image):
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save(self, db_params):
        try:
            conn = psycopg2.connect(**db_params)
            cur = conn.cursor()

            cur.execute("""
                INSERT INTO Product(name, price, color, image) 
                VALUES (%s, %s, %s, %s);
            """, (self.name, self.price, self.color, self.image))

            conn.commit()
            cur.close()
            conn.close()
            print("Product table created successfully")

new_product = Product("Product1", 29.99, "Red", "product1.jpg")
new_product.save(db_params)


