from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()

class MongoDatabase:
    def __init__(self, collection=""):
        database = "smart_steel_db"
        connection_url = getenv('MONGO_DATABASE_URI')
        self.client = MongoClient(connection_url)
          
        self.db = self.client[database]
        self.collection = collection if collection != "" else "default"
    

    def insert_many(self, list_params):
        return self.db[self.collection].insert_many(list_params)
    
    def insert_one(self, single_params):
        return self.db[self.collection].insert_one(single_params)
    
    def query_one(self, query_params={}):
        params = {}
        if query_params:
            params = query_params
        
        result = self.db[self.collection].find_one(params)
        return result
    
    def query(self, query_params={}):
        params = {}
        if query_params:
            params = query_params
        
        result = self.db[self.collection].find(params)
        return result

