from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here

# Example code:
class User(Base):
	__tablename__ = "Users"
	user_id = Column(Integer, primary_key = True)
	name = Column(String)
	password = Column(String)
	points = Column(Integer)
	phone_number = Column(String)
	#picture = Column(String)

	def __repr__(self):
		return ("user name:{}, user pass:{}, user points:{}, user phone: {}".format(self.name, self.password, self.points, self.phone_number))

class Post(Base):
	__tablename__ = "Posts"
	post_id = Column(Integer, primary_key = True)
	title = Column(String)
	description = Column(String)
	category = Column(String)
	username = Column(String)
	contact = Column(String)
	# found_things = Column(List)
	def __repr__(self):
		return ("Post title: {}, Post description: {}, Post category: {}".format(self.title, self.description, self.category))