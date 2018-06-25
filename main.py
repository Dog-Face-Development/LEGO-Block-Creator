#Prompt
INPUTmain = input('LEGO CMD: ')

#Functions to answer commands
if INPUTmain == 'newpiece': #the 'newpiece' command
    global INPUTnewpiece #create global var
    global INPUTnewpiececount #create global var
    global INPUTnewpiececolour #create global var
    INPUTnewpiece = str(input('Name the piece you would like to add: ')) #ask for name
    INPUTnewpiececolour = str(input('What is the piece colour (make sure this colour is in the colour database, otherwise add new using \'newcolour\')? ')) #ask for colour
    INPUTnewpiececount = int(input('How many of that would you like to add? ')) #ask for qty
    print('A new piece has been created named:', '"' + INPUTnewpiece + '",', 'in the colour:', '"' + INPUTnewpiececolour + '",', 'in the quantity of:', INPUTnewpiececount) #check with user to make sure input ok
    
elif INPUTmain == 'newcolour': #the 'newcolour' command
    global INPUTnewcolour #create global var
    INPUTnewcolour = str(input('Name the colour you would like to add: ')) #ask for colour name
    print('A new colour had been created named:', '"' + INPUTnewcolour + '".') #check with user to make sure input ok
elif INPUTmain == 'newcolor': #the 'newcolor' command
    INPUTnewcolour = str(input('Name the color you would like to add: ')) #ask for colour name
    print('A new color had been created named:', '"' + INPUTnewcolour + '".') #check with user to make sure input ok

elif INPUTmain == 'addpiece': #the 'addpiece' command
    global INPUTpiecename #create global var
    global INPUTpiececolour #create global var
    global INPUTpiececount #create global var
    INPUTpiecename = str(input('What is the name of the piece that you would like to add to? ')) #ask for piece name
    INPUTpiececolour = str(input('What is the piece colour? ')) #ask for piece colour
    INPUTpiececount = int(input('How many of that piece do you want to add? ')) #ask for piece qty
    print(INPUTpiececount, 'pieces have been added to:', '"' + INPUTpiecename + '",', 'in the colour of:', '"' + INPUTpiececolour + '".') #check with user to make sure input ok

elif INPUTmain == 'removepiece': #the 'removepiece' command
    INPUTpiecename = str(input('What is the name of the piece that you would like to remove? ')) #ask for piece name
    INPUTpiececolour = str(input('What is the piece colour? ')) #ask for piece colour
    INPUTpiececount = int(input('How many of that piece do you want to remove? ')) #ask for piece qty
    print(INPUTpiececount, 'pieces have been removed from:', '"' + INPUTpiecename + '",', 'in the colour of:', '"' + INPUTpiececolour + '".') #check with user to make sure input ok

elif INPUTmain == 'sort-all': #the 'sort-all' command
    PIECESall = {'piecename':'piecenames', 'piececolour':'piecescolour', 'piececount':'noofpieces'} #create dictionary of pieces requested
    print('Here are all the pieces in the database:', PIECESall) #return specified results

elif INPUTmain == 'sort-name': #the 'sort-name' command
    global INPUTsearch #create global var
    INPUTsearch = str(input('Please enter a brick name: ')) #search bar to sort by name
    PIECESbyname = {'piecename':'piecenamescontainingINPUTsearch', 'piececolour':'piecescolour', 'piececount':'noofpieces'} #create dictionary of pieces requested
    print('The following results were found for this search keyword:', '"' + INPUTsearch + '", \n', PIECESbyname) #return specified results

elif INPUTmain == 'sort-colour': #the 'sort-colour' command
    INPUTsearch = str(input('Please enter a brick colour: ')) #search bar to sort by colour
    PIECESbycolour = {'piecename':'piecenames', 'piececolour':'piecescolourcontainingINPUTsearch', 'piececount':'noofpieces'} #create dictionary of pieces requested
    print('The following results were found for this colour:', '"' + INPUTsearch + '", \n', PIECESbycolour) #return specified results
elif INPUTmain == 'sort-color': #the 'sort-color' command
    INPUTsearch = str(input('Please enter a brick color: ')) #search bar to sort by colour
    PIECESbycolour = {'piecename':'piecenames', 'piececolour':'piecescolourcontainingINPUTsearch', 'piececount':'noofpieces'} #create dictionary of pieces requested
    print('The following results were found for this color:', '"' + INPUTsearch + '", \n', PIECESbycolour) #return specified results

elif INPUTmain == 'help': #the 'help' command
    print('You have entered the help area! Here is a list of commands for your reference:') #help title
    print('"newpiece" - creates a new piece in the database. \n"newcolour/newcolor" - creates a new colour in the database. \n"addpiece" - adds more of your selected piece to the database. \n"removepiece" - removes a quantity of your selected piece from the database. \n"sort-all" - prints all pieces and their respective colours and quantities to the screen. \n"sort-name" - prints all pieces related to the search query entered, as well as their respective colours and quantities to the screen. \n"sort-colour/sort-color" - prints all pieces in that colour, as well as their respective names and quantities. \n"help" - prints a list of commands, and is where you are right now.') #list of functions

elif INPUTmain == 'copyright' or 'license':
    print('Copyright (C) 2018 Dog Face Development Co. \nUse is subject to the terms and conditions outlined in the LICENSE.md document.')

else:
    print('Sorry, try again! \nType "help" for a list of commands.') #helpful error message