# Database related imports
# Make sure to import your tables!
from model import Base, User, Post

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind = engine)
session_factory = scoped_session(DBSession)

# Your database functions are located under here (querying, adding items, etc.)

# Example of adding a student:
def add_user(name, password, points, phone_number):
	
	session = session_factory()
	print("Added a user!")
	user = User(name = name, password = password, points = points, phone_number = phone_number)
	session.add(user)
	session.commit()

def add_post(title, description, category, username, contact):

	session = session_factory()
	print("Added a post!")
	post = Post(title = title, description = description, category = category, username = username, contact = contact)
	session.add(post)
	session.commit()

def query_all_users():
	session = session_factory()
	return session.query(User).all()

def query_all_posts():
	session = session_factory()
	return session.query(Post).all()

def query_by_name(name):
	session = session_factory()
	return session.query(User).filter_by(name = name).first()

def get_points(name):
	session = session_factory()
	return query_by_name(name).points

def update_points(amount, name):
	session = session_factory()
	usr = query_by_name(name)
	#usr.points += amount
	session.commit()

def query_by_title(title):
	session = session_factory()
	return session.query(Post).filter_by(title = title).all()

def delete_all_users():
	session = session_factory()
	session.query(User).delete()
	session.commit()

def delete_all_posts():
	session = session_factory()
	session.query(Post).delete()
	session.commit()

def query_by_category(category):
	session = session_factory()
	return session.query(Post).filter_by(category = category).all()

def query_by_username(username):
	session = session_factory()
	return session.query(Post).filter_by(username = username).all()

def delete_duplicates():
	session = session_factory()
	names = []
	
	for i in query_all_articles():
	
		names.append(i.name)
	
	names = set(names)
	names = list(names)
	temp = []

	for i in names:
		
		#l = query_by_name(i)
		temp.append(query_by_name(i)[0])
	
	delete_all()

	for i in temp:
		add(i.name, i.password, i.points, i.picture)
		#for j in range(len(l)-1):

			#delete_article_by_name(i)
	session.commit()