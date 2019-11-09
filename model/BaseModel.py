import mysql.connector
import json
from domain.DomainTabla import DomainTabla


class BaseModel:
    def __init__(self, response = None):
        self.response = response


    @staticmethod
    def connect():
        with open('./config/database.json') as f:
            data = json.load(f)

        return mysql.connector.connect(user=data["user"],
                                       password=data["password"],
                                        host=data["host"],
                                        database=data["database"])

    @staticmethod
    def get_config_paths(item=""):
        with open('./config/paths.json') as f:
            data = json.load(f)
            return data[item]

    @staticmethod
    def get_query(query_file):
        querys_path = BaseModel.get_config_paths("querys")
        with open(querys_path+query_file+'.sql', 'r') as myfile:
            query_str = myfile.read()
            return query_str

    def execute_insert(self, stmt, data):
        cnx = BaseModel.connect()

        cursor = cnx.cursor()
        cursor.execute(stmt, data)
        last_row_id = cursor.lastrowid

        cnx.commit()
        cursor.close()
        cnx.close()

        return last_row_id

    def execute_update(self, stmt, data):
        cnx = BaseModel.connect()

        cursor = cnx.cursor()
        cursor.execute(stmt, data)

        cnx.commit()
        cursor.close()
        cnx.close()



    @staticmethod
    def execute_query(stmt, params=None):
        cnx = BaseModel.connect()

        cursor = cnx.cursor(dictionary=True)
        cursor.execute(stmt, params)

        data = cursor.fetchall()

        cursor.close()
        cnx.close()

        return data

    @staticmethod
    def get_single_result(stmt="", script_name="", params=None):
        cnx = BaseModel.connect()

        cursor = cnx.cursor(dictionary=True)
        if len(script_name) > 0:
            stmt = BaseModel.get_query(script_name)

        cursor.execute(stmt, params)

        data = cursor.fetchone()

        cursor.close()
        cnx.close()
        return data

    @staticmethod
    def dict_to_object(obj, data={}):
        for key, value in data.items():
            setattr(obj, key, value)





