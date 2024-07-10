


import sqlite3
from veritabaniBaglantisi  import *
connection = sqlite3.connect("chinook.db")

sql="INSERT INTO genres(name) VALUES ('Macera')"#veritababnına ınsert ınto kullanarak genres tablosunun name alanına values olarak Macera ekledik
cursor.execute(sql) #sql kodu executable durumdadır demek

connection.commit() #excutable durumda olan sql kodu commit ile aksiyon alır ve ekleme işlemi gerçekleşir

connection.close()