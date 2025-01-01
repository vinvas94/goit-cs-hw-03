from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi

# MongoDB connection (Replace with your connection string)
client = MongoClient(
    "mongodb+srv://vintoniv1111:<db_password>@cluster0.1p0zz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1')
)

# Select or create a database
db = client["my_cat_database"]  # Replace "my_cat_database" with your desired database name

# Create a collection for cats
cats_collection = db["cats"]

def insert_cat(name, age, features):
    """
    Inserts a new cat document into the collection with an automatically generated ObjectId.

    Args:
        name (str): The cat's name.
        age (int): The cat's age.
        features (list): A list of the cat's features.
    """
    new_cat = {
        "name": name,
        "age": age,
        "features": features
    }
    result = cats_collection.insert_one(new_cat)
    print(f"Кіт {name} доданий з ID: {result.inserted_id}")

def find_cat_by_name(name):
    """Finds a cat by name"""
    result = cats_collection.find_one({"name": name})
    return result

def update_cat_age(name, new_age):
    """Updates the age of a cat by name"""
    result = cats_collection.update_one({"name": name}, {"$set": {"age": new_age}})
    return result

def add_feature_to_cat(name, new_feature):
    """Adds a new feature to a cat"""
    result = cats_collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    return result

def delete_cat_by_name(name):
    """Deletes a cat by name"""
    result = cats_collection.delete_one({"name": name})
    return result

def delete_all_cats():
    """Deletes all cats from the collection"""
    result = cats_collection.delete_many({})
    return result

def get_all_cats():
    """Gets all cats from the collection"""
    cats = cats_collection.find()
    return cats
