#This is where the code will be for the text adventure
#By the way, a good coding practice is to leave comments explaining parts of code
#To write a comment, just put a hashtag, then text directly after
#These are comments

import random #do not delete this, i will explain what it is later

#write your code starting from line 10

print("""
commands:
go [direction]
get [object]
to win, you have to find all the objects and escape the house
""")

currentRoom = "Back Entry"

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
  },
  
  "Torture Chamber" : {
    "south" : "Back Entry",
    "item" : "karaoke machine",
  },
  
  "Exit" : {
    "west" : "Back Entry",  
  },
  
  "Closet" : {
    "east" : "Back Entry",
    "north" : "Bathroom",
    "item" : "photo of josh hutcherson",
  },

  "Bathroom" : {
    "south" : "Closet",
    "item" : "guillotine",
  }
}

inventory = [];

while True:
  print("You are in the", currentRoom)

  if "item" in rooms[currentRoom]:
    print("There is a " + rooms[currentRoom]["item"])
  print("Inventory: ", end=" ")
  print(inventory)

  
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
