from pymongo import MongoClient

class MyMongoClient():
    def __init__(self,host='localhost',dbname:str=None):
        self.client=MongoClient(host)
        self.db=self.client[dbname]
    def get_all(self,collection):
        return self.db[collection].find()
    def get_one(self,collection,query):
        if query:
            return self.db[collection].find_one(query)
        else:
            raise "query is NULL"



