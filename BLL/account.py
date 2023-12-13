from DAL.account import AccountDAL

class AccountBLL:
    def checkAccount(self, account):
        return AccountDAL().login(account)