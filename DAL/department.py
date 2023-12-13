from DAL.DBConnect import Connection

class DepartmentDAL:
    def __init__(self):
        self.db=Connection()

    def getAll(self):
        query = "dep_select"
        result = self.db.fetch_data(query, None, procedure=True)
        return result if result is not None else []

    def getName(self, id):
        query = "dep_selectById"
        params = (id,)
        result = self.db.fetch_data(query, params, procedure=True)
        return result if result is not None else []