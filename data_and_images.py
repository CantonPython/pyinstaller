##############################################################################
# file: data_and_images.py 
# author: maureen morton
# date: 05/02/2020
#
# purpose: To incorporate image files and data files into executable
##############################################################################
# Resource:
# https://stackoverflow.com/questions/51060894/adding-a-data-file-in-pyinstaller-using-the-onefile-option

import sys
import os

##############################################################################
# functions: resource_path and print_file
# purpose: get file path of input filename (necessary functions)
##############################################################################
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # For dev
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def print_file(file_path):
    """ This may be redundant, but see commented out sample below """
    file_path = resource_path(file_path)
    return file_path

##############################################################################
# functions:
# purpose: these functions are called in main script so that filenames can
#   be easily found and changed in this module (optional, but very helpful!)
##############################################################################
def UpperLeftPhoto():
    file_path = print_file('football.png')
    return file_path

def SplashScreenPhoto():
    file_path = print_file('downtown_canton_ariel_web_size__large.png')
    return file_path

def TextFile():
    file_path = print_file('canton_activities.txt')
    return file_path

##############################################################################
# The following is from the above-mentioned website...
##############################################################################
### data_files/data.txt
##hello
##world
##
### myScript.py
##import sys
##import os
##
##def resource_path(relative_path):
##    """ Get absolute path to resource, works for dev and for PyInstaller """
##    try:
##        # PyInstaller creates a temp folder and stores path in _MEIPASS
##        base_path = sys._MEIPASS
##    except Exception:
##        base_path = os.path.abspath(".")
##
##    return os.path.join(base_path, relative_path)
##
##def print_file(file_path):
##    file_path = resource_path(file_path)
##    with open(file_path) as fp:
##        for line in fp:
##            print(line)
##
##if __name__ == '__main__':
##    print_file('data_files/data.txt')
