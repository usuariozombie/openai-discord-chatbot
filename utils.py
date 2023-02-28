# -*- coding: utf-8 -*-

import datetime, json, math, os, time

class Color():
	Reset = "\u001b[0m"
	Bold = "\u001b[1m"
	Underline = "\u001b[4m"
	Black = "\u001b[30m"
	LightRed = "\u001b[31m"
	LightGreen = "\u001b[32m"
	Yellow = "\u001b[33m"
	Blue = "\u001b[34m"
	Magenta = "\u001b[35m"
	Cyan = "\u001b[36m"
	White = "\u001b[37m"
	Gray = "\u001b[90m"
	Red = "\u001b[91m"
	Green = "\u001b[92m"
	LightYellow = "\u001b[93m"
	LightBlue = "\u001b[94m"
	LightMagenta = "\u001b[95m"
	LightCyan = "\u001b[96m"
	LightGray = "\u001b[97m"
	BGBlack = "\u001b[40m"
	BGRed = "\u001b[41m"
	BGGreen = "\u001b[42m"
	BGYellow = "\u001b[43m"
	BGBlue = "\u001b[44m"
	BGMagenta = "\u001b[45m"
	BGCyan = "\u001b[46m"
	BGWhite = "\u001b[47m"
	BGGray = "\u001b[100m"
	BGLightRed = "\u001b[101m"
	BGLightGreen = "\u001b[102m"
	BGLightYellow = "\u001b[103m"
	BGLightBlue = "\u001b[104m"
	BGLightMagenta = "\u001b[105m"
	BGLightCyan = "\u001b[106m"

class Debug():
	def Error(Message): print(f"{Color.Red}[{now('time')} ERROR] » {Message}{Color.Reset}")
	def Good(Message): print(f"{Color.Green}[{now('time')} GOOD] » {Message}{Color.Reset}")
	def Info(Message): print(f"{Color.Yellow}[{now('time')} INFO] » {Message}{Color.Reset}")
	def Line(Message): print(f"	{Color.Cyan}· {Message}{Color.Reset}")

class JSON():
	def Create(file_path): open(file_path, "w", encoding = "utf-8").write("{}")
	def Indent(data): return json.dumps(data, indent = "\t")
	def Read(file_path):
		with open(file_path, "r", encoding = "utf-8") as file:
			data = json.load(file)
		file.close()
		return data
	def Write(file_path, data):
		with open(file_path, "w") as file:
			json.dump(data, file, indent = "\t")
		file.close()

def ClearScreen(Title = None):
	os.system("cls") if os.name == "nt" else os.system("clear")
	if Title == True:
		print(f"""{Color.Red}
		       ______ ______  ___ __ __   _______  ______   ______  __     __     
		      /_____//_____/\/__//_//_/\/_______/\/_____/\ /_____/\/__/\ /__/\    
		      \:::__\\:::_ \ \::\| \| \ \::: _  \ \:::_ \ \\::::_\/\ \::\\:.\ \   
		         /: / \:\ \ \ \:.      \ \::(_)  \/\:(_) ) )\:\/___/\_\::_\:_\/   
		        /::/___\:\ \ \ \:.\-/\  \ \::  _  \ \: __ `\ \::___\/__\/__\_\_/\ 
		       /_:/____/\:\_\ \ \. \  \  \ \::(_)  \ \ \ `\ \ \:\____/\ \ \ \::\ \.
		       \_______\/\_____\/\__\/ \__\/\_______\/\_\/ \_\/\_____\/\_\/  \__\/\n\n{Color.Reset}""".replace("	", ""))

def now(Mode):
	if Mode == "unix": return math.trunc(time.time())
	if Mode == "date": return datetime.datetime.now().strftime("%d/%m/%Y")
	if Mode == "time": return datetime.datetime.now().strftime("%H:%M:%S")
	if Mode == "complete": return datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

def PurgeCache():
	if os.name == "nt": os.system(f"if exist __pycache__ rd /Q /S __pycache__")
	if os.name == "posix": os.system(f"rm -r __pycache__")

def TextClearer(Text): return Text.replace("*", "").replace("_", "").replace("~", "").replace("`", "")