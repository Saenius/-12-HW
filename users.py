
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	id = sa.Column(sa.INTEGER, primary_key = True) 
	first_name = sa.Column(sa.TEXT)
	last_name = sa.Column(sa.TEXT)
	gender = sa.Column(sa.TEXT)
	email = sa.Column(sa.TEXT)
	birthdate = sa.Column(sa.TEXT)
	height = sa.Column(sa.FLOAT)

def connect_db():
	engine = sa.create_engine(DB_PATH)
	Base.metadata.create_all(engine)
	session = sessionmaker(engine)
	return session()

def request_data():
	print("Hi! I'll write your data")
	first_name = input('Enter your first name: ')
	last_name = input('And now enter the last name: ')
	gender = input('Your gender: ')
	email = input('Your email, please: ')
	birthdate = input('Enter your birthdate: ')
	height = input('Height: ')
	user = User(
		id = user_id,
		first_name = first_name,
		last_name = last_name,
		gender = gender,
		email = email,
		birthdate = birthdate,
		height = height
		)
	return user

def main():
	session = connect_db()
	user = request_data()
	session.add(user)
	session.commit()
	print("Thanks,the data successfully saved!")

if __name__ == "__main__":
	main()



































