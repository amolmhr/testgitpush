from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://amolmhr28:pyrofighter@cluster0.6nqw5pp.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

d = {
    "name":"amol",
    "age":"30",
    "surname":"mehra"
}
db1 =client['mongotest']
coll =db1['test']
coll.insert_one(d )