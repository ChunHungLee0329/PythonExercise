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
import lxml
from pandas import ExcelWriter

template = "ExcelToBin_template.xls" 
template_sheet="Sheet1"
OutputBin = "ExcelToBin.bin"
MainPath = os.getcwd()  

data = pandas.read_html("http://www.stockq.org/taiwan/exchange_rate_CNY.php")[5]
writer = ExcelWriter('RateForRMB.xls')
data.to_excel(writer,'Sheet1')
writer.save()
