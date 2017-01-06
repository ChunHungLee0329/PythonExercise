# -*- coding: utf-8 -*-

''' �ɮ׸�T
�ɦW:program.py
����:version 1.02
�\��:A Tool support data file converter. (Data Converter Tool.ppt)
�@��:���T�E, Neil Lee
�ɶ�:2016/12/24
��s����:(�̷s���b�̤W��)
	=== Version 1.02 2016/1/5 update ===
	(1)use class "menu" from file "menu.py"
	(2)use class "BinExcelConverter" from file "BinExcelConverter.py"
	=== Version 1.01 2016/12/28 update ===
	(1)add new Menu class "menu_new"
	=== Version 1.00 2016/12/26 update ===
	(1)support BinToExcel/ExcelToBin	
'''

from Tkinter import *
import sys
import os
import BinExcelConverter as BEC
#import menu_new as M_new
import menu as M

def main():	

	help = "sample command for you: python program.py C:\a.bin C:\b.xls"
	if(len(sys.argv) == 1):	
		root = Tk()
		#myMenu = M_new.MainMenu(root)
		myMenu = M.MainMenu(root)
		
	elif(len(sys.argv) == 3):
		input = sys.argv[1] #get the parameter: inputPath
		template = sys.argv[2] #get the parameter: outputPath
		converter = BEC.BinExcelConverter(input, template) #assign an object to "converter" from class "BinExcelConverter"
		if(not converter.validationEncapsulation()):
			converter.writeLog()
			print converter.message
		else:			
			converter.convertingEncapsulation()#start converting to a new file.
			print converter.message
	else:
		print help
 
if __name__ == "__main__":
    main()