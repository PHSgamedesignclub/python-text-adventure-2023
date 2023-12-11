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
  },
  
  "Torture Chamber" : {
    "south" : "Back Entry",
  },
  
  "Exit" : {
    "west" : "Back Entry",  
  },
  
  "Closet" : {
    "east" : "Back Entry",
  }
}

while True:
  print("You are in the", currentRoom)
  playerCommand = []
  playerCommandString = input("What do you want to do? ")
  playerCommand = playerCommandString.split(" ")
  
  if playerCommand[0] == "go":
    if playerCommand[1] in rooms[currentRoom]:
      currentRoom = rooms[currentRoom][playerCommand[1]]
    else:
      print("You can't go that way")
