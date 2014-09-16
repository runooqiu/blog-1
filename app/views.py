from flask import render_template,flash, redirect, request, session, url_for
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'name':'rick'}
    return render_template("index.html", title='hello', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
#    from app import request
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'rick': #app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != 'chenglin': #app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return render_template("index.html", title='hello', user='rick')
    flash('this is a flash')
    return render_template('login.html', error=error, form=list())

@app.route('/test')
def test():
    from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.sql import select
#    engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
    engine = create_engine('mysql://root:123456@localhost:3306/web2py?charset=utf8',encoding = "utf-8",echo =True)
    metadata = MetaData(bind=engine)
    users = Table('users', metadata, autoload=True)
    con = engine.connect()
    data = con.execute(users.insert(), name='admin', email='admin@localhost')
#    data = con.query(users).all()
    s = select([users])
    user = con.execute(s)
    return render_template('test.html', title='Test', user=user)

@app.route('/test1')
def test1():
    from app import db, SQLAlchemy
#    user =  Table('users', metadata, autoload=True)
#   users = User.query.all()
    users = db.session.execute("select * from post").first()
    return render_template('test.html', user=users, db=db)
