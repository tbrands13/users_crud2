from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User


@app.route('/users')
def index():
    users = User.get_all()
    return render_template("read.html", users = users)



@app.route('/users/add', methods=["POST"])
def create_user():
    data = {
        "fname" : request.form['fname'],
        "lname" : request.form['lname'],
        "email" : request.form['email'],
        "occupation" : request.form['occupation'],
        'created_at' : request.form['created_at'],
        'updated_at' : request.form['updated_at']
    }
    newUser=User.save(data)
    return redirect(f"/user/{newUser}")


@app.route('/users/new')
def NewUser():
    return render_template("create.html")


@app.route('/user/<int:id>')
def show_user(id):
    data = {
        'id' :id
    }
    user= User.got_one(data)
    return render_template('show.html', user = user)



@app.route('/edit/user/<int:id>')
def go_edit(id):
    data = {
        'id' : id
    }
    all_users = User.got_one(data)
    return render_template('edit.html', user = all_users)



@app.route('/update/user', methods=['POST'])
def update_user():
    data = {
        'id' : request.form['id'],
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' : request.form['email'],
        'occupation' : request.form['occupation'],
        'updated_at' : request.form['updated_at']
    }
    # user = request.form['id']
    user = User.update_user(data)
    return redirect(f"/user/{data['id']}")


@app.route('/users/<id>/destroy')
def delete_user(id):
    data = {
        'id' : id
    }
    User.delete_user(data)
    return redirect('/users')