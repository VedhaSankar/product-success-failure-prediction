from flask import Flask, render_template, request
from pymongo import MongoClient
# import pymongo.errors as pymon_err
from dotenv import load_dotenv
import os

load_dotenv()


MONGO_URI = os.environ.get('MONGO_URI')
client = MongoClient(MONGO_URI)  

DB_NAME = 'trials'
database = client[DB_NAME]

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def start():

    if request.method=='POST':
        p_name    = request.values.get("p_name")
        description    = request.values.get("desc")

        result = {
            'p_name'    : p_name,
            'description'     : description
        }

        collection_name = 'users'
        new_collection = database[collection_name]
        x = new_collection.insert_one(result)
        print(x)
        return render_template('index.html', result="Inserted")

    return render_template('index.html')


if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)  