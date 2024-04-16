# Module opens connection to cisdbss.pcc.edu, gets data from database, closes connection

import pyodbc

class Database:
    __connection = None

# Opens connection to database
    @classmethod
    def connect(cls):
        if cls.__connection is None:
            server = 'tcp:cisdbss.pcc.edu'
            database = 'NAMES'
            username = '275student'
            password = '275student'
            cls.__connection = pyodbc.connect(
                'DRIVER={SQL Server};SERVER=' + server
                + ';DATABASE=' + database
                + ';UID=' + username + ';PWD=' + password
            )

# Closes connection to database
    @classmethod
    def close(cls):
        cls.__connection.close()
        cls.__connection = None

# Calls connection to database
# Embeds SQL commands (with parameter binding) to fetch Name, NameCount, Gender, Year
# Restricted by user input name & sex
# Calls to close connection
# Returns data with all 4 attributes
    @classmethod
    def readNames(cls, name, sex):
        from name import Name
        Database.connect()
        cursor = cls.__connection.cursor()
        cursor.execute("""SELECT Name, NameCount, Gender, Year, Total, Rank
        FROM names 
        JOIN name_counts ON names.NameID = name_counts.FK_NameID 
        JOIN year_gender_totals ygt ON name_counts.FK_YearGenderTotalID = ygt.YearGenderTotalID 
        WHERE (Name = ? and Gender = ?);""",name, sex)

  # puts each name object in list, returns
        name_data = []
        name = cursor.fetchone()
        while name:
            name_data.append(Name(name[0], name[1], name[2], name[3], name[4], name[5]))
            name = cursor.fetchone()
        return name_data