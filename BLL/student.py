from DAL.student import StudentDAL

class StudentBLL:
    @staticmethod
    def insert(student):
        return StudentDAL().insert(student)

    @staticmethod
    def update(student):
        return StudentDAL().update(student)

    @staticmethod
    def delete(id):
        return StudentDAL().delete(id)

    @staticmethod
    def show():
        return StudentDAL().show()