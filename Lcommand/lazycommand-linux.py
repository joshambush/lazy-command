#!/usr/bin/python3
import selenium
from selenium import webdriver
import os
import time
import platform as plat

def auto_crawl():
	print('crawler activated. input tags to scrape. Ex: h1 Ex: p ')
	url = input("url to scrape: ")
	element_crawler = str(input('Element: '))
	driver = webdriver.Firefox()
	driver.get(url)
	view_raw = input('view page source(type yes or no): ')
	if(view_raw == "yes"):
		print(driver.page_source)
	else:
		pass
	driver.set_window_size(1500,1500)
	try:
		print(driver.find_element_by_tag_name(element_crawler))
	except:
		print("could not find "+ element_crawler )
	
				
		
	
def sysinfo():
	os_type = "Running on the "+plat.system() +" Operating system"
	version_type = "version: "+plat.release()
	
	print(' ')
	disk_info = os.system('df -h')
	print(' ')
	time.sleep(3)
	sys_info = os.system('sudo lshw')
	#with open('systeminfo-log.txt','a') as fl:
		#fl.write()
		
	
def checkme():
	print("checking IP address")
	print(os.system('anonsurf myip'))
	


def options():
	command = input('> ')
	while True:
		if(command == '1'):
			sysinfo()
			options()
		elif(command == '2'):
			checkme()
			options()
		elif(command == '3'):
			auto_crawl()
			options()
		elif(command == '4'):
			quit()
options()
		
		
	
	
	
	
	
