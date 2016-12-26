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


class MainMenu(Frame):
	def __init__(self, master):
		Frame.__init__(self, master, relief=SUNKEN, bd=2, width=400, height=350)
		self.grid()
		self.menubar = Menu(self)
		frame = Frame(master)
        #frame.pack()	
		
		#menu: File
		menuFile = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="File", menu=menuFile)
		
		#menu: Tool
		menuTool = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="Tool", menu=menuTool)
		menuTool.add_command(label="Bin/Excel Converter", command=self.onBinExcelConverter)
		
		#menu: Help
		menuHelp = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="Help", menu=menuHelp)
		#menuHelp.add_command(label="About")
		#menuHelp.add_command(label="User Manual")
		
		#menu: Exit
		menuExit = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="Exit", menu=menuExit, command=sys.exit)
		
		root.config(menu=self.menubar)
		root.mainloop()	
		
	def onBinExcelConverter(self):
		root = None
		self.MenuChange()		
		#menuHelp = Menu(self.menubar, tearoff=0)
		#self.menubar.add_cascade(label="Help", menu=menuHelp)
		#menuHelp.add_command(label="aaa")
		#menuHelp.add_command(label="User Manual")
		#print "1234"		
		
	def MenuChange(self):		
		app = MainMenu(self)	
		
		
if __name__ == '__main__':
	root = Tk()
	app = MainMenu(root)
	#app.pack()
	#root.mainloop()
