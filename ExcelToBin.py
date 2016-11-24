import math
import pkgutil
import binascii
import bitstring
import win32com.client
import os
from bitstring import BitArray, BitStream


template = "ExcelToBin_template.xls" 
OutputBin = "ExcelToBin.bin"
MainPath = os.getcwd()  #use getcwd     #MainPath = "c:" + os.sep + "python27" + os.sep


#get Source bytes from Excel column C
ExcelValues=""
RowIndex = 2
RowMax = 65536
xlApp = win32com.client.Dispatch("Excel.Application")
workbook = xlApp.Workbooks.Open(os.path.join(MainPath, template))
while(RowIndex<RowMax):
	if xlApp.Range("C"+str(RowIndex),"C"+str(RowIndex)).Text=="":
		RowIndex = RowMax
	else:
		ExcelValues=ExcelValues+xlApp.Range("C"+str(RowIndex),"C"+str(RowIndex)).Text
	RowIndex=RowIndex+1
xlApp.DisplayAlerts = 0
xlApp.Visible = 0
workbook.Close(0)

#Excel Value string to Array
HexArray=[]
Index=0
while(Index<len(ExcelValues)):
	HexArray.append(hex(int((ExcelValues)[Index:Index+8],2)))
	Index=Index+8

#write to .bin
with open('hexfile_result.bin', 'wb') as f:
    f.write(bytearray(int(i, 16) for i in HexArray))
	
