from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import sqlite3

class FuelDatabase():
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QSLITE")
        self.db.setDatabaseName("fuel_finder.db")
        self.db.open()
        
    def create_tables(self):
        sql_list = ["""CREATE TABLE fuelStation(stationID integer, stationGPS text, stationPostcode text, owner text, primary key(stationID))""",
                    """CREATE TABLE user(userID integer, userName text, password text, userAddress1 text, userAddress2 text, userAddress3 text, userPostcode text, primary key(userID))""",
                    """CREATE TABLE owner(ownerID integer, ownerName text, primary key(ownerID))""",
                    """CREATE TABLE fuelType(fuelType text, primary key(fuelType))""",
                    """CREATE TABLE priceTable(priceReading real, primary key(priceReading))"""
                    ]
        with sqlite3.connect("fuel_finder.db") as db:
            cursor = db.cursor()
            for each in sql_list:
                cursor.execute(each)
            db.commit()

    def test_query(self):
        sql = """INSERT INTO fuelStation(stationGPS, stationPostcode, owner) values("24,24", "CB4 2US", "tesco")"""
        with sqlite3.connect("fuel_finder.db") as db:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
        

    


    
    
if __name__ == "__main__":
    database = FuelDatabase()
    database.test_query()
