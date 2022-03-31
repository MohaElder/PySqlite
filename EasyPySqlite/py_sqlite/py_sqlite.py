import sqlite3
import os.path

allowed_types=["INTEGER", "TEXT", "BLOB", "NULL", "REAL"]

class PySqlite:
    @staticmethod
    def initDbFromDict(path, name, tbl, overwrite=False):
        if os.path.exists(path + name + ".db") and overwrite == False:
            print("There is already a db! If you want to overwirte it, call initDbFromDict with overwrite = True")
            return True
        cursor = sqlite3.connect("{}{}.db".format(path,name), check_same_thread=False).cursor()
        if name == "" or tbl == "":
            print("empty argument!")
            return False
        creation_string = 'CREATE TABLE ' + name.upper() + ' (ID INT PRIMARY KEY     NOT NULL,'
        for key in tbl:
            if key == "":
                print("empty key!")
                return False
            sq_key = key.upper()
            sq_type = tbl[key].upper()
            if sq_type not in allowed_types:
                print("invalid type!")
            creation_string += '{}          {}    NOT NULL,'.format(sq_key, sq_type)
        creation_string = creation_string[0:-1] + ");"
        cursor.execute(creation_string)
        print("succesfully initialized {}.db !".format(name))
        
        return True