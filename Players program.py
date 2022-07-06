# Program to manage a text file registry of players and their details.

# Function to display the main menu.
def initmenu(): 
       print(
        """
            Players Maintenance Menu

                1 - List Players
                2 - Search player by ID
                3 - Add player
                4 - Update player
                5 - Delete player
                6 - Exit

        Enter one of the numbers above to choose an option from the menu.
       """
       )

# Funcion to display the details of a player.
def print_player():
    headers=["ID", "Last Name", "First Name", "Position", "Games Played","Points Scored"]
    underlines = ["---", "----------", "-----------", "---------", "-------------","--------------"]
    players_list = playerfound.copy()
    players_list.insert(0,underlines)
    players_list.insert(0,headers)
    cols_length = [max([len(str(row[i])) for row in players_list]) + 3 for i in range(len(players_list[0]))]
    row_format = "".join(["{:<" + str(cols_length) + "}" for cols_length in cols_length])
    print("\n")
    for row in players_list:
        print(row_format.format(*row))

# Function to display the list of players extracted from a file.
def listPlayers():
    players = []
    # Extract data into a list.
    for i in fullists[:-1]:
        i = i[:-1]
        j = i.split(",")
        j[5] = int(j[5])
        j[4] = int(j[4])
        if j[4] == 0:
            j.append("0,00")
        else:
            j.append("{:.2f}".format(round(j[5]/j[4],2)))
        players.append(j)  
 
    # When the content is in the list it displays it in a tabulated fashion.
    if players:    
        headers=["ID", "Last Name", "First Name", "Position", "Games Played","Points Scored","Average Points Scored"]
        underlines = ["---", "----------", "-----------", "---------", "-------------","--------------","----------------------"]
        players_list = players
        players_list.insert(0,underlines)
        players_list.insert(0,headers)
        cols_length = [
        (max([len(str(row[i])) for row in players_list]) + 3)
        for i in range(len(players_list[0]))
        ]
        row_format = "".join(["{:<" + str(cols_length) + "}" for cols_length in cols_length])
        
        print("\n")
        for row in players_list:
            print(row_format.format(*row))
    # When the file is empty the program displays a message.
    else:
        print("\nThe file is empty, please start adding players.")

# Function to search a player by its ID
def searchplayer():
    global playerId
    global playerfound, file_empty, inputerror
    # Display a message when the list is empty.
    if not fullists[:-1]:
        print("\nThe file is empty, please add players first.")
        file_empty = True 
    else:    
        # Check the input ID for invalid entries.
        file_empty = False
        try:
            playerId = int(input("\nEnter the ID of the player: "))
        except ValueError:
            print("\nError: Please enter a valid ID.")
            inputerror = True  
        else:    
            # Capture the line that matches the ID of the player in a list.
            inputerror = False
            count = 0
            playerfound = []
            while not playerfound and count != fullists.index(fullists[-1]):
                k = fullists[count][:-1].split(",")
                if int(k[0]) == playerId:
                    playerfound.append(k)
                count += 1

# Function to add a player
def addplayer():
    # Autogenerate id from the last line in the list and start assigning unused ids after the id 999 is reached.  
    for pID in fullists:
        pass 
    newID = int(pID[:-1]) + 1
    last_index = fullists.index(pID)
    if last_index == 999:
        print("\nThe program cannot store more players. Please delete some before adding more.")
    else:
        if pID == "1000,":                    
            used_Ids = []       
            for item in range(len(fullists)):            
                used_Ids.append(int(fullists[item].partition(',')[0]))
            
            unUsedId = 1        
            while unUsedId in used_Ids:
                unUsedId += 1
            fullists[-1] = str(unUsedId) + ","
            newID = 1000
        
        # Get the details of the new player and put them into a list.
        newPlayer = []
        userEntry = ""
        while not userEntry.isalpha() or len(userEntry) > 30:
            userEntry = input("\nEnter the last name of the player: ").capitalize()
            if len(userEntry) > 30:
                print("Error: The maximum length is 30 characters. ")
        newPlayer.append(userEntry)
        
        userEntry = ""
        while not userEntry.isalpha() or len(userEntry) > 30:
            userEntry = input("\nEnter the first name of the player: ").capitalize()
            if len(userEntry) > 30:
                print("Error: The maximum length is 30 characters. ")
        newPlayer.append(userEntry)

        userEntry = ""
        while userEntry != "Guard" and userEntry!= "Forward" and userEntry != "Centre":
            userEntry = input("\nEnter the position (Guard, Forward, or Centre): ").capitalize()
        newPlayer.append(userEntry)
            
        userEntry = -1
        while userEntry < 0 or userEntry > 200:
                try:
                    userEntry = int(input("\nEnter the number of games played between 0 and 200 inclusive: "))
                except ValueError:
                    print("Please enter a valid integer between 0 and 200 inclusive")
        newPlayer.append(userEntry)
        if userEntry != 0:
            userEntry = -1
            while userEntry < 0 or userEntry > 1000:
                    try:
                        userEntry = int(input("\nEnter the number of total points scored between 0 and 1000 inclusive: "))
                    except ValueError:
                        print("Please enter a valid integer between 0 and 1000 inclusive")
        else:
            userEntry = 0
        newPlayer.append(userEntry)

        # Transform the list into a string.
        lineToAdd = "" 
        for i in newPlayer:
            lineToAdd += str(i) + ","
        lineToAdd = lineToAdd[:-1]+"\n"
        
        # Add the string to the main list.
        lastindex = fullists[-1]
        fullists[-1] = lastindex + lineToAdd
            
        fullists.append(str(newID)+",")
        
        print("\n\t\tThe new player has been added!")

