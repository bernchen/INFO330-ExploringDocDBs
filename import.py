import sqlite3  # This is the package for all sqlite3 access in Python
from pymongo import MongoClient

# connect to mongodb and the appropriate collection
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# connect to sqlite database
conn = sqlite3.connect('pokemon.sqlite')
c = conn.cursor()

# read the data from sqlite database and transform it
for row in c.execute('SELECT p.id, p.pokedex_number, p.name, p.hp, p.attack, p.defense, p.speed, p.sp_attack, p.sp_defense, t.name, GROUP_CONCAT(a.name) as abilities FROM pokemon p JOIN pokemon_abilities pa ON p.id = pa.pokemon_id JOIN ability a ON pa.ability_id = a.id JOIN pokemon_type pt ON p.id = pt.pokemon_id JOIN type t ON pt.type_id = t.id WHERE p.pokedex_number BETWEEN 1 AND 801 GROUP BY p.id'):
    typelist = [t for t in row[10].split(',') if t]
    doc = {
        'id': row[0],
        'pokedex_number': row[1],
        'name': row[2],
        'hp': row[3],
        'attack': row[4],
        'defense': row[5],
        'speed': row[6],
        'sp_attack': row[7],
        'sp_defense': row[8],
        'types': typelist,
        'abilities': row[9].split(','),
    }
    # insert document into mongodb database
    pokemonDB['pokemon_data'].insert_one(doc)

# close connection
conn.close()
mongoClient.close()