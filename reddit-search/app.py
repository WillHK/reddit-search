from flask import Flask, jsonify, request
from joblib import load
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/search')
def search_reddit(query):
    return "Work In Progress."

if __name__ == '__main__':
    app.run()