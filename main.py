import sys
import json
import os

commands = ['setup','make','create','install','help']


arg_num = 0
version = 1
settings = '~/.utpm.json'
settings_data = {}

for arg in sys.argv:
	if arg_num > 0:
		if arg_num == 1
			if !(arg in commands):
				print("ERROR: INVALID COMMAND")
				break
			if arg == 'setup':
				setup()
	arg_num++
		

def create():
	print("\n Starting a new awesome mod...")
	project = {}
	project['name'] = input("Project Name: ")

	while os.path.exists(settings_data['utdir'] + '/' + project['name']):
		print "This project already exists."
		project['name'] = input("Project Name: ")


	project['author'[ = input("Author(s): ")

def setup():
	if os.path.exists(settings):
		with open(settings) as raw:
			settings_dadta = json.load(raw)
			print "Change existing UT Package Manager settings?\n"
			print "Unreal Tournament Directory: ", data['utdir']
			print "Version: ", data['version']
			del data 
		answer = input("\n\n Y/N: ")

		if answer[0].lower() == "n" || answer[0].lower() == "q":
			return 

	credits()
	new_settings = {}
	new_settings['version'] = version

	print "e.g. C:\Program\ Files\Unreal\ Tournament"
	while !os.path.exists(new_settings['utdir']):
		settings['utdir'] = input("Enter the absolute path to your Unreal Tournament game directory: ")
		if !os.path.exists(new_settings['utdir']):
			print "Cannot find path, please try again."
		if !os.path.exists(new_settings['utdir'] + '\System'):
			print "Invalid Unreal Tournament folder because 'System' folder does not exist."
		
	settings_file = open(settings,"w+")
	settings_file.write(json.dump(new_settings))
	settings_file.close()
	settings_data = new_settings
		
	print "\n\n Unreal Tournament Package Manager successfully set up."
	print "\n Happy Modding!"
		
def credits():
	print "\n\n Zachary Tyhacz 2019"
	print "Thank you for choosing UTPM!"
	print "\n If you would like to contribute to the UTPM project with edits, suggestions, comments, issues, fixes, or documentation please feel free to visit the Github!"
	print "\n\n"	
