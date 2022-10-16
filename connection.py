import pymongo

def connect():
    # Establishing a connection to MongoDB
    # MongoDB must be running on the machine, 27017 is the standard port
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")  # MongoClient('localhost', 27017)
    # Connect to the database. If it does not exist, it will be created
    db = db_client["med"]
    return db
    