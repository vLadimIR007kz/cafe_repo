from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pymysql
from flask import Flask, render_template, request, redirect, flash, jsonify

pymysql.install_as_MySQLdb()
import json


pymysql.install_as_MySQLdb()
app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'a really really really really long secret key'
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nazvanie = db.Column(db.String(50), nullable=False)
    adress = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    teg = db.Column(db.String(40), nullable=False)


class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, nullable=False)
    login_id = db.Column(db.Integer, nullable=False)
    product = db.Column(db.String(25), nullable=False)
    price = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(100), nullable=False)


@app.route("/")
@app.route("/choice")
def choice():
    return render_template("choice.html")


@app.route("/Account")
def account():
    return render_template("account.html")


if __name__ == '__main__':
    app.run(debug=True)