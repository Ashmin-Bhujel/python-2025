# Dictionaries in Depth
# Creating and accessing values
superheroes = {
    "Avengers": [
        "Iron Man",
        "Captain America",
        "Thor",
        "Black Widow",
        "Hulk",
        "Hawkeye",
    ],
    "X-Men": ["Wolverine", "Jean", "Storm", "Beast", "Mystique", "Magneto"],
}

print(superheroes["Avengers"])
# ['Iron Man', 'Captain America', 'Thor', 'Black Widow', 'Hulk', 'Hawkeye']


# Loop with dictionary
for team in superheroes:
    print(team)
# Avengers
# X-Men


# Conditional with dictionary
if "Midnight Sons" in superheroes:
    print("There are Midnight Sons")
else:
    print("There are no Midnight Sons")
# There are no Midnight Sons


# Some useful methods
# item
# * NOTE: It returns a list of tuples with first element being the key and second element being the value
for team, members in superheroes.items():
    print(f"Team: {team}\nMembers: {members}")
# Team: Avengers
# Members: ['Iron Man', 'Captain America', 'Thor', 'Black Widow', 'Hulk', 'Hawkeye']
# Team: X-Men
# Members: ['Wolverine', 'Jean', 'Storm', 'Beast', 'Mystique', 'Magneto']


# pop
# * NOTE: It returns and removes the value of given key from the dictionary
movie_genre = {
    "Avengers": "Sci-Fi",
    "Theri": "South Indian",
    "IT": "Horror",
    "Taare Zameen Par": "Bollywood",
    "November Sky": "Biopic",
}
print(movie_genre.pop("IT"))
# Horror


# copy
# * NOTE: It returns a shallow copy of the dictionary
d = {
    "Alphabets": ["A", "B"],
    "Numbers": [0, 1],
}
d_copy = d.copy()
print(d_copy)
# {"Alphabets": ["A", "B"], "Numbers": [0, 1]}

# clear
# * NOTE: It clears the dictionary
d.clear()
# {}


# "del" keyword
# * NOTE: Can be used to delete the given field of dictionry
del superheroes["X-Men"]
print(superheroes)
# {'Avengers': ['Iron Man', 'Captain America', 'Thor', 'Black Widow', 'Hulk', 'Hawkeye']}


# Nested dictionaries
my_info = {
    "name": "Ashmin",
    "age": 21,
    "Address": {
        "Planet": "Earth",
        "Country": "Nepal",
    },
}
print(my_info["Address"]["Planet"])
# Earth


# Dictionary comprehension
continents = ["Asia", "North America", "Africa", "Europe"]
places = ["Kathmandu", "Denver", "Kairo", "Paris"]
# * NOTE: Using zip function we can create a tuple like zip object from the given two lists
the_places = {continent: place for continent, place in zip(continents, places)}
print(the_places)
# {'Asia': 'Kathmandu', 'North America': 'Denver', 'Africa': 'Kairo', 'Europe': 'Paris'}
