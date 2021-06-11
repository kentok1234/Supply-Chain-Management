from Core.databases import Database


class SupplierModel:
    def __init__(self):
        self.db = Database()
        self.db.getConnection()

    def getNameSupplier(self):
        self.db.query("SELECT supplierid, name FROM supplier")
        return self.db.select_all()
