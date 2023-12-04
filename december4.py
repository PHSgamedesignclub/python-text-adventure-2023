#This is where the code will be for the text adventure
#By the way, a good coding practice is to leave comments explaining parts of code
#To write a comment, just put a hashtag, then text directly after
#These are comments

import random #do not delete this, i will explain what it is later

#write your code starting from line 10
#link: https://bit.ly/textadventure-temp

print("""
commands:
go [direction]
get [object]
to win, you have to find all the objects and escape the house
""")

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




