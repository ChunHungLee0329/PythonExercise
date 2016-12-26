# -*- coding: utf-8 -*-

''' 檔案資訊
檔名:BinExcelConverter.py
版本:version 1.00
功能:A class to process BinToExcel and ExcelToBin
作者:李俊鴻, Neil Lee
時間:2016/12/26
更新紀錄:
	(1)Version 1.00: create class BinExcelConverter
'''

import datetime
import math
import pkgutil
import binascii
import bitstring
import win32com.client
import os
from bitstring import BitArray, BitStream
from shutil import copyfile

class BinExcelConverter:
	
	def __init__(self, i, t):
		self.i = i #inputPath
		self.t = t #templatePath
		self.convertingItem = "" #current converting Item:ExcelToBin/BinToExcel
		self.supportFileExtension = { 
			'xls':'Excel', 'csv':'Excel', 'xlsx':'Excel',
			'bin':'Bin'				
															} #supported file name extension
		self.supportConvertingItem = ["ExcelToBin", "BinToExcel"] #supported Converting Item
		self.status = 1 #keep the status (1=ok ; 9=error)
		self.message = "" #keep the message
		self.state = "" #keep the state
		self.tempFolder = os.getcwd() + "\\tempData\\" #tempFolder to process data
		self.dataContent = "" #reading file to string from "readFileToString()"
		self.resultPath = os.getcwd() + "\\resultData\\" #resultFolder to save file
	
	#check the inputPath/templatePath match the supportFileExtension 
	def volidateFileExtension(self):
		#search supportFileExtension to volidate the filename extension of inputPath/templatePath
		if(self.i.split('.')[1] and self.t.split('.')[1] in self.supportFileExtension):
			return True
		else:
			self.status = 9
			if(self.i.split('.')[1] not in self.supportFileExtension):
				self.message += "system doesn't support: " + "." + self.i.split('.')[1] + "\n"
			if(self.t.split('.')[1] not in self.supportFileExtension):
				self.message += "system doesn't support: " + "." + self.t.split('.')[1] + "\n"
			return False	
	
	#check the Data Converting request support or not
	def volidateConvertingItem(self):
		#ConvertingItem=ExcelToBin
		i_Type = self.supportFileExtension[self.i.split('.')[1]] #get input file type (Excel/Bin)
		t_Type = self.supportFileExtension[self.t.split('.')[1]] #get template file type (Excel/Bin)
		self.convertingItem = i_Type + "To" + t_Type #assign converting Item: ExcelToBin/BinToExcel
		if(self.convertingItem in self.supportConvertingItem):
			return True
		else:
			self.status = 9
			self.message += "system doesn't support converting: " + self.convertingItem + "\n"
			self.convertingItem = ""			
			return False
	
	#check the inputPath/templatePath data exist or not
	def volidateFilePath(self):
		if(os.path.exists(self.i) and os.path.exists(self.t)): #validate inputFilePath/outputFilePath
			return True
		else:
			if(not os.path.exists(self.i)):
				self.message += "system doesn't find the FilePath: " + self.i + "\n"
			if(not os.path.exists(self.t)):
				self.message += "system doesn't find the FilePath: " + self.t + "\n"
			return False
	
	#copy file to tempFolder:tempData
	def copyAsTempData(self):
		if(self.i == self.i): #copy inputFile into tempFolder(tempData) and reset self.i			
			copyfile(self.i, self.tempFolder + self.i.split('\\')[-1])
			self.i = self.tempFolder + self.i.split('\\')[-1]
		if(self.t == self.t): #copy templateFile into tempFolder(tempData) and reset self.t			
			copyfile(self.t, self.tempFolder + self.t.split('\\')[-1])
			self.t = self.tempFolder + self.t.split('\\')[-1]
	
	#read input File as a serial sequence of string value
	def readFileToString(self):
		if(self.convertingItem == "BinToExcel"): #read a "Bin" file
			OpenFile = open(self.i, 'rb')
			self.dataContent = BitArray(OpenFile,length=256)
		elif(self.convertingItem == "ExcelToBin"): #read a "Excel" file
			RowIndex = 2
			RowMax = 65536
			xlApp = win32com.client.Dispatch("Excel.Application")
			workbook = xlApp.Workbooks.Open(self.i)
			while(RowIndex<RowMax):
				if (xlApp.Range("C"+str(RowIndex),"C"+str(RowIndex)).Text == ""):
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
		self.resultPath = self.resultPath + tempFileName + "_result_" + strDateTime + "." + tempFileExtension
		if(self.convertingItem == "BinToExcel"): #convert to Excel
			self.binToExcel()
		elif(self.convertingItem == "ExcelToBin"): #convert to Bin
			self.excelToBin()
		#self.deleteTempData()
	
	def binToExcel(self):
		xlApp = win32com.client.Dispatch("Excel.Application")
		workbook = xlApp.Workbooks.Open(self.t)
		RowIndex = 2
		CurrentBit = 0
		BitRange = 0
		while(CurrentBit<int(len(self.dataContent))):
			BitRange = int(xlApp.Range("B"+str(RowIndex),"B"+str(RowIndex)).Value)	
			xlApp.Range("C"+str(RowIndex),"C"+str(RowIndex)).Value = self.dataContent[CurrentBit:CurrentBit+BitRange].bin					
			CurrentBit = CurrentBit + BitRange	
			RowIndex=RowIndex+1
		workbook.SaveAs(self.resultPath)
		xlApp.DisplayAlerts = 0
		xlApp.Visible = 0
		workbook.Close(0)
	
	def excelToBin(self):
		#excel string to Array
		self.readFile()
		HexArray=[]
		Index=0
		while(Index<len(self.dataContent)):
			HexArray.append(hex(int((self.dataContent)[Index:Index+8],2)))
			Index=Index+8
		#write to bin file
		with open(self.resultPath, 'wb') as f:
			f.write(bytearray(int(i, 16) for i in HexArray))	
	
	def deleteTempData(self):
		print ""
	
	#have a operation log and write into a text file
	def log(self):
		print "log"
	