import mysql.connector
from mysql.connector import Error
from ..utils.logger import *
    
class Database:
    def __init__ (self,host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                log_setup("Connected to MariaDB database")
        except Error as e:
            log_error(f"Error: {e}, have you created the database ?")
            self.connection = None
            
    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            log_setup("Disconnected from MariaDB database")

    def query(self, query, params=None):
            cursor = None
            try:
                cursor = self.connection.cursor()
                cursor.execute(query, params)
                if query.strip().upper().startswith("SELECT"):
                    results = cursor.fetchall()
                    log_msg(f"Query : {query} | results : {results}")
                    return results
                else:
                    self.connection.commit()
                    log_msg("Query executed successfully")
                    return []
            except Error as e:
                log_error(f"Failed to execute query: {e}")
                return []
            finally:
                if cursor:
                    cursor.close()



