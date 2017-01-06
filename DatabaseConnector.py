# -*- coding: utf-8 -*-

''' 檔案資訊
檔名:DataBaseConnector.py
版本:version 1.00
功能:A class to transit data in DataBase
作者:李俊鴻, Neil Lee
時間:2017/1/5
更新紀錄:(最新的在最上面)
	=== Version 1.00 2017/1/5 update ===
	(1)	
作者筆記:
	(1)
'''

import sqlite3
import socket
from datetime import datetime
import time



class DatabaseConnector:
	
	
	#[section]: initial
	def __init__(self, dbName):
		self.ID = "" #loginID
		self.PWD = "" #loginPWD
		self.userAction = "" # "BinToExcel" or "ExcelToBin"
		self.commandSQL = "" # A SQL command string
		self.sourceFilePath = ""
		self.sourceFileName = ""
		self.templateFilePath = ""
		self.templateFileName = ""
		self.resultFilePath = ""
		self.resultFileName = ""
		self.dbName = dbName
		self.dbConnection = None
		self.dbCursor = None
		self.defaultDatabase() # initial DB:"DataConverter"
	
	
	
	#[section]: initial DB environment & connection
	def defaultDatabase(self):		
		self.connectDatabase()	
		self.defaultDatabaseTable() #only for testing
		self.defaultDatabaseData() #only for testing
		self.disConnectDatabase() 
		
	def connectDatabase(self):
		self.dbConnection = sqlite3.connect(self.dbName)
		self.dbCursor = self.dbConnection.cursor()
		
	def disConnectDatabase(self):
		self.dbConnection.commit()
		self.dbConnection.close()
	
	def defaultDatabaseTable(self):
		#default table:UserList
		self.SQLcommand = "CREATE TABLE IF NOT EXISTS UserList ( "
		self.SQLcommand += "UserID VARCHAR(50) NOT NULL, "
		self.SQLcommand += "UserPassword VARCHAR(50) NOT NULL, "
		self.SQLcommand += "UserName NVARCHAR(50) NULL, "
		self.SQLcommand += "UserEmail VARCHAR(60) NULL, "
		self.SQLcommand += "UserGroup VARCHAR(20) NULL, "
		self.SQLcommand += "UserStatus VARCHAR(5) NOT NULL, "
		self.SQLcommand += "PRIMARY KEY (UserID) "
		self.SQLcommand += "); "
		self.dbCursor.execute(self.SQLcommand)
		
		#default table:UserLoginLog
		self.SQLcommand = "CREATE TABLE IF NOT EXISTS UserLoginLog ( "
		self.SQLcommand += "UserID VARCHAR(50) NOT NULL, "
		self.SQLcommand += "UserPassword VARCHAR(50) NOT NULL, "
		self.SQLcommand += "LoginStatus VARCHAR(10) NOT NULL, "
		self.SQLcommand += "LoginIP VARCHAR(10) NOT NULL, "
		self.SQLcommand += "LoginPC VARCHAR(10) NOT NULL, "
		self.SQLcommand += "LoginDateTime VARCHAR(30) NULL "
		self.SQLcommand += "); "
		self.dbCursor.execute(self.SQLcommand)

		#default table:UserActionLog
		self.SQLcommand = "CREATE TABLE IF NOT EXISTS UserActionLog ( "
		self.SQLcommand += "UserID VARCHAR(50) NOT NULL, "
		self.SQLcommand += "UserAction VARCHAR(50) NOT NULL, "
		self.SQLcommand += "SourceFilePath VARCHAR(100) NOT NULL, "
		self.SQLcommand += "SourceFileName VARCHAR(100) NOT NULL, "
		self.SQLcommand += "TemplateFilePath VARCHAR(100) NULL, "
		self.SQLcommand += "TemplateFileName VARCHAR(100) NULL, "
		self.SQLcommand += "ResultFilePath VARCHAR(100) NOT NULL, "
		self.SQLcommand += "ResultFileName VARCHAR(100) NOT NULL, "
		self.SQLcommand += "LogConvertItem VARCHAR(30) NOT NULL, "
		self.SQLcommand += "LogConvertConfig VARCHAR(200) NOT NULL, "
		self.SQLcommand += "LogInputData VARCHAR(200) NULL, "
		self.SQLcommand += "LogOutputData VARCHAR(200) NULL, "
		self.SQLcommand += "LogStatus VARCHAR(5) NOT NULL, "
		self.SQLcommand += "LogMessage VARCHAR(300) NOT NULL, "
		self.SQLcommand += "LogDateTime VARCHAR(30) NULL "
		self.SQLcommand += "); "
		self.dbCursor.execute(self.SQLcommand)
	
	def defaultDatabaseData(self):
		self.SQLcommand = "DELETE FROM UserList; "
		self.dbCursor.execute(self.SQLcommand)
		self.SQLcommand = "INSERT INTO UserList VALUES ('10002002', 'mis', 'NeilLee', 'chunhunglee0329@gmail.com', '', '1'); "
		self.dbCursor.execute(self.SQLcommand)
		
	
	
	
	#[section]: functions
	# validate User Login ID/PWD is True or False
	def validateUserLogin(self, ID, PWD):
		self.ID = ID
		self.PWD = PWD
		self.connectDatabase()
		self.SQLcommand = "SELECT * FROM UserList WHERE UserID='%s' AND UserPassword='%s' " % (self.ID, self.PWD)
		self.dbCursor.execute(self.SQLcommand)
		if self.dbCursor.fetchone() is not None:
			return True
		else:
			return False
		self.disConnectDatabase()
	
	#insert log into table "UserLoginLog"
	def insertUserLoginLog(self, STATUS):
		myPC = socket.gethostname()
		myName = socket.getfqdn(myPC)
		myAddr = socket.gethostbyname(myPC)
		self.connectDatabase()
		self.SQLcommand = "INSERT INTO UserLoginLog VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (self.ID, self.PWD, STATUS, myAddr, myPC, datetime.today())
		self.dbCursor.execute(self.SQLcommand)
		self.disConnectDatabase()		
		
	#insert log into table "UserActionLog"
	def insertUserActionLog(self, Action, SourceFilePath, SourceFileName, TemplateFilePath, TemplateFileName, ResultFilePath, ResultFileName, ConvertItem, ConvertConfig, InputData, OutputData, Status, Message):
		self.connectDatabase()
		self.SQLcommand = "INSERT INTO UserActionLog VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') " % (self.ID, Action, SourceFilePath, SourceFileName, TemplateFilePath, TemplateFileName, ResultFilePath, ResultFileName, ConvertItem, ConvertConfig, InputData, OutputData, Status, Message, datetime.today() )
		self.dbCursor.execute(self.SQLcommand)
		self.disConnectDatabase()		

	
	
	
	
	
		
if __name__ == "__main__":
    DatabaseConnector("AAA", "BBB")
