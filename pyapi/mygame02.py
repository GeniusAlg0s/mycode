#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

#riddle
def riddle():
    print("answer correctly only one try  and recieve a game changing prize")
    print("what is always coming but never arrives")
    answer = input("? :")
    if answer.lower()  == "tomorrow":
        print("correct takes some spoiled monster juice")
        inventory.append("juice")
        answered = 1
    else:
        print("you have failed play on")
        answered = 1
        


def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  teleport [rooms{hall,kitchen,dining room, garden, pantry}]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
      #the + was changed to + to allow more then one item in a room
    print('You see a ' , rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : ['key']
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : ['potion','sword'],
                  'north': 'Pantry',
                  'east' : 'Trap Door',
               },
            'Trap Door' : {
                  'south' : 'Field'
                },
            'Garden' : {
                  'north' : 'Dining Room',
                  'east'  : 'Field',
                  'item'  : ['pale'],
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : ['cookie','milk'],
               },
            'Field' : {
                  'west' :'Garden',
                  'item' :['cow'],
               }, 
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

answered = 0
#loop forever
while True:
  while answered == 0:
        riddle()
        answered = 1
    
  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #TELEPORT- if the move is 'teleport and the move[1] in rooms go there
  if move[0] == 'teleport':
      #check if room exist
      move[1] = move[1].title()
      print(move)
      if move[1] in rooms.keys():
          #set current room to room
          currentRoom = move[1]
      else:
          print("there is no such place")

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      #del rooms[currentRoom]['item']

      #NEW DELETE- instead of del use the remove method to take away that item
      rooms[currentRoom]['item'].remove(move[1])
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'juice' in inventory:
      print("there is the monster in the room ....you drank the juice it teleported you back to hall. YOU WILL NOT BE SAVED TWICE!!")
      inventory.remove("juice")
      currentRoom = 'Hall'
      continue
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'milk' in inventory:
      print("the monster took the milk it was stale from siiting out the monster has died! YOU Win!!")
      break
  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
