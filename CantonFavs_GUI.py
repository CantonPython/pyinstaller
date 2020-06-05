##############################################################################
# file: CantonFavs_GUI.py 
# author: maureen morton
# date: 05/02/2020 first draft
#       05/19/2020 adding input and results windows
#
# purpose: To make GUI for the cantonfavs program, using cantonfavslib module
##############################################################################

import tkinter as tk
from tkinter import ttk
from tkinter import *

import os

import data_and_images

import cantonfavslib

##############################################################################
# Class definition for SplashScreen
# purpose: create a splash screen to display before GUI input screen loads
##############################################################################
class SplashScreen(Frame):
    def __init__(self, master=None, width=0.8, height=0.6, useFactor=True):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=BOTH, expand=YES)

        # get screen width and height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        w = (useFactor and ws*width) or width
        h = (useFactor and ws*height) or height
        # calculate position x, y
        x = (ws/2) - (w/2) 
        y = (hs/2) - (h/2)
        self.master.geometry('%dx%d+%d+%d' % (w/1.1, h/1.1, x, y))
        
        self.master.overrideredirect(True)
        self.lift()

##############################################################################
# Class definition for the main application controller
# purpose: This class is used to load and switch between the application forms
##############################################################################

class CantonFavs_APP(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "CantonFavs")
        ##### Logo image for upper left of GUI window #####
        logophoto = PhotoImage(file=data_and_images.UpperLeftPhoto())
        self.wm_iconphoto(False,logophoto)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand= True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # create a dictionary that holds the windows
        self.frames = {}
        
        for F in (InputWindow, ResultsWindow):
           frame = F(container, self)
           self.frames[F] = frame
           frame.grid(row=0, column = 0, sticky = "nsew")
        ######################## create a pulldown menu, and add it to the menu bar
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=container.quit)
        self['menu'] = menubar

        self.show_frame(InputWindow)
        return

           
    def show_frame(self, cont): # from CantonFavs_APP class
    
        frame = self.frames[cont]
        frame.tkraise()
        return

    def get_frame_data(self, cont): # from CantonFavs_APP class
    
        frame = self.frames[cont]
        params = frame.params.get()
        return

##############################################################################
# Class definition for the InputWindow
# purpose: This class is used to define the input window
##############################################################################

class InputWindow(ttk.Frame):

    def __init__(self, root, controller):
  
        ttk.Frame.__init__(self, root)

        ######################## the main frame for the window
        mainframe = ttk.Frame(self, padding=(3,3,12,12))
        mainframe.grid(column=0, row=0, sticky = "nsew")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)


        # User's entries jobframe
        user_info = ttk.Frame(mainframe)
        user_info.grid(row=1, sticky="nwe", columnspan=5)

        ttk.Label(user_info, text="Find an activity to enjoy in Canton, Ohio!").grid(column=0, row=0, sticky="w")
        
        ttk.Label(user_info, text="What's your name?").grid(column=0, row=1, sticky = "w")
        self.your_name = tk.StringVar()
        your_name = ttk.Entry(user_info, width = 10, textvariable = self.your_name)
        your_name.grid(column=1, row=1, sticky = "w")

        ttk.Label(user_info, text="What kind of activity do you want to do?").grid(column=0, row=2, sticky = "w")
        self.your_category = tk.StringVar()
        choices_category = ["Outdoors", "Sports", "Shopping", "Museums", \
                                  "Music", "Eat", "Arts", "Nerdy", "Surprise me!"]
        self.your_category.set("") # set the default option
        popupMenu_category = tk.OptionMenu(user_info, self.your_category, *choices_category)
        popupMenu_category.grid(column=1, row=2, sticky = "w")

        ttk.Label(user_info, text="What price range do you want?").grid(column=0, row=3, sticky = "w")
        self.your_price = tk.StringVar()
        choices_price = ["Free", "Low $", "Medium $$", "High $$$", "Any"]
        self.your_price.set("") # set the default option
        popupMenu_price = tk.OptionMenu(user_info, self.your_price, *choices_price)
        popupMenu_price.grid(column=1, row=3, sticky = "w")

        ttk.Label(user_info, text="What season do you want?").grid(column=0, row=4, sticky = "w")
        self.your_season = tk.StringVar()
        choices_season = ["Spring", "Summer", "Fall", "Winter", "Any"]
        self.your_season.set("")
        popupMenu_season = tk.OptionMenu(user_info, self.your_season, *choices_season)
        popupMenu_season.grid(column=1, row=4, sticky = "w")
       
        # make padding
        for child in user_info.winfo_children():
            child.grid_configure(padx=5, pady=5)

        ######################## run frame
        run_frame = ttk.Frame(mainframe)
        run_frame.grid(row=4, sticky = "nwe", columnspan=2)

        ttk.Button(run_frame, text='Get Best Activity', \
                   command= lambda: self.search_activities(controller)).grid(column=0, row=0, sticky = "w")

        # make padding
        for child in run_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # make padding
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    ##########################################################################
    # routine: get_variables
    # (from InputWindow class)
    # purpose: takes the information populated by the user in the GUI and 
    #          stores the input variables into the main datastructure variables
    ##########################################################################

    def get_variables(self): 
        try:
            # variables from InputWindow

            variables['name']               = self.your_name.get()
            variables['category']           = self.your_category.get()
            variables['price']              = self.your_price.get()
            variables['season']             = self.your_season.get()
            if variables['category'] == "Outdoors":
                variables['category'] = 1
            elif variables['category'] == "Sports":
                variables['category'] = 2
            elif variables['category'] == "Shopping":
                variables['category'] = 3
            elif variables['category'] == "Museums":
                variables['category'] = 4
            elif variables['category'] == "Music":
                variables['category'] = 5
            elif variables['category'] == "Eat":
                variables['category'] = 6
            elif variables['category'] == "Arts":
                variables['category'] = 7
            elif variables['category'] == "Nerdy":
                variables['category'] = 8
            elif variables['category'] == "Surprise me!":
                variables['category'] = 9

            if variables['price'] == "Free":
                variables['price'] = 1
            elif variables['price'] == "Low $":
                variables['price'] = 2
            elif variables['price'] == "Medium $$":
                variables['price'] = 3
            elif variables['price'] == "High $$$":
                variables['price'] = 4
            elif variables['price'] == "Any":
                variables['price'] = 5
                
            if variables['season'] == "Spring":
                variables['season'] = 1
            elif variables['season'] == "Summer":
                variables['season'] = 2
            elif variables['season'] == "Fall":
                variables['season'] = 3
            elif variables['season'] == "Winter":
                variables['season'] = 4
            elif variables['season'] == "Any":
                variables['season'] = 5
                
        except ValueError:
            pass

    ##########################################################################
    # routine: search_activities
    # (from InputWindow class)
    # purpose: takes the variables, and runs the CantonFavs library and
    #       calls the results window
    ##########################################################################

    def search_activities(self,controller):

        try:
            self.get_variables()

            cantonfavslib.main(variables)  

            controller.frames[ResultsWindow].display_results()
            controller.show_frame(ResultsWindow)

        except KeyError:
            pass
        return

