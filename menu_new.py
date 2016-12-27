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




class MainMenu(Tk):
	
	def __init__(self, root):
		self.root = root
		self.root.title("DataConverterTool") #set Window Form Title
		self.root.geometry("400x350") #set Windows Size
		self.frame = Frame(root) #top level: frame
		self.menubar = Menu(root) #create a default UI Menu object
		self.createMenuItem()	
		
	def createMenuItem(self):
		###Setting MenuItems
		#1.Menu: "File"
		self.menuFile = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="File", menu=self.menuFile)		
		#2.Menu: "Tool"
		self.menuTool = Menu(self.menubar, tearoff=0)
		self.menuTool.add_command(label="Bin/Excel Converter", command=self.eventChangeMenu_BinExcelConverter)
		self.menubar.add_cascade(label="Tool", menu=self.menuTool)
		#3.Menu: "About"
		self.menuAbout = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="About", menu=self.menuAbout)
		#4.Menu: "Exit"
		self.menuExit = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="Exit", menu=self.menuExit)
		#show Menu elements
		self.root.config(menu=self.menubar)
		self.root.mainloop()
		
	
	
	'''eventChangeMenuItem'''
	#reset all content 
	def MenuChange(self):
		self.frame.grid_remove()
	
	def eventChangeMenu_BinExcelConverter(self):
		self.MenuChange()
		
		#frameSource=inputPath section
		frameSource = Frame(self.frame, bg='yellow', pady=5)
		frameSource.pack(side=TOP, fill=X)
		lblSource = Label(frameSource, text="Source:", width=10).grid(row=0, column=0)
		textInputPath = Entry(frameSource, bd=1, width=25).grid(row=0, column=1)
		btnSource = Button(frameSource, text="Browse", width=8).grid(row=0, column=2)
		#btnSource = Button(frameSource, text="Browse", anchor=W, justify=LEFT, padx=5, command=lambda:self.getInputPath()).grid(row=0, column=2)
		#tkFileDialog.askopenfilename().encode('utf-8')
		
		#frameTemplate=templatePath section
		frameTemplate = Frame(self.frame, bg='blue', pady=5)
		frameTemplate.pack(side=TOP, fill=X)
		lblTemplate = Label(frameTemplate, text="Template:", width=10).grid(row=0, column=0)
		self.textTemplatePath = Entry(frameTemplate, bd=1, width=25).grid(row=0, column=1)
		btnTemplate = Button(frameTemplate, text="Browse", width=8).grid(row=0, column=2)
		
		#frameMessage=Message:
		frameMessage = Frame(self.frame, bg='red', pady=15)
		frameMessage.pack(side=TOP, fill=X)		
		lblMessage = Label(frameMessage, text="Message:", width=10).grid(row=0, column=0)
		textMessage = Listbox(frameMessage, bd=1, width=34, height=3).grid(row=0, column=1)
		
		#frameConvert=button Convert:
		frameConvert = Frame(self.frame, bg='green', pady=5)
		frameConvert.pack(side=TOP, fill=X)		
		btnConverter = Button(frameConvert, text="Converter")#, command=lambda:self.convert(i, o))
		btnConverter.grid(row=3, column=1, padx=150)
				
		self.frame.grid(row=0, column=0, padx=15, pady=30)
		
		
	


	
if __name__ == '__main__':
	root = Tk()
	app = MainMenu(root)
	app.pack()
	root.mainloop()