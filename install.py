#!/usr/bin/env python
import sys,os
if len(sys.argv)>1:
	try:
		if sys.argv[1]=="-u":
			if os.name=="nt":
				print os.popen("dir C:\\Python*\\Lib\\terminal_virtualface*")
				print "Removing..."
				print "del C:\\Python*\\Lib\\terminal_virtualface*"
				os.system("del C:\\Python*\\Lib\\terminal_virtualface*")
				print os.popen("dir C:\\Python*\\Lib\\terminal_virtualface*")
			else:
				if os.popen('echo $USER','r').read()=="root\n":
					f=os.popen('ls /usr/lib/python*/terminal_virtualface*','r').read().split("\n")
					for a in f:
						if a!="":
							print "rm "+a
							os.system("rm "+a)
					if os.popen('ls /usr/lib/python*/terminal_virtualface*','r').read()=="":
						print "Success."
					else:
						unsuc=os.popen('ls /usr/lib/python*/terminal_virtualface*','r').read().split("\n")
						print "Unsuccess for:"
						for a in unsuc:
							if a!="":
								print a
				else:
					print "Must be root."
			sys.exit()
	except:
		pass
else:
	if os.name=="nt":
		print "Copying..."
		os.system("copy lib\\terminal_virtualface.py C:\\Python*\\Lib")
		if "terminal_virtualface.py" in os.popen('dir C:\\Python*\\Lib\\terminal_virtualface*','r').read():
			print "Success."
		else:
			print "Error."
	else:
		if os.popen('echo $USER','r').read()=="root\n":
			print "Copying..."
			paths=os.popen("ls -d /usr/lib/python*/","r").read().split("\n")
			for a in paths:
				if a!="":
					print "cp terminal_virtualface.py "+a
					os.system("cp terminal_virtualface.py "+a)
			if "terminal_virtualface.py" in os.popen('ls /usr/lib/python*/terminal_virtualface*','r').read():
				print "Success for:"
				suc=os.popen('ls /usr/lib/python*/terminal_virtualface*','r').read().split("\n")
				for a in suc:
					if a!="":
						print a.split("/")[3]
			else:
				print "Error."
		else:
			print "Must be root."