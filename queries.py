from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# query 1 - Write a query that returns all the Pokemon named "Pikachu".
# find all documents where pokemon is named pikachu
pikachu_pokemon = pokemonColl.find({"name": "Pikachu"})
for pikachu in pikachu_pokemon:
    print(pikachu)

# query 2 - Write a query that returns all the Pokemon with an attack greater than 150.
# find all documents where attack field is greater than 150
strong_pokemon = pokemonColl.find({"attack": {"$gt": 150}})
# print each document
for strong in strong_pokemon:
    print(strong)

# query 3 - Write a query that returns all the Pokemon with an ability of "Overgrow"
# find all documents where abilities is overgrow
overgrow_pokemon = pokemonColl.find({"abilities": "Overgrow"})
# print each document
for overgrow in overgrow_pokemon:
    print(overgrow)