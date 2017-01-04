# -*- coding: utf-8 -*-

''' 檔案資訊
檔名:BinExcelConverter.py
版本:version 1.00
功能:A class to process BinToExcel and ExcelToBin
作者:李俊鴻, Neil Lee
時間:2016/12/26
更新紀錄:(最新的在最上面)
	=== Version 1.03 2017/1/4 updae ===
	(1)replace class file from "BinExcelConverter.py" to "BinExcelConverter_final.py"
	(2)add config dynamic function to determine excel column.
	=== Version 1.02 2016/12/29 update ===
	(1)modify "writeLog()" to have success & failed message.	
	(2)new function "validationEncapsulation()" to encapsulate validation process.
	(3)new function "convertingEncapsulation()" to encapsulate convert process.
	(4)enhance validation of mistake operation process, and add into error messag
	(5)cowork eMow to find bug: "binToExcel()" failure root cause.
	=== Version 1.01 2016/12/28 update ===
	(1)add function "checkSetting()" to check/create program default folder
	(2)add function "validateVariable()" to check dummy data input
	=== Version 1.00 2016/12/26 update ===
	(1)create class BinExcelConverter	
作者筆記:
	(1)reading/write Excel column from loading Config.ini to decide which sheet/column
	(2)wriet log needs enhancement, even apply "sqlite" and "Pandas"
'''

import datetime
import math
import pkgutil
import binascii
import bitstring
import win32com.client
import os
import ConfigParser
from bitstring import BitArray, BitStream
from shutil import copyfile




