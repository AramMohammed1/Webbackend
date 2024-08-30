from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
host = os.getenv('DBHOST')
client=MongoClient(host)
database= os.getenv('DATABASE')
db=client.get_database(database)