
import pymysql

def getdb():
    mydb = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = 'dbuser',
        password = 'qwer321',
        db = 'mydatabase'
    )
    # mydb = mysql.connector.connect(
    #     host = '40.2.195.1',
    #     port = '3306',
    #     user = 'cmbcdbop',
    #     password = '1qaz@WSX',
    #     database = 'paasdb'
    # )
