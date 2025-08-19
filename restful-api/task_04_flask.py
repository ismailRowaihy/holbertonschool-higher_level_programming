#!/usr/bin/python3

from flask import Flask,jsonify


app = Flask(__name__)
users = {
        "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
        "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
        }

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/status')
def statusPage():
    return "OK"

@app.route('/users/<username>')
def usersPage(username):
    if username  not in users.keys():
        return jsonify({"error": "User not found"})
    else:
        return jsonify(users[username])
        
@app.route('/data')
def DataPage():
    return jsonify(list(users.keys()))


if __name__ == "__main__": app.run(host='0.0.0.0', port=80)