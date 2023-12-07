from DAL.DBConnect import Connection
import mysql.connector
from DTO.account import AccountDTO

class AccountDAL:
    def __init__(self):
        self.db=Connection()

    def login(self, account):
        query = "login"
        params = (account.username, account.password)
        result = self.db.fetch_data(query, params, procedure=True)
        print(result)
        return len(result) > 0