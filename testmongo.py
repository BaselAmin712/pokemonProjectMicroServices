from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create a database
db = client.pokemon_images_test

# Create a test collection and insert a document
test_collection = db.test_collection
test_collection.insert_one({"name": "test_pokemon", "id": 999})

# Verify the insertion
print("Test document inserted.")