class BinExcelConverter:
	
	
	#[section]: initial
	def __init__(self, s, t):
		self.s = s #sourcePath
		self.t = t #templatePath
		self.tempFolder = os.getcwd() + "\\tempData\\" #tempPath to process data
		self.resultFolder = os.getcwd() + "\\resultData\\" #resultFolder to save file
		self.logFolder = os.getcwd() + "\\logData\\" #logFolder to save user log
		self.supportFileExtension = { 
			'xls':'Excel', 'csv':'Excel', 'xlsx':'Excel',
			'bin':'Bin'
															} #supported file name extension
		self.supportConvertingItem = ["ExcelToBin", "BinToExcel"] #supported Converting Item
		self.convertingItem = "" #current converting Item:ExcelToBin/BinToExcel	
		self.dataContent = "" #reading file to string from "readFileToString()"
		self.status = 1 #keep the status (1=ok ; 9=error)
		self.message = "" #keep the message
		self.state = "" #keep the state
		self.configExcelSetting = ""
		self.defaultProgramSetting() #check program default setting

	
	
	#[section]: validation/setting
	#check program default setting
	def defaultProgramSetting(self):
		config = ConfigParser.RawConfigParser()
		config.read('Config.ini')
		#default system folders
		sectionDefaultFolder = config.items("DefaultSettingFolder")
		for item in sectionDefaultFolder:
			if not os.path.isdir(os.getcwd()+"\\"+item[1]):
				os.mkdir(os.getcwd()+"\\"+item[1])
		#defaut dynamic variable
		if(self.configExcelSetting==""):
			self.configExcelSetting = "ExcelSetting_Default"
		sectionDefaultExcelSetting = config.items(self.configExcelSetting)
		for item in sectionDefaultExcelSetting:
			setattr(self, item[0], item[1])
		print self.templatecolvalue
		
	
	

	#encapsulate validation functions:	
	def validationEncapsulation(self):
		validationResult = False
		#start convertion after validation
		if(self.validateVariable()): #validate if input/template missing
			if(self.validateFileExtension()): #validate file name extension
				if(self.validateConvertingItem()): #validate converting item(BinToExcel/ExcelToBin)
					if(self.validateFilePath()): #validate file existence (sourcePath/templatePath)
						validationResult = True
		return validationResult
	
	#check the sourcePath/templatePath missing text.
	def validateVariable(self):
		if(len(self.s) == 0):
			self.status = 9
			self.message += "miss data input: Source file path \n "
			return False
		elif(len(self.t) == 0):
			self.status = 9
			self.message += "miss data input: Template file path \n "
			return False
		else:
			return True
			
	#check the sourcePath/templatePath match the supportFileExtension 
	def validateFileExtension(self):
		#search supportFileExtension to validate the filename extension of sourcePath/templatePath
		if(self.s.split('.')[1] and self.t.split('.')[1] in self.supportFileExtension):
			return True
		else:
			self.status = 9
			if(self.s.split('.')[1] not in self.supportFileExtension):
				self.message += "system doesn't support file name extension: " + "." + self.s.split('.')[1] + "\n"
			if(self.t.split('.')[1] not in self.supportFileExtension):
				self.message += "system doesn't support file name extension: " + "." + self.t.split('.')[1] + "\n"
			return False	
	
	#check the Data Converting request support or not
	def validateConvertingItem(self):
		#ConvertingItem=ExcelToBin
		i_Type = self.supportFileExtension[self.s.split('.')[1]] #get input file type (Excel/Bin)
		t_Type = self.supportFileExtension[self.t.split('.')[1]] #get template file type (Excel/Bin)
		self.convertingItem = i_Type + "To" + t_Type #assign converting Item: ExcelToBin/BinToExcel
		if(self.convertingItem in self.supportConvertingItem):
			return True
		else:
			self.status = 9
			self.message += "system doesn't support converting: " + self.convertingItem + "\n"
			self.convertingItem = ""			
			return False	
	
	#check the sourcePath/templatePath data exist or not
	def validateFilePath(self):
		if(os.path.exists(self.s) and os.path.exists(self.t)): #validate inputFilePath/outputFilePath
			return True
		else:
			if(not os.path.exists(self.s)):
				self.status = 9
				self.message += "system doesn't find the FilePath: " + self.s + "\n"
			if(not os.path.exists(self.t)):
				self.status = 9
				self.message += "system doesn't find the FilePath: " + self.t + "\n"
			return False
	
	
	
	
	#[Section]: data processing functions
	#encapsulate convertion functions
	def convertingEncapsulation(self):
		self.copyAsTempData()
		self.readFileToString()
		self.convert()
		self.writeLog()
	#copy file to tempFolder:tempData
	def copyAsTempData(self):
		self.s = self.s.replace('/','\\')
		self.t = self.t.replace('/','\\')
		#copy inputFile into tempFolder(tempData) and reset self.s			
		copyfile(self.s, self.tempFolder + self.s.split('\\')[-1])
		self.s = self.tempFolder + self.s.split('\\')[-1]
		#copy templateFile into tempFolder(tempData) and reset self.t			
		copyfile(self.t, self.tempFolder + self.t.split('\\')[-1])
		self.t = self.tempFolder + self.t.split('\\')[-1]	
	
	#read input File as a serial sequence of string value
	def readFileToString(self):
		sheet = self.sourcesheet
		colValue = self.sourcecolvalue
		if(self.convertingItem == "BinToExcel"): #read a "Bin" file
			OpenFile = open(self.s, 'rb')
			self.dataContent = BitArray(OpenFile,length=256)
		elif(self.convertingItem == "ExcelToBin"): #read a "Excel" file
			RowIndex = 2
			RowMax = 65536
			xlApp = win32com.client.Dispatch("Excel.Application")
			workbook = xlApp.Workbooks.Open(self.s)
			while(RowIndex<RowMax):
				if (xlApp.Range(colValue+str(RowIndex),colValue+str(RowIndex)).Text == ""):
					RowIndex = RowMax
				else:
					self.dataContent=self.dataContent+xlApp.Range("C"+str(RowIndex),"C"+str(RowIndex)).Text
				RowIndex=RowIndex+1
			xlApp.DisplayAlerts = 0
			xlApp.Visible = 0
			workbook.Close(0)	
	
	#main funciton:convert, getting "self.dataContent" to generate Bin/Excel file
	def convert(self):		
		tempFile = self.t.split('\\')[-1]
		tempFileName = tempFile.split('.')[0]
		tempFileExtension = tempFile.split('.')[1]
		strDateTime = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
		self.resultFolder = self.resultFolder + tempFileName + "_result_" + strDateTime + "." + tempFileExtension
		if(self.convertingItem == "BinToExcel"): #convert to Excel
			self.binToExcel()
		elif(self.convertingItem == "ExcelToBin"): #convert to Bin
			self.excelToBin()
		#message
		self.message = "Finish the job, please check below path:\n"
		self.message += self.resultFolder + '\n'
		self.message += "soucePath:\n" + self.s + "\n"
		self.message += "templatePath:\n" + self.t + "\n"
		#self.deleteTempData()
	
	def binToExcel(self):
		sheet = self.templatesheet
		colValue = self.templatecolvalue
		colBits = self.templatecolbits
		xlApp = win32com.client.Dispatch("Excel.Application")
		workbook = xlApp.Workbooks.Open(self.t)
		RowIndex = 2
		CurrentBit = 0
		BitRange = 0
		while(CurrentBit<int(len(self.dataContent))):
			BitRange = int(xlApp.Range(colBits+str(RowIndex),colBits+str(RowIndex)).Value)	
			xlApp.Range(colValue+str(RowIndex),colValue+str(RowIndex)).Value = self.dataContent[CurrentBit:CurrentBit+BitRange].bin					
			CurrentBit = CurrentBit + BitRange	
			RowIndex=RowIndex+1
		workbook.SaveAs(self.resultFolder)
		xlApp.DisplayAlerts = 0
		xlApp.Visible = 0
		workbook.Close(0)	
	
	def excelToBin(self):
		#excel string to Array
		HexArray=[]
		Index=0
		while(Index<len(self.dataContent)):
			HexArray.append(hex(int((self.dataContent)[Index:Index+8],2)))
			Index=Index+8
		#write to bin file
		with open(self.resultFolder, 'wb') as f:
			f.write(bytearray(int(i, 16) for i in HexArray))	
	
	#backup sourcePath/templatePath file from tempData to backupData then delete it
	def backupData(self):
		print ""
		
	#have a operation log and write into a text file
	def writeLog(self):
		strDateTime = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
		fileName = "userLog_" + strDateTime + ".txt"
		self.logFolder = self.logFolder + fileName
		with open(self.logFolder, 'wb') as f:
			f.write(self.message)	
	
	
	
	#system log in function
	def login(self):
		return True