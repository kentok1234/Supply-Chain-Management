from Core.databases import Database


class PegawaiModel:
    def __init__(self):
        self.db = Database()
        self.db.getConnection()

    def getJumlahPegawai(self):
        self.db.query("SELECT COUNT(*) FROM employees")
        return self.db.select_one()
