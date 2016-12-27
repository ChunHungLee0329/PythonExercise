# -*- coding: utf-8 -*-

''' 檔案資訊
檔名:program.py
版本:version 1.00
功能:A Tool support data file converter. (Data Converter Tool.ppt)
作者:李俊鴻, Neil Lee
時間:2016/12/24
更新紀錄:
	(1)Version 1.00:support BinToExcel/ExcelToBin
'''

from Tkinter import *
import sys
import os
import binExcelConverter as BEC
import menu_new as M_new
import menu as M

def main():	

	help = "sample command for you: python program.py C:\a.bin C:\b.xls"
	if(len(sys.argv) == 1):	
		#root = Tk()
		#myMenu = M_new.MainMenu(root)
		myMenu = M.MainMenu()
		
	elif(len(sys.argv) == 3):
		input = sys.argv[1] #get the parameter: inputPath
		template = sys.argv[2] #get the parameter: outputPath
		converter = BEC.BinExcelConverter(input, template) #assin an object to "converter" from class "BinExcelConverter"
		if(not converter.volidateFileExtension()):#volidate file name extension
			print converter.message()
		elif(not converter.volidateConvertingItem()):#volidate converting item(BinToExcel/ExcelToBin)
			print converter.message()
		elif(not converter.volidateFilePath()):#volidate file existence (inputPath/templatePath)
			print converter.message()
		else:
			converter.copyAsTempData()#copy data into folder=tempData (inputPath/templatePath)
			converter.readFileToString()#read file data to a string
			converter.convert()#start converting to a new file.
	else:
		print help
 
if __name__ == "__main__":
    main()