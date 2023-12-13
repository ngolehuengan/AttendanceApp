from DAL.DBConnect import Connection

class AccountDAL:
    def __init__(self):
        self.db=Connection()

    def login(self, account):
        query = "login"
        params = (account.username, account.password)
        result = self.db.fetch_data(query, params, procedure=True)
        return len(result) > 0