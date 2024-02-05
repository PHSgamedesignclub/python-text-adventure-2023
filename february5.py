#This is where the code will be for the text adventure
#By the way, a good coding practice is to leave comments explaining parts of code
#To write a comment, just put a hashtag, then text directly after
#These are comments

import random #do not delete this, i will explain what it is later

#write your code starting from line 10

print("""
commands:
go [direction] (up, down, north, south, east, west)
get [object]
to win, you have to find all the objects and escape the house
also you are kirby but he inhaled josh hutcherson
""")

currentRoom = "Back Entry"

def showStatus(): 
  print("You are in the", currentRoom)

  if "item" in rooms[currentRoom]:
    print("There is a " + rooms[currentRoom]["item"])
  print("Inventory: ", end=" ")
  print(inventory)

rooms = {
  "Back Entry" : {
    "south" : "Backyard",
    "north" : "Torture Chamber",
    "east" : "Exit",
    "west" : "Closet",
  },
  
  "Backyard" : {
    "north" : "Back Entry",
    "item" : "weapons-grade uranium maiden",
    "south" : "Secret Gate",
  },

  "Secret Gate" : {
    "north" : "Backyard",
    "east" : "Josh Hutcherson Shrine Room",
    "west" : "Shrek Shrine Room",
  },

  "Shrek Shrine Room" : {
    "east" : "Secret Gate",
    "down" : "Shrock Shrine Room",
  },

  "Shrock Shrine Room" : {
    "up" : "Shrek Shrine Room",
    "item" : "Shrock",
  },

  "Josh Hutcherson Shrine Room" : {
    "west" : "Secret Gate",
    "item" : "photo of josh hutcherson",
  },
  
  "Torture Chamber" : {
    "south" : "Back Entry",
    "item" : "karaoke machine",
    "west" : "Stair Room",
  },

  "Stair Room" : {
    "east" : "Torture Chamber",
    "down" : "Basement",
  },

  "Basement" : {
    "up" : "Stair Room",
  },
  
  "Exit" : {
    "west" : "Back Entry",  
    "east" : "Dying Room",
    "north" : "Living Room",
    "south" : "Room of Rooms",
  },

  "Dying Room" : {
    "west" : "Exit",
    "north" : "Room of the Dead",
  },

  "Room of the Dead" : {
    "south" : "Dying Room",
    "north" : "Room of the Living Dead",
  },

  "Living Room" : {
    "south" : "Exit",
    "east" : "Room of the Living",
  },

  "Room of the Living" : {
    "south" : "Room of the Living Dead",
    "west" : "Living Room",
  },

  "Room of the Living Dead" : {
    "north" : "Room of the Living",
    "south" : "Room of the Dead",
  },

  "Room of Rooms" : {
    "north" : "Exit",
    "east" : "Room of Rooms",
    "west" : "Room of Rooms",
  },

  "Weight Room" : {
    "item" : "protein powder",
    "north" : "Living Room",
  },
  
  "Closet" : {
    "east" : "Back Entry",
    "north" : "Bathroom",
    "item" : "photo of josh hutcherson",
    "west" : "Bedroom",
  },

  "Bedroom" : {
    "east" : "Closet",
  },

  "Bathroom" : {
    "south" : "Closet",
    "item" : "guillotine",
  }
}

inventory = [];

while True:
  showStatus()

  
  playerCommand = []
  itemList = []
  playerCommandString = input("What do you want to do? ")
  playerCommand = playerCommandString.split(" ")
  
  if playerCommand[0] == "go":
    if playerCommand[1] in rooms[currentRoom]:
      currentRoom = rooms[currentRoom][playerCommand[1]]
    else:
      print("You can't go that way")

  elif playerCommand[0] == "get":
    itemList = rooms[currentRoom]["item"].split(" ")
    item = rooms[currentRoom]["item"]
    if "item" in rooms[currentRoom] and playerCommand[1] == itemList[0]:
      inventory.append(item)
      print("You picked up the " + rooms[currentRoom]["item"])
      del rooms[currentRoom]["item"]

  print()

#go north = ['go','north']
