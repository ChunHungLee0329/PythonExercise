# coding=UTF-8

from tkinter import *
from tkinter import ttk
import datetime
import math
import pkgutil
import binascii
import bitstring
import win32com.client
import os
from bitstring import BitArray, BitStream

MainPath = os.getcwd()
strFormTitle="BinaryFileConversion"


def funBinToExcel():
	strBitsValue = ""
	inputName = "hexfile.bin"
	Template = "BinToExcel_template.xls"
	outputName = "BinToExcel_result_" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".xls"
	OpenFile=open(inputName, 'rb')
	ReadFile=OpenFile.read();
	for element in ReadFile: 
		strBitsValue = strBitsValue + bin(int(hex(ord(element)), 16))[2:].zfill(8)
	funGenerateExcel(MainPath, Template, strBitsValue, outputName)

def funGenerateExcel(path, template, data, newfile):
	xlApp = win32com.client.Dispatch("Excel.Application")
	workbook=xlApp.Workbooks.Open(os.path.join(path, template))
	RowIndex = 2
	CurrentBit = 0
	BitRange = 0
	while(CurrentBit<int(len(data))):
		BitRange = int(str(xlApp.Range("B"+str(RowIndex),"B"+str(RowIndex)).Value).split(".")[0])
		if type(data) is bitstring.BitArray:
			xlApp.Range("C"+str(RowIndex),"C"+str(RowIndex)).Value = data[CurrentBit:CurrentBit+BitRange].bin
		if type(data) is str:
			xlApp.Range("C"+str(RowIndex),"C"+str(RowIndex)).Value = data[CurrentBit:CurrentBit+BitRange]			
		CurrentBit = CurrentBit + BitRange	
		RowIndex=RowIndex+1
	workbook.SaveAs(os.path.join(path, newfile))
	xlApp.DisplayAlerts = 0
	xlApp.Visible = 0
	workbook.Close(0)

def funExcelToBin():
	inputName = "ExcelToBin_template.xls"
	outputName = "ExcelToBin_result_" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".bin"
	Template = ""
	ExcelValues=""
	RowIndex = 2
	RowMax = 65536
	Index=0
	HexArray=[]
	xlApp = win32com.client.Dispatch("Excel.Application")
	workbook = xlApp.Workbooks.Open(os.path.join(MainPath, inputName))
	while(RowIndex<RowMax):
		if xlApp.Range("C"+str(RowIndex),"C"+str(RowIndex)).Text=="":
			RowIndex = RowMax
		else:
			ExcelValues=ExcelValues+xlApp.Range("C"+str(RowIndex),"C"+str(RowIndex)).Text
		RowIndex=RowIndex+1
	xlApp.DisplayAlerts = 0
	xlApp.Visible = 0
	workbook.Close(0)
	while(Index<len(ExcelValues)):
		HexArray.append(hex(int((ExcelValues)[Index:Index+8],2)))
		Index=Index+8
	funGenerateBin(MainPath, Template, HexArray, outputName)

def funGenerateBin(path, template, data, newfile):
	with open(newfile, 'wb') as f:
		f.write(bytearray(int(i, 16) for i in data))
	
window=Tk()
window.title( strFormTitle )  #define title
window.geometry('600x200') #define window form size
mainframe = ttk.Frame(window, padding="6 6 24 24")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=2)
mainframe.rowconfigure(0, weight=2)
ttk.Label(mainframe, text="1.BinToExcel(Read a hexfile and convert to Excel)").grid(row=1, column=1, sticky=W)
ttk.Button(mainframe, text="BinToExcel", command=funBinToExcel).grid(row=2, column=1, sticky=W)
ttk.Label(mainframe, text="2.ExcelToBin(Read an excelfile and generate a hexfile)").grid(row=3, column=1, sticky=W)
ttk.Button(mainframe, text="ExcelToBin", command=funExcelToBin).grid(row=4, column=1, sticky=W)
window.mainloop() 




