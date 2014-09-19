from flask import render_template,flash, redirect, request, session, url_for
from app import db
from forms import LoginForm
from app import app
from models.User import User

@app.route('/')
@app.route('/index')
def index():
    user = {'name':'rick'}
    return render_template("index.html", title='hello', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
#    from app import request
    error = None
    users = None
    if request.method == 'POST' and  request.form['username'] is not None:
        pu = request.form['username']
        users = User.query.filter(User.username==pu).all()
#        users = list(db.session.execute("select * from \"user\" where username=:username", {'username':pu}).fetchall())
        if request.form['password'] != users[0].password: #app.config['PASSWORD']:
#        if request.form['password'] != users.password: #app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return render_template("index.html", title='hello', user=users)
    flash('this is a flash')
    return render_template('login.html', error=error, form=list(),user=users)

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST' and  request.form['username'] is not None and  request.form['password'] is not None:
        user = User(username=request.form['username'], password=request.form['password'])
        db.session.add(user)
        db.session.commit()
        return "gogo"
    users = User.query.all()
    return render_template('register.html', users=users)


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
    users = db.session.execute("select * from user").first()
    return render_template('test.html', user=users, db=db)
