from Core.databases import Database


class SupplierModel:
    def __init__(self):
        self.db = Database()
        self.db.getConnection()

    def setDataSupplier(self, data):
        try:
            self.db.query("INSERT INTO supplier(name, contact, address, city) VALUES(?, ?, ?, ?)",
                          (str(data[0]), str(data[1]), str(data[2]), str(data[3])))
            return 1
        except ConnectionError:
            return 0

    def getJumlahSupplier(self):
        self.db.query("SELECT COUNT(*) FROM supplier")
        return self.db.select_one()

    def getNameSupplier(self):
        self.db.query("SELECT supplierid, name FROM supplier")
        return self.db.select_all()

    def getDataSupplier(self):
        self.db.query("SELECT * FROM supplier")
        return self.db.select_all()

    def updateDataSupplier(self, data):
        try:
            self.db.query("UPDATE supplier SET name=?, contact=?, address=?, city=? WHERE supplierid=?",
                          (str(data[0]), str(data[1]), str(data[2]), str(data[3]), int(data[4])))
            return 1
        except ConnectionError:
            return 0

    def deleteDataSupplier(self, id):
        self.db.query("DELETE FROM supplier WHERE supplierid=:id", (id,))
