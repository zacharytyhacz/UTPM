import sys
import json
import os

commands = ['setup','make','create','install','help','require']


arg_num = 0
version = 1
settings = os.path.expanduser('~/.utpm.json')
settings_data = {}

def create():
	print("\n Starting a new awesome mod...")
	project = {}
	project['name'] = input("Project Name: ")

	while os.path.exists(settings_data['utdir'] + '/' + project['name']) == False:
		print("This project already exists.")
		project['name'] = input("Project Name: ")

	project['author'] = input("Author(s): ")

def setup ():
	if os.path.exists(settings):
		with open(settings) as raw:
			settings_data = json.load(raw)
			print("Change existing UT Package Manager settings?\n")
			print("Unreal Tournament Directory: ", data['utdir'])
			print("Version: ", data['version'])
			del data 
		answer = input("\n\n Y/N: ")

		if answer[0].lower() != "y":
			return 

	credits()
	new_settings = {}
	new_settings['version'] = version
	new_settings['utdir'] = '12123123123'

	while os.path.exists(new_settings['utdir']) == False:
		new_settings['utdir'] = input("Enter the absolute path to your Unreal Tournament game directory: ")
		if os.path.exists(new_settings['utdir']) == False:
			print("Cannot find path, please try again.")
		if os.path.exists(new_settings['utdir'] + '/System') == False:
			new_settings['utdir'] = '12123123123'
			print("Invalid Unreal Tournament folder because 'System' folder does not exist.")
		
	settings_file = open(settings,"w+")
	json.dump(new_settings, settings_file)
	settings_file.close()
	settings_data = new_settings
		
	print("\n\n Unreal Tournament Package Manager successfully set up.")
	print("\n Happy Modding!")
		
def credits ():
	print("\n\n Zachary Tyhacz 2019")
	print("Thank you for choosing UTPM!")
	print("\n If you would like to contribute to the UTPM project with edits, suggestions, comments, issues, fixes, or documentation please feel free to visit the Github!")
	print("\n GITHUB: https://github.com/zacharytyhacz/UTPM ")
	print("\n\n")

command = ""
make_method = ""
make_methods = ["u","int","ini"]

for arg in sys.argv:
	if arg_num > 0:
		if arg_num == 1:
			command = arg.lower().split(':')[0]
			if command not in commands:
				print("ERROR: INVALID COMMAND")
				break
			if command == 'setup':
				setup()
			if command == 'help':
				help()
			if command == 'make': 
				make_method = arg.lower().split(':')[1]
				if make_method not in make_methods:
					print("ERROR: INVALID MAKE:<METHOD>")
					break;

		elif arg_num == 2:
			if command == 'create':
				# check if this project name already exists
				# create Classes folder 
				# create readme.md file
				# create utpm.proj file 
	arg_num =+ 1
		
