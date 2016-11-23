# coding=UTF-8

#import library.
import math
import pkgutil
import binascii
import bitstring
import win32com.client
import os
from bitstring import BitArray, BitStream


def ConvertChrtoInt(data):
	#region convert 0~F to 0~15, e.g. 3=3, A=10, F=15
	Output = 0
	if(data=="A"):
		Output = 10
	elif(data=="B"):
		Output = 11
	elif(data=="C"):
		Output = 12
	elif(data=="D"):
		Output = 13
	elif(data=="E"):
		Output = 14
	elif(data=="F"):
		Output = 15
	else:
		Output = int(data)
	return Output

def GetBitValue(data):
	#convert the bit to the value, e.g. 1=0001, F=1111 etc.
	Output = ""
	n=3
	while (n>=0):
		if(data>=2**n):
			data=data-2**n
			Output+='1'
		else:
			Output+='0'
		n=n-1
	return Output	

def ReadBit(data):
	#Read the Bit then convert to the Value
	return GetBitValue(ConvertChrtoInt(data))	

def Generator(data):
	#generate an array from the data resource, e.g. file, bits set or else
	DataArray=[]
	if(hasattr(data, 'read')):
		read = data.read()
		for element in read:
			if(element):
				DataArray.append(element)
		yield DataArray	
	else:
		for element in data:
			DataArray.append(element)
		yield DataArray	

def GenerateBitString(data):
	#input data then generate the bit string
	result=""
	generator = Generator(data)
	for Item in generator:
		for Element in Item:
			if(len(hex(ord(Element)).replace('0x','').upper())==1):
				result += "0"+hex(ord(Element)).replace('0x','').upper()
			else:
				result += hex(ord(Element)).replace('0x','').upper()
	return result

def GenerateBitArray(data):
	#input bit string then output the BitArray
	DataArray=[]
	for bit in GenerateBitString(data):
		DataArray.append(ReadBit(bit))
	return DataArray

def SplitBitArray(data):
	#split each element in the Bit Array, e.g. ["1234"]->["1","2","3","4"]
	DataArray=[]
	for bit in data:
		DataArray.append(bit[0])
		DataArray.append(bit[1])
		DataArray.append(bit[2])
		DataArray.append(bit[3])
	return DataArray

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
	



#main program
FileName = "hexfile.bin" 
TemplateExcel = "BinToExcel_template.xls"
MainPath = "c:" + os.sep + "python27" + os.sep + "exercise" + os.sep + "BintoExcel" + os.sep
data = open(FileName, 'rb')
tmpArray = SplitBitArray(GenerateBitArray(data))
GenerateExcel(MainPath, TemplateExcel, tmpArray, "BinToExcel_result.xls")


