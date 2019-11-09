import mysql.connector
import json


def connect():
    with open('./config/database.json') as f:
        data = json.load(f)

    return mysql.connector.connect(user=data["user"],
                                   password=data["password"],
                                   host=data["host"],
                                   database=data["database"])

cnx = connect()
cnx.close()
print(cnx)

