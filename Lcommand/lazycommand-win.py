import subprocess
import webbrowser
import os
import time
import hashlib

def main1():
	print ""
	print ""
	print " #################################"
	print " #################################"
	print " ##### password MD5 hashing  #####"
	print " #################################"
	print " #################################"
	print ""
	print ""
	password_hash = raw_input("Enter password to hash: ")
	print "               "
	print " Hashing psw... "
	time.sleep(2)
	print " Almost done....."
	time.sleep(1)
	print ""
	hashing_method(password_hash)

def hashing_method(password_hash): 
	hash1 = hashlib.md5(password_hash)
	print "______________________________________________________"
	print "######################################################"
	print "# Password: "+ hash1.hexdigest()
	print "######################################################"
	print ""

def main():
	with open('usage.txt', 'r') as f:
		f_contents = f.read()
		print""
		print f_contents
		print""

	r = int(raw_input("--> "))
	print ""
	if r == 1:
		subprocess.call('ipconfig')
	elif r == 2:
		subprocess.call('tasklist')
	elif r == 3:
		subprocess.call('netstat')
	elif r == 4:
		os.system('cmd') #Need to be fixed 
	elif r == 5:
		W = raw_input("Enter Website: ")
		webbrowser.open(W)
	elif r == 6:
		with open('passQ.txt', 'r') as fl:
			fl_contents = fl.read()
			print fl_contents
			print ""
	elif r == 7:
		fd = open('passQ.txt',"w")
		input = raw_input("Write to file:")
		fd.write(input)
	elif r == 8:
		time.ctime()
		CREATE_NO_WINDOW = 0x08000000
		netShut = subprocess.call('ipconfig -release', creationflags=CREATE_NO_WINDOW)
		print "Internet is Off!"
	elif r == 9 :
		time.ctime()
		CREATE_NO_WINDOW = 0x08000000
		netShut = subprocess.call('ipconfig -renew', creationflags=CREATE_NO_WINDOW)
		print "Internet is On!"
	elif r == 10:
		main1()
        elif r == 11:
                subprocess.call()
	else:
		print "Not an Option...Sorry!"
		print ""

while True:
        time.sleep(3)
	print ""
	print \
	"""
	|****************************|
	|Author:Josh Ambush
	|https://github.com/joshambush/
	| joshambush5435@gmail.com
	|by-: joshambush
	|______________________________|
	"""
	restart = raw_input("Enter Program? (y/n): ")

	if restart == "y":
		main()
	else:
		exit()


main()
