from DAL.face import FaceDAL

class FaceBLL:
    @staticmethod
    def select_id(id):
        return FaceDAL().select_id(id)

    @staticmethod
    def select_name(id):
        return FaceDAL().select_name(id)

    @staticmethod
    def select_roll(id):
        return FaceDAL().select_roll(id)