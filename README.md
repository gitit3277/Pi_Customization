# Pi_Customization (Graphical Interface provided by Tkinter) 
# This program will allow you to customize your Pi with the click of 1 Button
# The settings that will be changed will be as follows: 
#	set NTP to time.google.com
#	set the Pi to boot up to a webpage 
#	disable screen timeout 
#	duplicate HDMI-1 and HDMI-2 *** This setting will only alter the Pi 4 behaviour 
#	allow you to select a Static IP from a drop down list     
#	open port 22 so that ssh works 


#	Bugs 
#	SSH is not working due to closed port 22
#		*port opened using :
#		sudo systemctl enable ssh
#		sudo systemctl start ssh