from Core.databases import Database


class UserModel:
    def __init__(self):
        self.db = Database()
        self.db.getConnection()

    def getOneDataUser(self, params):
        self.db.query("SELECT employeeid, username, password FROM user WHERE username=:username "
                      "and password=:password;", {"username": params[0], "password": params[1], })

        return self.db.select_one()

