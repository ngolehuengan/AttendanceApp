from tkinter import StringVar
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

    def execute_query(self, query, params=None, procedure=False):
        try:
            if params is None:
                params = []
            params = [value.get() if isinstance(value, StringVar) else value for value in params]
            if procedure:
                self.cursor.callproc(query, params)
            else:
                self.cursor.execute(query, params)

            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")

    def fetch_data(self, query, params=None, procedure=False):
        try:
            if params is None:
                params = []

            if procedure:
                self.cursor.callproc(query, params)
            else:
                self.cursor.execute(query, params)
            result = []
            for result_set in self.cursor.stored_results():
                result.extend(result_set.fetchall())

            return result
        except mysql.connector.Error as err:
            print(f"Error fetching data: {err}")
            return []

    def insert(self, query, params=None, procedure=False):
        self.execute_query(query, params, procedure)

    def __del__(self):
        self.cursor.close()
        self.conn.close()