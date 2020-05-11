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

	#run the main loop   
	window.mainloop() 




