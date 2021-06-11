from Core.databases import Database


class ProdukModel:

    def __init__(self):
        self.db = Database()
        self.db.getConnection()

    def getJumlahProduk(self):
        self.db.query("SELECT COUNT(*) FROM product")

        return self.db.select_one()

    def getDataProduk(self):
        self.db.query("SELECT productid, supplier.name, productname, quantity, price FROM product INNER JOIN supplier "
                      "ON product.supplierid = supplier.supplierid")

        return self.db.select_all()

    def setDataProduk(self, data):
        try:
            self.db.query("INSERT INTO product(supplierid, productname, quantity, price) VALUES(?, ?, ?, ?)",
                      (int(data[0]), str(data[1]), int(data[2]), int(data[3])))
            return 1
        except ConnectionError:
            return 0

    def deleteDataProduk(self, id):
        self.db.query("DELETE FROM product WHERE productid=:id", (id,))