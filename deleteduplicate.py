import sqlite3  # This is the package for all sqlite3 access in Python
from pymongo import MongoClient

# connect to mongodb and the appropriate collection
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# find duplicate documents
pipeline = [
    {"$group": {"_id": "$pokedex_number", "count": {"$sum": 1}}},
    {"$match": {"count": {"$gt": 1}}}
]
duplicate_pokedex_numbers = [doc["_id"] for doc in pokemonColl.aggregate(pipeline)]
print(duplicate_pokedex_numbers)

# delete duplicate documents
for pokedex_number in duplicate_pokedex_numbers:
    filter = {"pokedex_number": pokedex_number}
    pokemonColl.delete_many(filter=filter, collation={"locale": "en", "strength": 1})

# delete all documents
#pokemonColl.delete_many({})
    
# close connection
mongoClient.close()