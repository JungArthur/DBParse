# import py_parse
import pyodbc

def sql_select(objName):

    return_value = None
    try:
        cursor = DB_Connection.getInstance().cnxn.cursor()
        # 'DI_FN_EG_MI_GetStoredProcedureParameters'
        # Sample select query
        rows = cursor.execute(f"""
        SELECT TOP 1 A.DEFINITION AS CONTENTS -- 내용
          FROM SYS.SQL_MODULES A WITH (NOLOCK)
          LEFT JOIN SYS.OBJECTS B WITH (NOLOCK) ON A.OBJECT_ID = B.OBJECT_ID
         WHERE B.Name = '{objName}'
         ORDER BY TYPE, NAME
        """)

        row = cursor.fetchone()
        while row:
            # print(row[0])
            return_value = row[0]
            row = cursor.fetchone()

        # # Sample select query
        # for obj in rows:
        #     return_value = obj
        # # cursor Close

        cursor.close()
    except Exception as ex:
        print(ex)
    finally:
        # Connection Close
        return return_value

class DB_Connection:
    __instance = None
    # Connection
    cnxn = None

    @staticmethod
    def getInstance():
        if DB_Connection.__instance == None:
            DB_Connection()
        return DB_Connection.__instance

    def __init__(self):
        if DB_Connection.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            # server = 'tcp:myserver.database.windows.net'
            server = 'tcp:*.*.org'
            database = '*'
            username = '*'
            password = '*'
            self.cnxn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

            how_many = self.cnxn.getinfo(pyodbc.SQL_MAX_CONCURRENT_ACTIVITIES)
            print(f'SQL_MAX_CONCURRENT_ACTIVITIES : {how_many}')

            DB_Connection.__instance = self

    def __del__(self):
        self.cnxn.close()
