from DAL.DBConnect import Connection

class FaceDAL:
    def __init__(self):
        self.db=Connection()

    def select_id(self, id):
        query = "face_id"
        params = (id,)
        result = self.db.fetch_data(query, params, procedure=True)
        return result[0][0] if result else None

    def select_name(self, id):
        query = "face_name"
        params = (id,)
        result = self.db.fetch_data(query, params, procedure=True)
        return result[0][0] if result else None

    def select_roll(self, id):
        query = "face_roll"
        params = (id,)
        result = self.db.fetch_data(query, params, procedure=True)
        return result[0][0] if result else None