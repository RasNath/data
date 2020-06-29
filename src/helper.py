# define method to pull data from spreadsheet
def get_spreadsheet_data(sheet_name, worksheet_index):
    sheet = client.open(sheet_name).get_worksheet(worksheet_index)
    return sheet.get_all_values()[1:]

def preserve_null_values(list_name):
    print('Preserving NULL values...')
    for x in range(len(list_name)):
        for y in range(len(list_name[x])):
            if list_name[x][y] == '':
                list_name[x][y] = None
    print('NULL values preserved.')
    
# define method to write list of data to MySQL table
def write_to_mysql_table(sql_data, table_name):
    try:
        connection = mysql.connector.connect(
                user       = mc.user,
                password   = mc.password,
                host       = mc.host,
                database   = mc.database
            )
        sql_drop = " DROP TABLE IF EXISTS {} ".format(table_name)
        sql_create_table = """CREATE TABLE {}
                ( FK INT(11),
                  level INT(11),
                  FOREIGN KEY (FK) REFERENCES table1(PK)
                )""".format(table_name)
 
        sql_insert_statement = """INSERT INTO {}
                ( FK,
                  level
                   )
        VALUES ( %s,%s )""".format(table_name)
        cursor = connection.cursor()
        #cursor.execute(sql_drop)
        print('Table {} has been dropped'.format(table_name))
        cursor.execute(sql_create_table)
        print('Table {} has been created'.format(table_name))
        for i in sql_data:
            cursor.execute(sql_insert_statement, i)
        connection.commit()
        print("Table {} successfully updated.".format(table_name))
    except mysql.connector.Error as error :
        connection.rollback()
        print("Error: {}. Table {} not updated!".format(error, table_name))
    finally:
        cursor.execute('SELECT COUNT(*) FROM {}'.format(table_name))
        rowCount = cursor.fetchone()[0]
        print(table_name, 'row count:', rowCount)
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")
            
# update data in MySQL table
def update_mysql_table(sql_data, table_name):
# we are using a try/except block (also called a try/catch block in other languages) which is good for error handling. It will "try" to execute anything in the "try" block, and if there is an error, it will report the error in the "except" block. Regardless of any errors, the "finally" block will always be executed.
    try:
# Here we include the connection credentials for MySQL. We create a connection object that we pass the credentials to, and notice that we specify the database (which from the mysqlcreds.py file tells us that we will be using the qa_db database so we won't need to include that in any code when executing any MySQL statements
        connection = mysql.connector.connect(
                user       = mc.user,
                password   = mc.password,
                host       = mc.host,
                database   = mc.database
            )
 
        sql_insert_statement = """INSERT INTO {}
                ( Column1,
                  Column2,
                  Column3 )
        VALUES ( %s,%s,%s )""".format(table_name)
        cursor = connection.cursor()
        for i in sql_data:
            cursor.execute(sql_insert_statement, i)
        connection.commit()
        print("Table {} successfully updated.".format(table_name))
    except mysql.connector.Error as error :
        connection.rollback()
        print("Error: {}. Table {} not updated!".format(error, table_name))
    finally:
        cursor.execute('SELECT COUNT(*) FROM {}'.format(table_name))
        rowCount = cursor.fetchone()[0]
        print(table_name, 'row count:', rowCount)
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")