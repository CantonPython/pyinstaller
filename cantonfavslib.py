##############################################################################
# file: cantonfavslib.py 
# author: maureen morton
# date: 05/19/2020
#
# purpose: Library for carrying out: "To provide options of what to do today
#   in Canton, based on user's input characteristics"
#   in conjunction with GUI script
##############################################################################s
import pandas as pd
from random import randint
import data_and_images

##############################################################################
# function: main()
##############################################################################
def main(variables):
##    # Set dictionary to store variables
##    variables = {}
##    # Get user input
##    your_input(variables)
    # Read file of activities
    gather_activities(variables)
    # Use user input to choose category
    choose_category(variables)
    # Use user input to choose price range
    choose_price(variables)
    # Use user input to choose time of year (season)
    choose_season(variables)
    # Output the "best" activities to do today based on user input
    best_activities(variables)

    
##############################################################################
# function: your_input
# purpose: get user input
##############################################################################    
def your_input(variables):
    print('\nGreetings! Let\'s look at what you could do in Canton today!\n')
    variables['name'] = input('\nWhat\'s your name?\n')
    variables['category'] = int(input('\nType the number of the category you ' +\
                                  'want:\n'+\
                                  '1 Outdoors, 2 Sports, 3 Shopping, 4 Museums,' +\
                                  ' 5 Music, 6 Eat, 7 Arts, 8 Nerdy, 9 Surprise me!\n'))
    variables['price'] = int(input('What price range do you want? (Type the number) \n' +\
                              '1 Free, 2 Low $, 3 Medium $$, 4 High $$$, 5 Any\n'))
    variables['season'] = int(input('What season is it? (Type the number) \n' +\
                                '1 spring, 2 summer, 3 fall, 4 winter, 5 any\n'))

##############################################################################
# function: gather_activities
# purpose: Read the file with activities and their characteristics
############################################################################## 
def gather_activities(variables):
    variables['filename'] = data_and_images.TextFile()
    variables['data'] = pd.read_csv(variables['filename'],delimiter='\t')
    
##############################################################################
# function: choose_category
# purpose: Use user input to choose category
##############################################################################    
def choose_category(variables):
    if variables['category'] == 1:
        variables['cat_str'] = "Outdoors"
    elif variables['category'] == 2:
        variables['cat_str'] = "Sports"
    elif variables['category'] == 3:
        variables['cat_str'] = "Shopping"
    elif variables['category'] == 4:
        variables['cat_str'] = "Museums"
    elif variables['category'] == 5:
        variables['cat_str'] = "Music"
    elif variables['category'] == 6:
        variables['cat_str'] = "Eat"
    elif variables['category'] == 7:
        variables['cat_str'] = "Arts"
    elif variables['category'] == 8:
        variables['cat_str'] = "Nerdy"
    # Surprise me! category:
    elif variables['category'] == 9:
        value = randint(1,9)
        if value == 1:
            variables['cat_str'] = "Outdoors"
        elif value == 2:
            variables['cat_str'] = "Sports"
        elif value == 3:
            variables['cat_str'] = "Shopping"
        elif value == 4:
            variables['cat_str'] = "Museums"
        elif value == 5:
            variables['cat_str'] = "Music"
        elif value == 6:
            variables['cat_str'] = "Eat"
        elif value == 7:
            variables['cat_str'] = "Arts"
        elif value == 8:
            variables['cat_str'] = "Nerdy"

    

##############################################################################
# function: choose_price
# purpose: Use user input to choose price range
##############################################################################    
def choose_price(variables):
    if variables['price'] == 1:
        variables['pri_str'] = "Free"
    elif variables['price'] == 2:
        variables['pri_str'] = "Low"
    elif variables['price'] == 3:
        variables['pri_str'] = "Medium"
    elif variables['price'] == 4:
        variables['pri_str'] = "High"
    # "Any", choose randomly
    elif variables['price'] == 5:
        value = randint(1,4)
        if value == 1:
            variables['pri_str'] = "Free"
        elif value == 2:
            variables['pri_str'] = "Low"
        elif value == 3:
            variables['pri_str'] = "Medium"
        elif value == 4:
            variables['pri_str'] = "High"

##############################################################################
# function: choose_season
# purpose: Use user input to choose time of year (season)
##############################################################################    
def choose_season(variables):
    if variables['season'] == 1:
        variables['sea_str'] = "Spring"
    elif variables['season'] == 2:
        variables['sea_str'] = "Summer"
    elif variables['season'] == 3:
        variables['sea_str'] = "Fall"
    elif variables['season'] == 4:
        variables['sea_str'] = "Winter"
    elif variables['season'] == 5:
        variables['sea_str'] = "Any"

##############################################################################
# function: best_activities
# purpose: Output the "best" activities to do today based on user input
##############################################################################    
def best_activities(variables):
    filename = 'Canton_activities_for_' + variables['name'] + '.txt'
    with open(filename, 'w') as wf:
        wf.write('\nHi, '+ variables['name']+ '!\n')
        # print('\nHi,', variables['name'], '!\n')
        if variables['season'] == 1:
            season = 'the spring'
        elif variables['season'] == 2:
            season = 'the summer'
        elif variables['season'] == 3:
            season = 'the fall'
        elif variables['season'] == 4:
            season = 'the winter'
        elif variables['season'] == 5:
            season = 'any'
        if variables['price'] == 1:
            price = 'no' # free
        elif variables['price'] == 2:
            price = 'a low'
        elif variables['price'] == 3:
            price = 'a medium'
        elif variables['price'] == 4:
            price = 'a high'
        elif variables['price'] == 5:
            price = 'any'
        if variables['category'] == 1:
            cat = 'outdoors'
        elif variables['category'] == 2:
            cat = 'sports'
        elif variables['category'] == 3:
            cat = 'shopping'
        elif variables['category'] == 4:
            cat = 'museums'
        elif variables['category'] == 5:
            cat = 'music'
        elif variables['category'] == 6:
            cat = 'eat'
        elif variables['category'] == 7:
            cat = 'arts'
        elif variables['category'] == 8:
            cat = 'nerdy'
        elif variables['category'] == 9:
            cat = 'surprise me!'
        variables['echo_input'] = 'You wanted an activity for ' + season + ' season, that has '\
                                  + price + ' price,\nin the category of: '+ cat+'\n'
        wf.write(variables['echo_input'])
        best = variables['data'].loc[(variables['data']["Price"]==variables['pri_str']) & \
                                     (variables['data']["Season"]==variables['sea_str']) & \
                                     (variables['data']["Category"]==variables['cat_str']) \
                                     ,["Activity"]]
        variables['best'] = 'Therefore, CantonFavs recommends you try the following activities:\n'\
                            + best.to_string(index=False, header=False)
        wf.write(variables['best'])

        
