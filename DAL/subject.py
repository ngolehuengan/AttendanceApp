from DAL.DBConnect import Connection

class SubjectDAL:
    def __init__(self):
        self.db=Connection()

    def getId(self, id):
        query = "subj_selectId"
        params = (id,)
        result = self.db.fetch_data(query, params, procedure=True)
        return result if result is not None else []

    def getName(self, id):
        query = "subj_selectName"
        params = (id,)
        result = self.db.fetch_data(query, params, procedure=True)
        return result if result is not None else []