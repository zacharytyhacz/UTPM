import sys
import datetime
import json
import os
import pprint

commands = ['setup','make','create','install','--help','require']
make_methods = ["u","int","ini"]

arg_num = 0
version = 1
settings = os.path.expanduser('~/.utpm.json')
settings_data = {}

# Create a new project folder
# 
# Creates Classes folder, utpm.proj file
def create(project_name):
	print("\n Starting a new awesome mod...")

	project = {}
	project['name'] = project_name

	if os.path.exists(settings_data['utdir'] + '/' + project['name']):
		print(settings_data['utdir'] + '/' + project['name'])
		print("ERROR: This project folder already exists within your Unreal Tournament directory.")
		return
	proj_dir = settings_data['utdir'] + '/' + project['name']
	project['authors'] = raw_input("Enter author or authors: ")
	project['description'] = raw_input("Enter project description: ")

	# create main project folder 
	os.makedirs(proj_dir)

	# create classes folder 
	os.makedirs(proj_dir + "/Classes")
	os.makedirs(proj_dir + "/Models")
	os.makedirs(proj_dir + "/Sounds")
	os.makedirs(proj_dir + "/Textures")
	
	proj_file =  open(proj_dir + "/utpm.proj","w+")
	json.dump(project,proj_file)
	proj_file.close()
	del proj_file

	create_readme = raw_input("Create README.md? Y/N: ")
	if create_readme[0].lower() == 'y':
		readme = open(proj_dir + "/README.md","w+")
		readme.write(str(datetime.date.today()) + "\n" + project['name'] + " by " + project['authors'] + "\n")
		readme.write(str(project['description']) + "\n\n")
		readme.close()
		del readme

	# check if this project name already exists
	# create Classes folder 
	# create readme.md file
	# create utpm.proj file 

# Set user's UT directory and create a .utpm.json local file to hold local data 
def get_settings():
	global settings_data
	if os.path.exists(settings):
		with open(settings) as raw:
			settings_data = json.load(raw)
			print(settings_data['utdir'])
			return True 
	return False

def setup ():
    global settings_data
    if get_settings() == True:
            print("Unreal Tournament Directory: ", settings_data['utdir'])
            print("Version: ", settings_data['version'])
            print("\nChange existing UT Package Manager settings?\n")
            answer = raw_input("\n\n Y/N: ")

            if answer[0].lower() != "y":
                    return 

    credits()
    new_settings = {}
    new_settings['version'] = version
    new_settings['utdir'] = '12123123123'

    while os.path.exists(new_settings['utdir']) == False:
            new_settings['utdir'] = raw_input("Enter the absolute path to your Unreal Tournament game directory: ")
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
		
# show credits / info
def credits ():
	print("\n\n Zachary Tyhacz 2019")
	print("Thank you for choosing UTPM!")
	print("\n If you would like to contribute to the UTPM project with edits, suggestions, comments, issues, fixes, or documentation please feel free to visit the Github!")
	print("\n GITHUB: https://github.com/zacharytyhacz/UTPM ")
	print("\n\n")

command = ""
make_method = ""

if get_settings() == False:
    setup()
for arg in sys.argv:
	print(settings_data['utdir'])
	print(arg)
	print(str(arg_num))
	if arg_num > 0:
		# get command name
		if arg_num == 1:
			command = arg.lower().split(':')[0]
			if command not in commands:
				print("\n" + command)
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
		elif arg_num == 2: # get arguments 
			if command == 'create':
				create(arg)	
	arg_num += 1
