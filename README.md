# Pyinstaller tutorial
Includes an example Python application to be bundled (CantonFavs) and instructions for bundling them into an executable. The resulting executable can be distributed so that the end user can use it without installing Python or any modules.

Note that although Pyinstaller can be used for Windows, Mac, and Linux systems, I only tried on Windows and Mac -- The example and instructions in this tutorial appear to work well for Windows but there are some issues on Mac (see bottom section below).


## Example Python application to be bundled
This example application "CantonFavs" suggests an activity to do in Canton, Ohio based on user-input preferences. Files for the application are:
* CantonFavs_GUI.py	-- main script
* cantonfavslib.py	-- module with functions for meat of the program
* data_and_images.py	-- module for listing and changing data and image files
* canton_activities.txt	-- data file containing info about activities in Canton (INCOMPLETE, as you may notice many "TBD"s)
* football.png		-- image file for corner of GUI window and bottom of screen (application icon, probably should be .ico file actually)
* downtown_canton_ariel_web_size__large.png	-- image file for splash screen

## Information about Pyinstaller, specific to the example application
Files:
* pyinstaller_presentation_summer2020.pdf -- presentation slides for the June 9, 2020 talk
* Instructions_make_executable_CantonFavs_example.txt -- details how to use pyinstaller to make CantonFavs application into executable, especially useful if you like to sleep during presentations or your Internet connection fizzles
* CantonFavs_GUI.spec -- can be used with pyinstaller to expedite and modify the way that pyinstaller builds the CantonFavs executable

## Known issues with this example
Results will likely differ according to operating systems and versions of Python, Pyinstaller, and your other modules, but here is what I'm getting:
* Currently seems to be fully operational on Windows 10, 64 bit, both before and after bundling.
* Unresolved problems on Mac (Version 10.15.4) before bundling:
  * In CantonFavs_GUI.py, the splash screen does not work. If it's commented out, the scripts otherwise run normally.
* Problems on Mac (Version 10.15.4) in process of and/or after bundling:
  * Issues with loading modules related to tkinter leads to failure for app to launch GUI -- resolved by adding binaries=[('/System/Library/Frameworks/Tk.framework/Tk', 'tk'), ('/System/Library/Frameworks/Tcl.framework/Tcl', 'tcl')], and hiddenimports=['tkinter','tkinter.ttk'], to .spec file
  * After above resolution, the bundled CantonFavs_GUI.app only partially works -- the input window appears but the "Get Best Activity" button fails when pressed
  * Also after above resolution, the bundled CantonFavs_GUI Unix executable mostly works but it 1) fails to write output file of results -- when run from command line, the Unix executable will write the output file -- and 2) keeps console window
