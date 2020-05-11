#!/usr/bin/python3 

from tkinter import *
from PIL import ImageTk, Image
import os, time 

#Takes string input and returns dictionary with keys  
def dict_return(strings):
	dictionary_keys=["ID", "NAME", "LOCATION", "IP_SUBNET", "ROUTERS", "DNS","WEBPAGE"]
	temp_list=strings.rstrip(' ').split(",")
	dictionary_list={}	
	for i in range(len(dictionary_keys)):
		dictionary_list.update({dictionary_keys[i]: temp_list[i]})
	return dictionary_list	


#Function that reads a file and returns a list, where each item in the list is a dictionary with key values    
def list_of_configurations(FILENAME):
	content=[line.rstrip('\n') for line in open(FILENAME)]
	content=[x for x in content if x[0]  !="#"]

	# Converts each string in the content list into a dictionary 
	for i in range(len(content)):
		content[i]= dict_return(content[i])
	
	return content	

#Script1 sets NTP by modifying /etc/systemd/timesyncd.conf 
def script1():
	pass

#Script2 sets the IP address to static by modifying /etc/dhcpcd.conf
def script2(): 
	pass

#Script3 sets the Kiosk webpage, disables the screen timeout, duplicates the HDMI-1 on HDMI-2 and enables SSH by modyfing the /etc/xdg/lxsession/LXDE-pi/autostart file
def script3():
	pass

def click():
	print(listbox.get(ACTIVE)[:6])
	for i in range(len(pies)):
		if pies[i]["ID"]==listbox.get(ACTIVE)[:6]:
			print("Found it")	
			print(pies[i])
			#Set NTP
			script1()
			
			#Set Static IP
			script2()

			#Set Kiosk Webpage, Disable screen timeout, Duplicate HDMI-1 on HDMI-2, enable ssh 	
			script3()

	pass

def reboot_now():
	pass

if __name__=="__main__":
	pies=list_of_configurations("static_configurations.txt")	
	
	window=Tk()
	window.title("ClickOnce Pi Setup ")
	window.geometry("400x600")

	#add picture 
	canvas=Canvas(window, width=300, height=300)
	image=ImageTk.PhotoImage(Image.open("picture.jpg"))
	canvas.create_image(0,0,anchor=NW,image=image)
	canvas.pack()  

	#Create Scroll bar 
	scrollbar = Scrollbar(window)
	scrollbar.pack(side=RIGHT, fill=Y)
	listbox=Listbox(window, width=28, height=10)
	listbox.pack()

	listbox.config(yscrollcommand=scrollbar.set)
	scrollbar.config(command=listbox.yview)

	#add the configuration options to the list
	for i in range(len(pies)):
		listbox.insert(END, pies[i]["ID"]+pies[i]["NAME"])

	#add a button to perform the configuration 
	Button(window, text="SUBMIT", width=6, command=click) .pack() 

	#add a reboot button 
	Button(window, text="Reboot", width=6, command=reboot_now) .pack() 

	#run the main loop   
	window.mainloop() 




