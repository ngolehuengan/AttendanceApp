from DAL.subject import SubjectDAL

class SubjectBLL:
    @staticmethod
    def getId(id):
        return SubjectDAL().getId(id)

    @staticmethod
    def getName(id):
        return SubjectDAL().getName(id)