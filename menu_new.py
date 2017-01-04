# -*- coding: utf-8 -*-

''' 檔案資訊
檔名:menu.py
版本:version 1.00
功能:A class to show the ToolUserInterface
作者:李俊鴻, Neil Lee
時間:2016/12/28
更新紀錄:(最新的在最上面)
	=== Version 1.03 2017/1/4 update ===
	(1)chnage UI design/event: File->open sourcePath/templatePath
	(2)add config menu to control excel column
	(3)add login function  ==>pending db link
	(4)writelog()  ==>pending db link and insert into db.
	=== Version 1.02 2016/12/29 update ===
	(1)remove frameMessage in UI.
	(2)"tkMessageBox" will have message.
	=== Version 1.01 2016/12/28 update ===
	(1)add function "writeLog()" to keep operation error message file log.
	=== Version 1.00 2016/12/26 update ===
	(1)create class MainMenu	
作者筆記:
	(1)login/logout function is pending.
	(2)UI design/event change per eMow comment
	(3)add the menu to load a "Config.ini" setting.
'''


import sys
import Tkinter
from Tkinter import *
import BinExcelConverter as BEC
import tkFileDialog, tkMessageBox




class MainMenu(Tkinter.Tk):
	#[section]: initial
	def __init__(self, root):
		#initial variable (constructor)
		self.loginID = ""
		self.Msg = ""
		self.sourcePath = ""
		self.templatePath = ""
		self.configExcelSetting = ""
		#setting variable
		self.root = root
		self.root.title("DataConverterTool") #set Window Form Title
		self.root.geometry("600x400") #set Windows Size
		self.frame = Frame(root) #top level: frame
		self.menuBar = Menu(root) #create a default UI Menu object		
		self.createMenuItem() #loading MenuItem		

		
		
	#[section]: create UI/Menu
	#create MenuItem: menuBar
	def createMenuItem(self): 		
		#1. Menu:"File"
		self.menuFile = Menu(self.menuBar, tearoff=0)
		self.menuFile.add_command(label="Source File", command=lambda:self.browseFilePath(label="sourcePath"))
		self.menuFile.add_command(label="Template File", command=lambda:self.browseFilePath(label="templatePath"))
		self.menuFile.add_separator()
		self.menuFile.add_command(label="Login", command=self.createLoginWindow)
		self.menuFile.add_command(label="Logout", command=self.logout)
		self.menuFile.add_separator()
		self.menuFile.add_command(label="Exit", command=lambda:sys.exit())
		self.menuBar.add_cascade(label="File", menu=self.menuFile)
		#2. Menu:"Tool"		
		self.menuTool = Menu(self.menuBar, tearoff=0)
		self.menuTool.add_command(label="Bin/Excel Converter", command=self.eventChangeMenuItem_Tool_BinExcelConverter)
		self.menuTool.add_command(label="others...") 
		self.menuBar.add_cascade(label="Tool", menu=self.menuTool)
		#3. Menu:"Config"
		self.menuConfig = Menu(self.menuBar, tearoff=0)
		#3.1 Menu:"Config"-->"ExcelSetting"
		self.menuConfigSubmenu = Menu(self.menuConfig, tearoff=0)
		self.menuConfigSubmenu.add_radiobutton(label="ExcelSetting_Default", command=lambda:self.eventChhangeMenuItem_Config_ExcelSetting(item="ExcelSetting_Default"))
		self.menuConfigSubmenu.add_radiobutton(label="ExcelSetting_+1", command=lambda:self.eventChhangeMenuItem_Config_ExcelSetting(item="ExcelSetting_+1"))
		self.menuConfigSubmenu.add_radiobutton(label="ExcelSetting_+2", command=lambda:self.eventChhangeMenuItem_Config_ExcelSetting(item="ExcelSetting_+2"))
		self.menuConfig.add_cascade(label='ExcelSetting', menu=self.menuConfigSubmenu, underline=0)
		#3.2 Menu:"Config"-->OtherConfig
		self.menuConfig.add_command(label="OtherConfig...", underline=0)
		self.menuBar.add_cascade(label="Config", underline=0, menu=self.menuConfig)	
		#show Menu elements		
		self.root.config(menu=self.menuBar)
		self.frame.pack()
		self.root.mainloop()
	
	
	
	#[section]: Login/Logout template
	#System Login/Logout function
	def createLoginWindow(self):
		#open window: login
		self.frmLogin = Toplevel(self.root)
		self.frmLogin.title("login: enter your info.")
		self.frmLogin.geometry("250x150")
		self.frameLogin = Frame(self.frmLogin) #create a Frame "frameLogin" into fraLogin
		#frameLoginID: a Frame layout to clone "LoginID section"
		self.tempLoginID = StringVar() #string variable:"tempLoginID", assign value into "textLoginID"
		self.frameLoginID = Frame(self.frameLogin, pady=12)
		self.frameLoginID.pack(side=TOP, fill=X)
		self.lblLoginID = Label(self.frameLoginID, text="UserID:", width=10).grid(row=0, column=0)
		self.textLoginID = Entry(self.frameLoginID, width=20, textvariable=self.tempLoginID).grid(row=0, column=1)
		#frameLoginPWD: a Frame layout to clone "LoginPWD section"
		self.tempLoginPWD = StringVar() #string variable:"tempLoginPWD", assign value into "textLoginPWD"
		self.frameLoginPWD = Frame(self.frameLogin, pady=12)
		self.frameLoginPWD.pack(side=TOP, fill=X)
		self.lblLoginPWD = Label(self.frameLoginPWD, text="Password:", width=10).grid(row=0, column=0)
		self.textLoginPWD = Entry(self.frameLoginPWD, width=20, show="*", textvariable=self.tempLoginPWD).grid(row=0, column=1)
		#frameLoginBTN: a Frame layout to clone "LoginBTN section"
		self.frameLoginBTN = Frame(self.frameLogin)
		self.frameLoginBTN.pack(side=TOP, fill=X)
		self.btnLogin = Button(self.frameLoginBTN, text="Login", command=self.login)
		self.btnLogin.grid(row=0, column=0, padx=100)
		#frame pack/mainloop
		self.frameLogin.pack()
		self.frmLogin.mainloop()
	#Login	
	def login(self):
		#hardcode ID/PWD:1234/1234
		self.frmLogin.destroy()
		if(self.tempLoginID.get()=="1234" and self.tempLoginPWD.get()=="1234"):
			self.loginID = self.tempLoginID
			self.Msg = "Login successfully!"
			tkMessageBox.showinfo("OK", self.Msg)
		else:
			self.loginID = ""
			self.Msg = "Try again!"
			tkMessageBox.showinfo("Error", self.Msg)
	#Logout
	def logout(self):
		self.loginID = ""
		self.Msg = "Logout successfully!"
		tkMessageBox.showinfo("OK", self.Msg)
		
	
	
	#[section]: open Files dialog
	#File open
	def browseFilePath(self, label):
		tempPath = tkFileDialog.askopenfilename().encode('utf-8')
		setattr(self, label, tempPath)
		self.Msg = "Upload " + label + " successfully below:\n" + tempPath
		tkMessageBox.showinfo("OK", self.Msg)
		
		
		
	#[section]: Menu "Tool" change event 
	#Bin/Excel Converter
	def eventChangeMenuItem_Tool_BinExcelConverter(self):
		if(self.loginID == ""):
			tkMessageBox.showinfo("Error", "Please login system firstly!")
		else:
			converter = BEC.BinExcelConverter(self.sourcePath, self.templatePath)
			#OverRide object("converter") attribute
			if(self.configExcelSetting is not ""):
				converter.configExcelSetting = self.configExcelSetting
				converter.defaultProgramSetting()
			#start converter
			if(not converter.validationEncapsulation()):
				converter.writeLog()
				tkMessageBox.showinfo("Error", converter.message)
			else:			
				converter.convertingEncapsulation()#start converting to a new file.
				tkMessageBox.showinfo("OK", converter.message)
	
	
	
	#[section]: Menu "Config" change event
	#"ExcelSetting"
	def eventChhangeMenuItem_Config_ExcelSetting(self, item):
		self.configExcelSetting = item
		
	
	

	

	

#default python menu_new.py to new an object from class "MainMenu()"
if __name__ == '__main__':
	root = Tk()
	app = MainMenu(root)
	app.pack()
	root.mainloop()
	