# Function to update a player
def updateplayer():
    if not file_empty:
        # Display the current details to change.
        global fullists
        if playerfound:
            print("\nThese are the current details of the player:")
            print_player()
            
            # Ask if the user wants to change the items and asks for the new data.             
            change = ["Position", "number of games played", "number of total points scored"]
            global confirmation            
            def confirm_change(to_change):
                global confirmation
                confirmation = ""
                while confirmation not in ("n", "N", "y", "Y"):
                    confirmation = input("\nWould you like to change the "+str(to_change)+"? (Y/N only): ")
            
            # Input to change the position.
            confirm_change(change[0])
            if confirmation in ("y","Y"): 
                new_position = ""
                while new_position not in ("Guard", "Forward", "Centre"):
                    new_position = input("\nEnter a new position (Guard, Forward, or Centre): ").capitalize()
                playerfound[0][3] = new_position
                        
            # input to change the games played and score.
            for i in range(2):
                confirm_change(change[i+1])
                if confirmation in ("y","Y"): 
                    new_gamesNscore = -1
                    while new_gamesNscore < 0 or new_gamesNscore > i*800+200:
                        try:
                            new_gamesNscore = int(input("\nEnter the number of "+str(change[i+1])+ " between 0 and "+str(i*800+200)+" inclusive: "))
                        except ValueError:
                            print("Please enter a valid integer between 0 and "+str(i*800+200)+" inclusive")
                            
                    playerfound[0][i+4] = new_gamesNscore

            # Replace old line with updated one
            # transform list into a single string line
            lineToAdd = "" 
            for item in playerfound[0]:
                lineToAdd += str(item) + ","
            lineToAdd = lineToAdd[:-1] + "\n"
            
            # rewrite list of lines with the new line.
            count = 0
            player_index = ""
            while player_index != str(playerId):
                player_index = fullists[count].partition(',')[0]
                count = count + 1
            if lineToAdd == fullists[count-1]:
                print("\nNo changes have been made.")
            else:                    
                fullists[count-1] = lineToAdd
                print("\nThe player has been updated")
                print_player()
        # Display message when no player matches the ID.    
        else:
            print("\nThere is no player with that ID\n")

# Function to delete a player
def deleteplayer():
    # Show details of the player to delete and ask for confirmation.
    if not file_empty:
        if playerfound:
            print("\nThese are the details of the player to delete:\n")
            print_player()
            confirm_delete = ""                
            while confirm_delete != "n" and confirm_delete != "N" and confirm_delete != "y" and confirm_delete != "Y":
                confirm_delete = input("\nAre you sure you want to delete this player? (Y/N): ")
                if confirm_delete == "y" or confirm_delete == "Y":
                    # Delete the player
                    fullists.remove(','.join(playerfound[0])+"\n")
                    print("\nThe player has been deleted!")
        else:
            print("\nThere is no player with that ID")
        print("\n")            
                    
# Main program
print("\n\t\tWelcome to Blockhouse Bay Basketball Club\n")

# Check for the file and extract data into a list.
try:
    myfile = open("players.txt", "r")
    fullists = myfile.readlines()
    myfile.close()
    
except FileNotFoundError:
    # When a file does not exist it creates one with an ID for the first player.
    myfile = open("players.txt", "w")
    myfile.writelines("1,")
    myfile.close()
    # Show a message indicating that the file is empty.
    print("\nThe file is empty, please start adding players.")
    myfile = open("players.txt", "r")
    fullists = myfile.readlines()
    myfile.close() 
finally:
    # It gives the list a first ID in case the file is empty.
    if not fullists:
        fullists.append("1,")    
    
    # Loop to maintain the program running and calling the functions.
    choice = 0
    while choice!= 6:
        initmenu()
        try:
            choice = int(input("\t\tChoice: "))
        except ValueError:
            print("\nPlease enter one of the options below.")     
        else:
            if choice > 6 or choice < 1:
                print("\nPlease enter one of the options below.")
            elif choice == 1:
                listPlayers()
            
            elif choice == 2:
                searchplayer()
                # Display the details of the player when the ID is on the list of players.
                if not file_empty:
                    if playerfound and not inputerror:                        
                        print_player()
                    elif not playerfound:
                        print("\nThere is no player with that ID")
            
            elif choice == 3:
                addplayer()
            
            elif choice == 4:
                searchplayer()
                updateplayer()
            
            elif choice == 5:
                searchplayer()
                deleteplayer()

    # Write the final list with players into the file when the user exits the program.
    myNewFile = open("players.txt", "w")
    for line in fullists:
        myNewFile.write(line)
    myNewFile.close()        
    input("\nPress Enter to exit.\n")