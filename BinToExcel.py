# coding=UTF-8

import math
import pkgutil
import binascii
import bitstring
import win32com.client
import os
from bitstring import BitArray, BitStream

#basic setting:
FileName = "hexfile.bin" 
TemplateExcel = "BinToExcel_template.xls"
OutputExcel = "BinToExcel_result.xls"
MainPath = "c:" + os.sep + "python27" + os.sep   #change folder to c:\python27
GetString=""
GetArray=[]

#functions
def GenerateExcel(path, template, data, newfile):
	#get the path folder to find the excel template. 
	#Using the data to fill up the excel to save as the new name from newfile
	xlApp = win32com.client.Dispatch("Excel.Application")
	workbook=xlApp.Workbooks.Open(os.path.join(path, template))
	RowIndex = 2
	CurrentBit = 0
	BitRange = 0
	while(CurrentBit<int(len(data))):
		BitRange = int(xlApp.Range("B"+str(RowIndex),"B"+str(RowIndex)).Value)
		xlApp.Range("C"+str(RowIndex),"C"+str(RowIndex)).Value = data[CurrentBit:CurrentBit+BitRange].bin
		CurrentBit = CurrentBit + BitRange	
		RowIndex=RowIndex+1
	CheckExcelData(int(len(data)), xlApp)
	workbook.SaveAs(os.path.join(path, newfile))
	xlApp.DisplayAlerts = 0
	xlApp.Visible = 0
	workbook.Close(0)
	
def GenerateExcel(path, template, source_type, data, newfile):
	#get the path folder to find the excel template. 
	#Using the data to fill up the excel to save as the new name from "newfile"
	xlApp = win32com.client.Dispatch("Excel.Application")
	workbook=xlApp.Workbooks.Open(os.path.join(path, template))
	RowIndex = 2
	CurrentBit = 0
	BitRange = 0
	while(CurrentBit<int(len(data))):
		BitRange = int(xlApp.Range("B"+str(RowIndex),"B"+str(RowIndex)).Value)
		if source_type=="GetArray":
			xlApp.Range("C"+str(RowIndex),"C"+str(RowIndex)).Value = data[CurrentBit:CurrentBit+BitRange].bin
		if source_type=="GetString":
			xlApp.Range("C"+str(RowIndex),"C"+str(RowIndex)).Value = data[CurrentBit:CurrentBit+BitRange]			
		CurrentBit = CurrentBit + BitRange	
		RowIndex=RowIndex+1
	CheckExcelData(int(len(data)), xlApp)
	workbook.SaveAs(os.path.join(path, newfile))
	xlApp.DisplayAlerts = 0
	xlApp.Visible = 0
	workbook.Close(0)
	
def CheckExcelData(TotalRows, xlApp):
	#double check excel data
	RowIndex = 1
	ColumnA = ""
	ColumnB = ""
	ColumnC = ""
	while(RowIndex<TotalRows):
		ColumnA = xlApp.Range("A"+str(RowIndex),"A"+str(RowIndex)).Value
		ColumnB = xlApp.Range("B"+str(RowIndex),"B"+str(RowIndex)).Value
		ColumnC = xlApp.Range("C"+str(RowIndex),"C"+str(RowIndex)).Value
		if(ColumnA=="" or ColumnB=="" or ColumnC==""):
			print "error"
			break
		RowIndex=RowIndex+1


OpenFile=open(FileName, 'rb')
ReadFile=OpenFile.read();
GetArray=BitArray(OpenFile,length=256)  #thanks 93mowmow give feedback: Add a hexfile.bin for testing.
for element in ReadFile: 
	GetString = GetString+bin(int(hex(ord(element)), 16))[2:].zfill(8)

GenerateExcel(MainPath, TemplateExcel, "GetArray", GetArray, OutputExcel)









