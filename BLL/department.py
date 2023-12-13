from DAL.department import DepartmentDAL

class DepartmentBLL:
    @staticmethod
    def getAll():
        return DepartmentDAL().getAll()

    @staticmethod
    def getName(id):
        return DepartmentDAL().getName(id)