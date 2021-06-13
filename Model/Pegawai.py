from Core.databases import Database


class PegawaiModel:
    def __init__(self):
        self.db = Database()
        self.db.getConnection()

    def getJumlahPegawai(self):
        self.db.query("SELECT COUNT(*) FROM employees")
        return self.db.select_one()

    def getDataPersonPegawai(self, id):
        self.db.query("SELECT firstname, lastname, phonenumber, email, address, city, jabatan FROM employees "
                      "WHERE employeeid=?", (id, ))
        return self.db.select_one()
