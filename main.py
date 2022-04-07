"""
LEGO Block Creator
Copyright (C) 2016-2022 @willtheorangeguy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# Import Statements
import os

# Prompt
INPUTmain = input('LEGO CMD: ')

# Functions to Answer Commands
# Piece Commands
if INPUTmain == 'newpiece': # the 'newpiece' command
    global INPUTnewpiece # create global var
    global INPUTnewpiececount # create global var
    global INPUTnewpiececolour # create global var
    INPUTnewpiece = str(input('Name the piece you would like to add: ')) # ask for name
    INPUTnewpiececolour = str(input('What is the piece colour (make sure this colour is in the colour database, otherwise add using "newcolour")? ')) # ask for colour
    INPUTnewpiececount = int(input('How many of that would you like to add? ')) # ask for qty
    print('A new piece has been created named:', '"' + INPUTnewpiece + '",', 'in the colour:', '"' + INPUTnewpiececolour + '",', 'in the quantity of:', INPUTnewpiececount) # check with user to make sure input ok

elif INPUTmain == 'newcolour': # the 'newcolour' command
    global INPUTnewcolour # create global var
    INPUTnewcolour = str(input('Name the colour you would like to add: ')) # ask for colour name
    print('A new colour had been created named:', '"' + INPUTnewcolour + '".') # check with user to make sure input ok
elif INPUTmain == 'newcolor': # the 'newcolor' command
    INPUTnewcolour = str(input('Name the color you would like to add: ')) # ask for colour name
    print('A new color had been created named:', '"' + INPUTnewcolour + '".') # check with user to make sure input ok

elif INPUTmain == 'addpiece': # the 'addpiece' command
    global INPUTpiecename # create global var
    global INPUTpiececolour # create global var
    global INPUTpiececount # create global var
    INPUTpiecename = str(input('What is the name of the piece that you would like to add to? ')) # ask for piece name
    INPUTpiececolour = str(input('What is the piece colour? ')) # ask for piece colour
    INPUTpiececount = int(input('How many of that piece do you want to add? ')) # ask for piece qty
    print(INPUTpiececount, 'pieces have been added to:', '"' + INPUTpiecename + '",', 'in the colour of:', '"' + INPUTpiececolour + '".') # check with user to make sure input ok

elif INPUTmain == 'removepiece': # the 'removepiece' command
    INPUTpiecename = str(input('What is the name of the piece that you would like to remove? ')) # ask for piece name
    INPUTpiececolour = str(input('What is the piece colour? ')) # ask for piece colour
    INPUTpiececount = int(input('How many of that piece do you want to remove? ')) # ask for piece qty
    print(INPUTpiececount, 'pieces have been removed from:', '"' + INPUTpiecename + '",', 'in the colour of:', '"' + INPUTpiececolour + '".') # check with user to make sure input ok

elif INPUTmain == 'sortparts-all': # the 'sortparts-all' command
    PIECESall = {'piecename':'piecenames', 'piececolour':'piecescolour', 'piececount':'numofpieces'} # create dictionary of pieces requested
    print('Here are all the pieces in the database:', PIECESall) # return specified results

elif INPUTmain == 'sortparts-name': # the 'sortparts-name' command
    global INPUTsearch # create global var
    INPUTsearch = str(input('Please enter a brick name: ')) # search bar to sort by name
    PIECESbyname = {'piecename':'piecenamescontainingINPUTsearch', 'piececolour':'piecescolour', 'piececount':'numofpieces'} # create dictionary of pieces requested
    print('The following results were found for this search keyword:', '"' + INPUTsearch + '", \n', PIECESbyname) # return specified results

elif INPUTmain == 'sortparts-colour': # the 'sortparts-colour' command
    INPUTsearch = str(input('Please enter a brick colour: ')) # search bar to sort by colour
    PIECESbycolour = {'piecename':'piecenames', 'piececolour':'piecescolourcontainingINPUTsearch', 'piececount':'numofpieces'} # create dictionary of pieces requested
    print('The following results were found for this colour:', '"' + INPUTsearch + '", \n', PIECESbycolour) # return specified results
elif INPUTmain == 'sortparts-color': # the 'sortparts-color' command
    INPUTsearch = str(input('Please enter a brick color: ')) # search bar to sort by colour
    PIECESbycolour = {'piecename':'piecenames', 'piececolour':'piecescolourcontainingINPUTsearch', 'piececount':'numofpieces'} # create dictionary of pieces requested
    print('The following results were found for this color:', '"' + INPUTsearch + '", \n', PIECESbycolour) # return specified results

    # Set commands
elif INPUTmain == 'newset': # the 'newset' command
    global INPUTnewset # create global var
    global INPUTnewsetnum # create global var
    global INPUTnewsettheme # create global var
    global INPUTnewsetpiececount # create gloabl var
    global INPUTnewsetcount # create global var
    INPUTnewset = str(input('Name the set you would like to add: ')) # ask set name
    INPUTnewsetnum = str(input('What is the set number for the set you would like to add? ')) # ask set number
    INPUTnewsettheme = str(input('What is the theme for the set you would like to add? (make sure this theme is in the database, otherwise add using "newtheme") ')) #ask set theme
    INPUTnewsetpiececount = str(input('How many pieces are there in this set? ')) # ask set piece count
    INPUTnewsetcount = int(input('How many of this set would you like to add? ')) # ask number of sets to add
    print('A new set has been created named:', '"' + INPUTnewset + '",', 'with the set number:', '"' + INPUTnewsetnum + '",', 'in the theme:', '"' + INPUTnewsettheme + '",', 'with the piece count of:', INPUTnewsetpiececount + ',', 'in the quantity of:', INPUTnewsetcount) # check with user to make sure input ok

elif INPUTmain =='newtheme': # the 'newtheme' command
    global INPUTnewtheme # create global var
    INPUTnewtheme = str(input('Name the theme you would like to add: ')) # ask for theme name
    print('A new theme had been created named:', '"' + INPUTnewtheme + '"') # check with user to make sure input ok

elif INPUTmain == 'addset': # the 'addset' command
    global INPUTsetnum # create global var
    global INPUTsetcount # create global var
    INPUTsetnum = str(input('What is the set number of the set that you would like to add? ')) # ask for set number
    INPUTsetcount = int(input('How many of that set do you want to add? ')) # ask for set qty
    print(INPUTsetcount, 'sets have been added to set number:', '"' + INPUTsetnum + '"') # check with user to make sure input ok

elif INPUTmain == 'removeset': # the 'removeset' command
    INPUTsetnum = str(input('What is the set number of the set that you would like to remove? ')) # ask for set number
    INPUTsetcount = int(input('How many of that set do you want to remove? ')) # ask for set qty
    print(INPUTsetcount, 'sets have been removed from set number:', '"' + INPUTsetnum + '"') # check with user to make sure input ok

elif INPUTmain == 'sortsets-all': # the 'sortsets-all' command
    SETSall = {'setname':'setnames', 'setnum':'setnums', 'settheme':'setthemes', 'setpiececount':'numofpieces', 'setcount':'numofsets'} # create dictionary of sets requested
    print('Here are all the sets in the database:', SETSall) # return specified results

elif INPUTmain == 'sortsets-name': # the 'sortsets-name' command
    INPUTsearch = str(input('Please enter a set name (NOT number): ')) # search bar to sort by name
    SETSbyname = {'setname':'setnamescontainingINPUTsearch', 'setnum':'setnums', 'settheme':'setthemes', 'setpiececount':'numofpieces', 'setcount':'numofsets'} # create dictionary of pieces requested
    print('The following results were found for this search keyword:', '"' + INPUTsearch + '", \n', SETSbyname) # return specified results

elif INPUTmain == 'sortsets-number': # the 'sortsets-number' command
    INPUTsearch = str(input('Please enter a set number (NOT name): ')) # search bar to sort by name
    SETSbynum = {'setname':'setnames', 'setnum':'setnumscontainingINPUTsearch', 'settheme':'setthemes', 'setpiececount':'numofpieces', 'setcount':'numofsets'} # create dictionary of pieces requested
    print('The following results were found for this search keyword:', '"' + INPUTsearch + '", \n', SETSbynum) # return specified results

elif INPUTmain == 'sortsets-theme': # the 'sortsets-theme' command
    INPUTsearch = str(input('Please enter a set theme: ')) # search bar to sort by name
    SETSbytheme = {'setname':'setnames', 'setnum':'setnums', 'settheme':'setthemescontainingINPUTsearch', 'setpiececount':'numofpieces', 'setcount':'numofsets'} # create dictionary of pieces requested
    print('The following results were found for this search keyword:', '"' + INPUTsearch + '", \n', SETSbytheme) # return specified results


    # Other commands
elif INPUTmain == 'help': # the 'help' command
    print('You have entered the help area! Here is a list of commands for your reference:')
    print('newpiece - creates a new piece in the database.')
    print('newcolour/newcolor - creates a new colour in the database.')
    print('addpiece - adds a quantity of your selected piece to the database.')
    print('removepiece - removes a quantity of your selected piece from the database.')
    print('sortparts-all - prints all pieces and their respective colours and quantities to the screen.')
    print('sortparts-name - prints all pieces related to the search query entered, as well as their respective colours and quantities to the screen.')
    print('sortparts-colour/sortparts-color - prints all pieces in that colour, as well as their respective names and quantities.')
    print('newset - creates a new set in the database.')
    print('newtheme - creates a new theme in the database. ')
    print('addset - adds a quantity of your selected set to the database.')
    print('removeset - removes a quantity of your selected set from the database.')
    print('sortsets-all - prints all sets and their respective set numbers, themes, piece count and quantity to the screen.')
    print('sortsets-name - prints all the sets related to the set name entered, as well as their respective set numbers, themes, piece count and quantity to the screen.')
    print('sortsets-number - prints all the sets related to the set number entered, as well as their respective set names, themes, piece count and quantity to the screen.')
    print('sortsets-theme - prints all the sets related to the set theme entered, as well as their respective set names, numbers, piece count and quantity to the screen.')
    print('copyright/license"- prints license and copyright information and opens the license in default text editor.')
    print('help - prints this help text')

elif INPUTmain == 'copyright' or 'license': # the 'copyright command'
    print('Copyright (C) 2018-2022 Dog Face Development Co. \nUse is subject to the terms and conditions outlined in the LICENSE.md document.') # copyright info
    os.startfile("") # opens license

else:
    print('Sorry, try again! \nType "help" for a list of commands.') # helpful error message
