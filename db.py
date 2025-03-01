# from pymongo import MongoClient
# import datetime
#
# # MongoDB connection URI (replace with your actual connection string)
# MONGO_URI = "mongodb+srv://soumyaroy172003:Soumya1234@iotproject.pvno5.mongodb.net/"
#
# client = MongoClient(MONGO_URI)
# db = client['AccessLogsDB']
# collection = db['AccessLogs']
#
# # def insert_access_log(status,decoded_data):
# #     """Insert an access log entry into MongoDB."""
# #     # Split the string into lines
# #     lines = decoded_data.split("\n")
# #
# #     # Extract the Registered Users line and remove the prefix
# #     registered_users = lines[1].replace("Registered Users: ", "").strip()
# #
# #     log_entry = {
# #         "timestamp": datetime.datetime.now(),
# #         "status": status,
# #         "registered_user":registered_users
# #     }
# #     collection.insert_one(log_entry)
# #     print(f"[LOG] Access logged with status: {status}")
#
#
# def insert_access_log(status,name):
#     """Insert an access log entry into MongoDB."""
#
#
#     log_entry = {
#         "timestamp": datetime.datetime.now(),
#         "status": status,
#         "registered_user":name
#     }
#     collection.insert_one(log_entry)
#     print(f"[LOG] Access logged with status: {status}")

#
# from pymongo import MongoClient
# import datetime
#
# # MongoDB connection URI (replace with your actual connection string)
# MONGO_URI = "mongodb+srv://soumyaroy172003:Soumya1234@iotproject.pvno5.mongodb.net/"
#
# try:
#     client = MongoClient(MONGO_URI)
#     db = client['AccessLogsDB']
#     collection = db['AccessLogs']
#     print("[LOG] Successfully connected to MongoDB")  # Print when the connection is established
# except Exception as e:
#     print(f"[ERROR] Failed to connect to MongoDB: {e}")
#     exit(1)
#
# def insert_access_log(status, name):
#     """Insert an access log entry into MongoDB."""
#     log_entry = {
#         "timestamp": datetime.datetime.now(),
#         "status": status,
#         "registered_user": name
#     }
#     collection.insert_one(log_entry)
#     print(f"[LOG] Access logged with status: {status}")
#


from pymongo import MongoClient
import datetime

# MongoDB connection URI (replace with your actual connection string)
MONGO_URI = "mongodb+srv://soumyaroy172003:Soumya1234@iotproject.pvno5.mongodb.net/"

try:
    client = MongoClient(MONGO_URI)
    db = client['AccessLogsDB']
    collection = db['AccessLogs']
    print("[LOG] Successfully connected to MongoDB")  # Print when the connection is established
except Exception as e:
    print(f"[ERROR] Failed to connect to MongoDB: {e}")
    exit(1)

def insert_access_log(status, name):
    """Insert an access log entry into MongoDB."""
    log_entry = {
        "timestamp": datetime.datetime.now(),
        "status": status,
        "registered_user": name
    }
    collection.insert_one(log_entry)
    print(f"[LOG] Access logged with status: {status}")

# # Ensure `name` is defined before calling the function
# name = "John Doe"  # Replace this with an actual value
# insert_access_log("Success", name)
