from pymongo import MongoClient
import datetime

# MongoDB connection URI (replace with your actual connection string)
MONGO_URI = "mongodb+srv://soumyaroy172003:Soumya1234@iotproject.pvno5.mongodb.net/"

client = MongoClient(MONGO_URI)
db = client['AccessLogsDB']
collection = db['AccessLogs']

# def insert_access_log(status,decoded_data):
#     """Insert an access log entry into MongoDB."""
#     # Split the string into lines
#     lines = decoded_data.split("\n")
#
#     # Extract the Registered Users line and remove the prefix
#     registered_users = lines[1].replace("Registered Users: ", "").strip()
#
#     log_entry = {
#         "timestamp": datetime.datetime.now(),
#         "status": status,
#         "registered_user":registered_users
#     }
#     collection.insert_one(log_entry)
#     print(f"[LOG] Access logged with status: {status}")


def insert_access_log(status,name):
    """Insert an access log entry into MongoDB."""


    log_entry = {
        "timestamp": datetime.datetime.now(),
        "status": status,
        "registered_user":name
    }
    collection.insert_one(log_entry)
    print(f"[LOG] Access logged with status: {status}")