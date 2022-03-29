# @Time    : 2021/6/24 12:38 AM
# @Author  : Yasushi Oh
# @File    : py_cursor.py

"""main.py

    This file provides backend server functionality 
    for Self-Reliance Portal. It mainly handles user 
    login, regstration, and other operations involving 
    the database. It also handles some OSS related stuff.

"""

'''Dependencies:
    sqlite3,
    threading 
'''

import sqlite3
import threading

class PyCursor:
    """PyCursor

    Purpose: Cursor class wraps the sqlite library
        for client to perform database operations more 
        easily.

    Fields:
        db_name: the name of the cursor to operate at first
    """
    connection = None  # sqlite connection
    cursor = None  # sqlite cursor
    db_path = None  # active database's path

    def __init__(self, sqlite_path, db_path):
        """Initializes the cursor.

        Initializes the cursor by initializing db_path and
            calling connect with db_path.

        Args:
            db_name: the database's name to connect.

        Returns:
            None

        Raises:
            None
        """

        self.db_path = db_path
        self.sqlite_path = sqlite_path

        print("Successfully initialized with sqlite_path: " + sqlite_path + " and db path: " + db_path)

        self.connect()

    def connect(self):
        """connects the cursor to another database

        connects the cursor to another database by reinitializing
            the sqlite connection and cursor

        Args:
            db_name: the database's name to initialize

        Returns:
            None

        Raises:
            Error: db name not found!
        """
        try:
            self.connection = sqlite3.connect(
                self.sqlite_path + self.db_path, check_same_thread=False)
            self.cursor = self.connection.cursor()
        except:
            print("db path not found!")

    def run(self, command):
        """runs a command in the database

        runs a command in the database and
            commits it

        Args:
            command: the command to execute

        Returns:
            None

        Raises:
            Error: database execution errors, probably related with command.
        """
        lock = threading.Lock()  # threading.lock() added to prevent recursive use of cursor error
        try:
            lock.acquire(True)
            self.cursor.execute(command)
            self.connection.commit()
        finally:
            lock.release()

    def get(self, condition):
        """get one record from the database according
            to the condition

        Args:
            condition: the condition to execute

        Returns:
            the found record

        Raises:
            Error: database execution errors, probably related with command.
        """
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.cursor.execute(
                "SELECT * FROM " + self.db_name + " WHERE (" + condition + ")"
            )
        finally:
            lock.release()
            return self.cursor.fetchone()

    def getAll(self, condition=""):
        """gets all records in the database

        Args:
            condition(optional): the condition to execute,


        Returns:
            None

        Raises:
            Error: database execution errors, probably related with command.
        """

        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.cursor.execute(
                "SELECT * FROM " +
                self.db_name +
                (" WHERE " if condition != "" else "") +
                condition
            )
        finally:
            lock.release()
            return self.cursor.fetchall()

    def delete(self, condition):
        """deletes the record according to the condition

        Args:
            condition: the condition to execute,


        Returns:
            None

        Raises:
            Error: database execution errors, probably related with command.
        """
        # delete the record only when it exists in the db
        self.run(
            "DELETE FROM " +
            self.db_name +
            " WHERE EXISTS (SELECT * FROM " +
            self.db_name +
            " WHERE " +
            condition +
            ") AND " +
            condition)
        return "Deleted"

    def insert(self, prop, values):
        """inserts into the record with with desired column and value

        Args:
            prop: the columns to insert(e.g: name, sex, age)

            values: the values to insert(e.g: calen, male, 19)


        Returns:
            <string>success

        Raises:
            Error: prop not found or value invalid
        """
        self.run("INSERT INTO " + self.db_name + " (" + prop + ") " +
                 "VALUES (" + values + ")")
        return "Success"

    def update(self, condition, values):
        """updates the record with with desired condition and values

        Args:
            condition: the condition to execute

            values: the values to insert(e.g: calen, male, 19)


        Returns:
            <string>success

        Raises:
            Error: value invalid or condition error or condition not found
        """
        self.run("UPDATE " + self.db_name + " SET " +
                 values + " WHERE " + condition)
        return "success"