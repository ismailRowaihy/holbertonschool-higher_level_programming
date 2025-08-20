#!/usr/bin/python3

from flask import Flask,jsonify,request


app = Flask(__name__)
users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/status')
def statusPage():
    return "OK"

@app.route('/users/<username>')
def usersPage(username):
    if username  not in users.keys():
        return {"error": "User not found"},404
    else:
        return jsonify(users[username])
        
@app.route('/data')
def DataPage():
    return jsonify(list(users.keys()))

@app.route('/add_user', methods=['POST'])
def add_user():
    newUser = request.get_json()
    if "username" not in newUser.keys():
        return {"error":"Username is required"},400
    
    users[newUser["username"]] = newUser
    return {"message": "User added","user":newUser},201

if __name__ == "__main__": app.run()