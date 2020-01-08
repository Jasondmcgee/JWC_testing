from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)  

client = MongoClient("mongodb+srv://Peaches:peaches17@cluster0-tlhyy.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.Submissions
proposals = db.Proposals

@app.route('/')
def homepage():
    info = proposals.find()
    return render_template('homepage.html', info=info)


if __name__ == '__main__':
    app.run(debug=True)