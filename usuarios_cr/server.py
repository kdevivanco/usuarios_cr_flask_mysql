import random
import json
from flask import Flask, render_template, request, redirect, session 
from models.connections import connectToMySQL
import pprint
from models.users import User

app = Flask(__name__)

@app.route('/')
def show_users():
    users = User.get_all()
    for user in users:
        print(user.first_name)
    return render_template('users.html',users=users)

@app.route('/create')
def show_create_page():
    users = User.get_all()
    return render_template('create.html',users=users)

@app.route('/create',methods = ["POST"])
def create_new_user():
    new_user = User.create_new(request.form)
    
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)