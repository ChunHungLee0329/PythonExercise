# coding=UTF-8

#import library.
import math
import pkgutil
import binascii
import bitstring
import win32com.client
import os
from bitstring import BitArray, BitStream


def ConvertArrayToString(data):
	Output=""
	for string in data:
		Output += string
	return Output

def GenerateExcel(path, template, data, newfile):
	#get the path folder to find the excel template. 
	#Using the data to fill up the excel to save as the new name from newfile
	xlApp = win32com.client.Dispatch("Excel.Application")
	workbook=xlApp.Workbooks.Open(os.path.join(path, template))
	LenData = int(len(data))
	TotalBits = LenData
	CurrentBits = 0
	IndexBits = 0
	RowIndex = 2
	while(CurrentBits<TotalBits):
		IndexBits = int(xlApp.Range("B"+str(RowIndex),"B"+str(RowIndex)).Value)		
		xlApp.Range("C"+str(RowIndex),"C"+str(RowIndex)).Value = ConvertArrayToString(data[CurrentBits:CurrentBits+IndexBits])
		CurrentBits = CurrentBits + IndexBits	
		RowIndex=RowIndex+1
	workbook.SaveAs(os.path.join(path, newfile))
	xlApp.DisplayAlerts = 0
	xlApp.Visible = 0
	workbook.Close(0)
	

#new main program
bitArray = []
FileName = "hexfile.bin" 
TemplateExcel = "BinToExcel_template.xls"
MainPath = "c:" + os.sep + "python27" + os.sep + "exercise" + os.sep + "BintoExcel" + os.sep
data = file(FileName, 'rb').read()
Array = BitArray(bytes=data[0:])
for item in Array:
	if(item):
		bitArray.append('1')
	else:
		bitArray.append('0')
GenerateExcel(MainPath, TemplateExcel, bitArray, "BinToExcel_result.xls")
