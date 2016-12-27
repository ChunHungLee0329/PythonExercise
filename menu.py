# -*- coding: utf-8 -*-

''' 檔案資訊
檔名:menu.py
版本:version 1.00
功能:A class to show the ToolUserInterface
作者:李俊鴻, Neil Lee
時間:2016/12/26
更新紀錄:
	(1)Version 1.00: create class MainMenu
'''


# -*- coding: utf-8 -*-

''' 檔案資訊
檔名:menu.py
版本:version 1.00
功能:A class to show the ToolUserInterface
作者:李俊鴻, Neil Lee
時間:2016/12/26
更新紀錄:
	(1)Version 1.00: create class MainMenu
'''


import sys
from Tkinter import *
import BinExcelConverter as BEC
import tkFileDialog, tkMessageBox


class MainMenu():
	
	def __init__(self):
		self.root = Tk() #create an initial Frame 
		self.root.title("DataConverterTool") #set Window Form Title
		self.root.geometry("400x350") #set Windows Size
		
		menubar = Menu(self.root) #default menubar from Menu
		self.createMenuItem() #create Menu Item
		
		#self.textInputPath = self.root.Entry(self.root)
		#self.textTemplatePath = ""
		#self.tempInputPath = StringVar()
	
	def createMenuItem(self):	
		#create a Menu object
		menubar = Menu(self.root)		
		
		###Setting MenuItems
		#1.Menu: "File"
		menuFile = Menu(menubar, tearoff=0)
		menubar.add_cascade(label="File", menu=menuFile)		
		#2.Menu: "Tool"
		menuTool = Menu(menubar, tearoff=0)
		menuTool.add_command(label="Bin/Excel Converter", command=self.eventChangeMenu_BinExcelConverter)
		menubar.add_cascade(label="Tool", menu=menuTool)
		#3.Menu: "About"
		menuAbout = Menu(menubar, tearoff=0)
		menubar.add_cascade(label="About", menu=menuAbout)
		#4.Menu: "Exit"
		menuExit = Menu(menubar, tearoff=0)
		menubar.add_cascade(label="Exit", menu=menuExit)			
		#show Menu elements
		self.root.config(menu=menubar)
		self.root.mainloop()
	
	
	'''eventChangeMenuItem'''
	def eventChangeMenu_BinExcelConverter(self):
		#self.MenuChange()

		#frameSource=inputPath section
		frameSource = Frame(self.root, width=400, height=50, padx=70, pady=10)
		frameSource.pack(side=TOP, fill=X)
		lblSource = Label(frameSource, text="Source:").grid(row=0, column=0)
		textInputPath = Entry(frameSource, bd=1).grid(row=0, column=1)
		btnSource = Button(frameSource, text="Browse", anchor=W, justify=LEFT, padx=5, command=lambda:textInputPath.set(tkFileDialog.askopenfilename().encode('utf-8'))).grid(row=0, column=2)
		#btnSource = Button(frameSource, text="Browse", anchor=W, justify=LEFT, padx=5, command=lambda:self.getInputPath()).grid(row=0, column=2)
		#tkFileDialog.askopenfilename().encode('utf-8')
		
		#frameTemplate=templatePath section
		frameTemplate = Frame(self.root, width=400, height=50, padx=55, pady=10)
		frameTemplate.pack(side=TOP, fill=X)
		lblTemplate = Label(frameTemplate, text="Template:").grid(row=0, column=0)
		self.textTemplatePath = Entry(frameTemplate, bd=1).grid(row=0, column=1)
		btnTemplate = Button(frameTemplate, text="Browse", anchor=W, justify=LEFT, padx=5, command=lambda:self.getTemplatePath()).grid(row=0, column=2)
		
		#frameMessage=Message:
		frameMessage = Frame(self.root, width=400, height=50, padx=35, pady=10)
		frameMessage.pack(side=TOP, fill=X)
		lblMessage = Label(frameMessage, text="Message:", anchor=W, justify=LEFT, padx=20, pady=20).grid(row=2, column=0)
		#textMessage = ScrolledText(frameMessage, bd=1)
		#textMessage.pack(row=2, column=1)
		
		#frameConvert=button Convert:
		frameConvert = Frame(self.root, width=400, height=25, padx=150)
		frameConvert.pack(side=TOP, fill=X)		
		btnConverter = Button(frameConvert, text="Converter", command=lambda:self.convert(i, o))
		btnConverter.grid(row=3, column=1)		

		
	
	def getInputPath(self):
		aaa = "1"
		#self.tempInputPath.set(tkFileDialog.askopenfilename().encode('utf-8'))
		#tempInputPath = tkFileDialog.askopenfilename().encode('utf-8')
		#self.textInputPath.set(tempInputPath)
	
	def getTemplatePath(self):
		tempTemplatePath = tkFileDialog.askopenfilename().encode('utf-8')
		#self.TemplatePath.set(tempTemplatePath)
	
	
	def convert(self, i, o):
		self.i = i
		self.o = o
		print i	
	
	
	def MenuChange(self):
		#self.root.destroy()
		print "1234"
	
	
	
	
	
	
	
	
		
		
if __name__ == '__main__':
	print "5678"
	
	
	

	
	
