# UTPM
Unreal Tournament (99) Package Manager
Easily set up new project folders, install packages/maps/mods in one command.

# Commands 

## __`utpm help`__
See a list of commands and  help about using the Unreal Tournament Package Manager

## __`utpm setup`__
Set your Unreal Tournament main directory.
e.g. C:/Program\ Files/Unreal\ Tournament 

## __`utpm create <project name>`__
Create a new UT project. 
Will create Classes folder and a README.md !  

## __`utpm make:u <project folder name>`__
Will generate the .u for your project and place into your System folder.

## __`utpm make:int <project folder name>`__
Will walk through creating a .int file for your project.
Select a class in the project folder you want to create mutator/game mode/other out of.
Create name and description for the mutator and it will create the .int and place in your System folder.

## __`utpm make:ini <project folder name>`__
Will create a .ini for your project.
Will parse through class files for config variables and set default values and place in your System folder.

# Files 
* These files are JSON formatted *
## __.utpm.json__
This will be placed in your local folder.
( Mac/Linux: ~/.utpm.json )
( Windows: -coming soon )

Keeps track of your UT directory and UTPM version number. Other settings may be implemented.

## __.utpm.proj__
This will be created in the root of a UT project folder.
Contains data about the project name, description, author(s), and possible dependencies.





