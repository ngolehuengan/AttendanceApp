from DAL.DBConnect import Connection

class StudentDAL:
    def __init__(self):
        self.db=Connection()

    def insert(self, student):
        query = "InsertStudent"
        params = (
            student.subject_id,
            student.year,
            student.semester,
            student.class_name,
            student.id_student,
            student.name,
            student.gender,
            student.dob,
            student.email,
            student.phone,
            student.address,
            student.teacher,
            student.photo
        )
        self.db.insert(query, params, procedure=True)

    def update(self, student):
        query = "UpdateStudent"
        params = (
            student.subject_id,
            student.year,
            student.semester,
            student.class_name,
            student.id_student,
            student.name,
            student.gender,
            student.dob,
            student.email,
            student.phone,
            student.address,
            student.teacher,
            student.photo
        )
        self.db.execute_query(query, params, procedure=True)

    def delete(self,id):
        query = "DeleteStudent"
        params = (id,)
        self.db.execute_query(query, params, procedure=True)

    def show(self):
        query = "info"
        result = self.db.fetch_data(query, None, procedure=True)
        return result if result is not None else []