##############################################################################
# Class definition for the Results Window
# purpose: This class is used to define the results window
##############################################################################

class ResultsWindow(ttk.Frame):

    def __init__(self, root, controller):
  
        ttk.Frame.__init__(self, root)

        ######################## the main frame for the window
        self.mainframe = ttk.Frame(self, padding=(3,3,12,12))
        self.mainframe.grid(column=0, row=0, sticky = "nwes")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        ######################## results main frame
        self.yourname = tk.StringVar()
        yourname = ttk.Label(self.mainframe, textvariable= self.yourname)
        yourname.grid(column=0, row=0, columnspan=2 ,sticky = "we")

        ######################## Results 1 frame
        results_frame1 = ttk.Labelframe(self.mainframe, text = "")
        results_frame1.grid(column=0, row=1, sticky = "nwes")
        results_frame1['relief'] = 'solid'

        self.name = tk.StringVar()
        name = ttk.Label(results_frame1, textvariable = self.name)
        name.grid(column=0, row=1, sticky = "we")
        
        self.echo_input = tk.StringVar()
        echo_input = ttk.Label(results_frame1, textvariable = self.echo_input)
        echo_input.grid(column=0, row=2, sticky = "we")

        self.best = tk.StringVar()
        best = ttk.Label(results_frame1, textvariable = self.best)
        best.grid(column=0, row=3, sticky = "we")

        for child in results_frame1.winfo_children():
            child.grid_configure(padx=10, pady=10)

        ######################## try again frame
        return_frame = ttk.Frame(self.mainframe)
        return_frame.grid(row=7, sticky = "nwe", columnspan=2)

        ttk.Button(return_frame, text='Try again', \
                   command=lambda: self.go_back(controller)).grid(column=0, row=0, sticky = "w")

        # make padding
        for child in return_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

        ## make padding
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    ##########################################################################
    # routine: display_results
    # (from ResultsWindow class)
    # purpose:    
    ##########################################################################

    def display_results(self):

        self.name.set("Hi, " + variables['name'] + "!")

        self.echo_input.set(variables['echo_input'])
        self.best.set(variables['best'])

    ##########################################################################
    # routine: go_back
    # (from ResultsWindow class)
    # purpose: Return to the input window to start over
    ##########################################################################

    def go_back(self,controller):

        try:
            controller.show_frame(InputWindow)

        except KeyError:
            pass

        return
       

########################################
# Running the splash screen
#   from: www.sunjay-varma.com
# THIS DOESN'T WORK ON MAC; I DON'T KNOW WHY
########################################
if __name__ == '__main__':
    rootsplash = Tk()

    sp = SplashScreen(rootsplash)
    sp.config(bg="light goldenrod")
    logophoto = PhotoImage(file=data_and_images.SplashScreenPhoto()).zoom(x=1,y=1)
                # .zoom makes image bigger/smaller, whole #'s only
    rootsplash.wm_iconphoto(False,logophoto)
    m = Label(sp,image=logophoto)
    #(sp, text="This is a test of the splash screen\n\n\nThis is only a test.\nwww.sunjay-varma.com")
    m.pack(side=TOP, expand=YES)
    m.config(bg="light goldenrod", justify=CENTER, font=("calibri", 29))
    m.image = logophoto
##    m.place(x=0,y=0) # specifies location
    Button(sp, text="Click HERE to find an activity in Canton, Ohio!", bg='red', command=rootsplash.destroy).pack(side=BOTTOM, fill=X)
    rootsplash.mainloop()

########################################
# Running the program
########################################
variables = {}
app = CantonFavs_APP()
app.mainloop()
