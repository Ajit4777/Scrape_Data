import mysql.connector

""" 
For SQL Connection
------------------
Parameters
----------
    -host
    -user
    -password
    -database name
    -password format
"""

class DbConnection():
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mindfire@1",
        database="product_database",
        auth_plugin='mysql_native_password'
        )

        self.mycursor = self.mydb.cursor()
    def get_db_link(self):
        return self.mycursor
    def get_my_db(self):
        return self.mydb

""" 
For Upload Data into database
------------------
Parameters
----------
    -sql querry
    -upload data value
"""
class SendData():
    def __init__(self):
        self.my_db = DbConnection()
        self.db_link = self.my_db.get_db_link()

    '''
    For Upload Data 
    ---------------
    Parameters 
    ----------
        - sql querry
        - value
    '''
    def upload_data(self,sql,val):
        self.db_link.executemany(sql, val)
    ''' 
    commit after upoloadin data into database
    '''
    def commint_db(self):
        self.db_commit = self.my_db.get_my_db()
        self.db_commit.commit()


