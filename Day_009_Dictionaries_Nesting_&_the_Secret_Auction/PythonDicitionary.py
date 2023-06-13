#Working with Python Dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again.",
}

#Retrieving items from a Dictionary:
bug = programming_dictionary["Bug"]
print(bug)
print()

#Adding items to a Dictionary
programming_dictionary["Dictionary"] = "Data model consisting of a collection of key-value pairs. Each key-value pair maps the key to its associated value."

print(programming_dictionary)
print()

#Create an empty Dictionary
empty_dictionary = {}
empty_dictionary["Dictionary"] = "Data model consisting of a collection of key-value pairs. Each key-value pair maps the key to its associated value."

print(empty_dictionary)
print()

#Clear data from Dictionary
empty_dictionary = {}
print(empty_dictionary)
print()

#Edit an item in a Dictionary
programming_dictionary["Loop"] = "Loop can be defined as an action of doing something over and over again."
print(programming_dictionary)
print()

#Looping through a Dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])
  print()
  print(f"{key}: {programming_dictionary[key]}")
  print()



#Nesting a list in a Dictionary
top_european_football_clubs = {
  "England": ["Manchester United", "Manchester City", "Liverpool", "Arsenal", "Chelsea"],
  "Spain": ["Real Madrid", "Barcelona", "Athletico Madrid", "Espanyol", "Villareal"],
  "Italy": ["Juventus", "Inter Milan", "AC Milan", "AS Roma", "Udinese"]
}

print(top_european_football_clubs["England"])
print()



#Nesting a Dictionary in a Dictionary
travel_log = {
  "cities_visited": {
    "France": {
      "loved_it": ["Paris", "Bordaux", "Lille", "Nice"],
      "hated_it": ["Rennes", "Montpellier", "Lyon"]
    },
    "Germany": ["Berlin", "Stuttgart", "Frankfurt", "Cologne"],
    "Spain": ["Madrid", "Barcelona", "Bilbao"]
  },
  "cities_to_visit": {
    "England": ["Manchester", "Liverpool", "London"],
    "China": ["Beijing", "Hongkong"],
    "Japan": ["Tokyo"]
  }
}

print(travel_log["cities_visited"]["France"]["hated_it"][1])


