from py_cursor import PyCursor
from py_sqlite import PySqlite

dict = {
    "name": "text",
    "password": "text",
    "isAdmin": "integer",
}

PySqlite.initDbFromDict("dbs/", "user", dict)

cursor = PyCursor("dbs/", "user")

cursor.insert("id, name, password, isAdmin", "001, 'calen', 12345678, 1")

cursor.update("name = 'calen'", 'password = 87654321')

cursor.delete("id = 1")