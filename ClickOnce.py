#!/usr/bin/python3 

from tkinter import *
from PIL import ImageTk, Image
import os, time 

#Takes string input and returns dictionary with keys  
def dict_return(strings):
	dictionary_keys=["ID", "NAME", "LOCATION", "IP_SUBNET", "ROUTERS", "DNS", "NTP", "WEBPAGE"]
	temp_list=strings.strip()

	temp_list=strings.split(",")

	dictionary_list={}	
	for i in range(len(dictionary_keys)):
		dictionary_list.update({dictionary_keys[i]: temp_list[i].strip()})
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
def script1(pie):
	os.system("echo [Time] >/etc/systemd/timesyncd.conf")
	f = open("/etc/systemd/timesyncd.conf", "a")
	f.write(pie["NTP"]  + "\n")
	f.close()	

#Script2 sets the IP address to static by modifying /etc/dhcpcd.conf
def script2(pie): 

	f = open("/etc/xdg/lxsession/LXDE-pi/autostart", "w")
	f.write("@lxpanel --profile LXDE-pi\n@pcmanfm --desktop --profile LXDE-pi\n@xscreensaver -no-splash\npoint-rpi\n@chromium-browser --noerrdialogs --kiosk --incognito ")	
	f.close()	

	f = open("/etc/xdg/lxsession/LXDE-pi/autostart", "a")
	f.write(pie["WEBPAGE"])
	f.write("\n@xset s noblank\n@xset s off\n@xset s -dpms\n@xrandr --output HDMI-2 --same-as HDMI-1\n")
	
	f.close()

#Script3 sets the Kiosk webpage, disables the screen timeout, duplicates the HDMI-1 on HDMI-2 and enables SSH by modyfing the /etc/xdg/lxsession/LXDE-pi/autostart file
def script3(pie):
	
	f = open("/etc/dhcpcd.conf", "w")
	f.write("interface eth0 \n")
	f.close()

	
	f = open("/etc/dhcpcd.conf", "a")     
	f.write("hostname \n")
	f.write("clientid \n")
	f.write("persistent \n")
	f.write("option rapid_commit \n")
	f.write("option domain_name_servers, domain_name, domain_search, host_name \n")
	f.write("option classless_static_routes \n")
	f.write("option interface_mtu \n")

	f.write("static "+pie["IP_SUBNET"]+"\n")
	f.write("static "+pie["ROUTERS"]+"\n")
	f.write("static "+pie["DNS"]+"\n")

	f.close()





def click():
	for i in range(len(pies)):


		if pies[i]["ID"]==listbox.get(ACTIVE)[:6]:
			#Set NTP
			script1(pies[i])
			
			#Set Static IP
			script2(pies[i])

			#Set Kiosk Webpage, Disable screen timeout, Duplicate HDMI-1 on HDMI-2, enable ssh 	
			script3(pies[i])

			if pies[i]["NAME"]=="Default":
				print("Defaults are being set")
				
			os.system("cp DEFAULTS/timesyncd.conf /etc/systemd/timesyncd.conf")
			os.system("cp DEFAULTS/dhcpcd.conf /etc/dhcpcd.conf") 
			os.system("cp DEFAULTS/autostart /etc/xdg/lxsession/LXDE-pi/autostart") 

def reboot_now():
	time.sleep(3)
	os.system("init 6")

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
		listbox.insert(END, pies[i]["ID"]+" "+pies[i]["NAME"])

	#add a button to perform the configuration 
	Button(window, text="SUBMIT", width=6, command=click) .pack() 

	#add a reboot button 
	Button(window, text="Reboot", width=6, command=reboot_now) .pack() 

	#run the main loop   
	window.mainloop() 




