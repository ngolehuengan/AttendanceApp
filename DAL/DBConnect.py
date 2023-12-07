import mysql.connector
class Connection:
    host = "localhost"
    user = "root"
    password = ""
    database = "attendance"
    connection = None

    def __init__(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor(buffered=True)

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_data(self, query, params=None, procedure=False):
        if procedure:
            self.cursor.callproc(query, params)
        else:
            self.cursor.execute(query, params)
        result = []
        for result_set in self.cursor.stored_results():
            result.extend(result_set.fetchall())
        return result

    def __del__(self):
        self.cursor.close()
        self.conn.close()