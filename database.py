from pymongo import MongoClient

client = MongoClient("mongodb+srv://ArnavShah:arnavshah@cluster0.sgw7j.mongodb.net/thermapal?retryWrites=true&w=majority")

db = client["thermapal"]
collection = db["temperature"]

def find(query):
    output = ""
    for document in collection.find(query):
        output += str(document)
    return output

