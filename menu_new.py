# -*- coding: utf-8 -*-

''' 檔案資訊
檔名:menu.py
版本:version 1.00
功能:A class to show the ToolUserInterface
作者:李俊鴻, Neil Lee
時間:2016/12/28
更新紀錄:
	=== Version 1.00 2016/12/26 update ===
	(1)create class MainMenu
	=== Version 1.01 2016/12/28 update ===
	(1)add function "writeLog()" to keep operation error message file log.
'''


import sys
from Tkinter import *
import BinExcelConverter as BEC
import tkFileDialog, tkMessageBox




class MainMenu(Tk):
	
	
	#initial class
	def __init__(self, root):
		self.root = root
		self.root.title("DataConverterTool") #set Window Form Title
		self.root.geometry("500x350") #set Windows Size
		self.frame = Frame(root) #top level: frame
		self.menuBar = Menu(root) #create a default UI Menu object
		self.createMenuItem() #loading MenuItem
	
	
	#create MenuItem: menuBar
	def createMenuItem(self): 		
		#1.Menu: "File"
		self.menuFile = Menu(self.menuBar, tearoff=0)
		self.menuBar.add_cascade(label="File", menu=self.menuFile)
		
		#2.Menu: "Tool"		
		self.menuTool = Menu(self.menuBar, tearoff=0)
		#2.1 "Bin/Excel Converter"
		self.menuTool.add_command(label="Bin/Excel Converter", command=self.eventChangeMenu_BinExcelConverter) 
		self.menuBar.add_cascade(label="Tool", menu=self.menuTool)
		
		#3.Menu: "About"
		self.menuAbout = Menu(self.menuBar, tearoff=0)
		self.menuBar.add_cascade(label="About", menu=self.menuAbout)
		
		#4.Menu: "Exit"
		self.menuExit = Menu(self.menuBar, tearoff=0)
		#4.1 "Exit"
		self.menuExit.add_command(label="Exit", command=lambda:sys.exit())
		self.menuBar.add_cascade(label="Exit", menu=self.menuExit) 
		
		#show Menu elements
		self.root.config(menu=self.menuBar)
		self.root.mainloop()

	
	#browse to assign a file path
	def browseFilePath(self):
		return tkFileDialog.askopenfilename().encode('utf-8')

		
	#select Menu: "Tool"->"Bin/Excel Converter"
	def loadMenuChange(self):
		self.frame.grid_remove()
	
		
	#eventChangeMenu: go to Menu "Tool" -> "Bin/Excel Converter"
	def eventChangeMenu_BinExcelConverter(self):
		#self.loadMenuChange()
		
		#frameSource: a Frame layout to clone "inputPath section"
		self.tempInput = StringVar() #string variable:"tempInput", assign value into "textInputPath"
		self.frameSource = Frame(self.frame, pady=5)
		self.frameSource.pack(side=TOP, fill=X)
		self.lblSource = Label(self.frameSource, text="Source:", width=10).grid(row=0, column=0)
		self.textInputPath = Entry(self.frameSource, width=40, state="readonly", textvariable=self.tempInput).grid(row=0, column=1)
		self.btnSource = Button(self.frameSource, text="Browse", width=8, command=lambda:self.tempInput.set(self.browseFilePath())).grid(row=0, column=2)

		#frameTemplate: a Frame layout to clone "templatePath section"
		self.tempTemplate = StringVar() #string variable:"tempTemplate", assign value into "textTemplatePath"
		self.frameTemplate = Frame(self.frame, pady=5)
		self.frameTemplate.pack(side=TOP, fill=X)
		self.lblTemplate = Label(self.frameTemplate, text="Template:", width=10).grid(row=0, column=0)
		self.textTemplatePath = Entry(self.frameTemplate, width=40, state="readonly", textvariable=self.tempTemplate).grid(row=0, column=1)
		self.btnTemplate = Button(self.frameTemplate, text="Browse", width=8, command=lambda:self.tempTemplate.set(self.browseFilePath())).grid(row=0, column=2)
		
		#frameMessage: a Frame layout to clone "Message section"
		self.tempMessage = StringVar() #string variable:"tempMessage", assign value into "textMessage"
		self.frameMessage = Frame(self.frame, pady=15)
		self.frameMessage.pack(side=TOP, fill=X)		
		self.lblMessage = Label(self.frameMessage, text="Message:", width=10).grid(row=0, column=0)
		self.textMessage = Text(self.frameMessage, width=48, height=5).grid(row=0, column=1)
		#self.textMessage = Listbox(self.frameMessage, bd=1, width=48, height=3).grid(row=0, column=1)
		
		#frameConvert= a Frame layout to clone "Convert Button section"
		self.frameConvert = Frame(self.frame, pady=5)
		self.frameConvert.pack(side=TOP, fill=X)		
		self.btnConverter = Button(self.frameConvert, text="Converter", command=lambda:self.convert(self.tempInput.get(), self.tempTemplate.get()))
		self.btnConverter.grid(row=3, column=1, padx=200)
		
		#frame grid
		self.frame.grid(row=0, column=0, padx=15, pady=30)
	
	
	#execute Data Convertion
	def convert(self, input, template):
		converter = BEC.BinExcelConverter(input, template)
		if(not converter.volidateVariable()): #volidate if input/template missing
			converter.writeLog() #testing for writeLog()
			print converter.message
			#self.textMessage.insert(END, converter.message)
		elif(not converter.volidateFileExtension()):#volidate file name extension
			print converter.message
		elif(not converter.volidateConvertingItem()):#volidate converting item(BinToExcel/ExcelToBin)
			print converter.message
		elif(not converter.volidateFilePath()):#volidate file existence (inputPath/templatePath)
			print converter.message
		else:
			converter.copyAsTempData()#copy data into folder=tempData (inputPath/templatePath)
			converter.readFileToString()#read file data to a string
			converter.convert()#start converting to a new file.


#default python menu_new.py to new an object from class "MainMenu()"
if __name__ == '__main__':
	root = Tk()
	app = MainMenu(root)
	app.pack()
	root.mainloop()