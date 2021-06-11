import sqlite3


class Database:
    con = None
    cursor = None

    def getConnection(self):
        if not self.con:
            print("Database connected")
            self.con = sqlite3.connect("Core/data.db")
            self.cursor = self.con.cursor()

        return self.con

    def query(self, query, params=""):
        self.cursor.execute(query, params)
        self.con.commit()

    def select_all(self):
        return self.cursor.fetchall()

    def select_one(self):
        return self.cursor.fetchone()
