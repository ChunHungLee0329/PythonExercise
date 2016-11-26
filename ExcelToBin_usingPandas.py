# coding=UTF-8
# -*- coding: utf-8 -*-

import math
import pkgutil
import binascii
import bitstring
import win32com.client
import os
from bitstring import BitArray, BitStream
import pandas 
import xlrd

template = "ExcelToBin_template.xls" 
template_sheet="Sheet1"
OutputBin = "ExcelToBin.bin"
MainPath = os.getcwd()  #use getcwd     #MainPath = "c:" + os.sep + "python27" + os.sep

data = pandas.read_excel(open(template,'rb'), sheetname=template_sheet)#, header=None, skiprows=1)
index=0
ExcelValues=""

#Reading Excel using pandas
while(index<len(data)):
	Bits = int(str(data.iloc[index:index+1][['Bits']].values[0][0]).split('.')[0])
	Value = str(data.iloc[index:index+1][['Value']].values[0][0])
	ExcelValues = ExcelValues+Value.zfill(Bits)
	index=index+1

#Excel Value string to Array
HexArray=[]
Index=0
while(Index<len(ExcelValues)):
	HexArray.append(hex(int((ExcelValues)[Index:Index+8],2)))
	Index=Index+8

#write to .bin
with open('hexfile_result.bin', 'wb') as f:
    f.write(bytearray(int(i, 16) for i in HexArray))
	

