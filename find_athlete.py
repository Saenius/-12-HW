import datetime
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"

Base = declarative_base()

class Athletes(Base):
	__tablename__ = 'athelete'
	id = sa.Column(sa.Integer, primary_key=True)
	age = sa.Column(sa.Integer)
	birthdate = sa.Column(sa.Text)
	gender = sa.Column(sa.Text)
	height = sa.Column(sa.Float)
	weight = sa.Column(sa.Integer)
	name = sa.Column(sa.Text)
	gold_medals = sa.Column(sa.Integer)
	silver_medals = sa.Column(sa.Integer)
	bronze_medals = sa.Column(sa.Integer)
	total_medals = sa.Column(sa.Integer)
	sport = sa.Column(sa.Text)
	country = sa.Column(sa.Text)

class User(Base):
	__tablename__ = 'user'
	id = sa.Column(sa.String(36), primary_key = True) 
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
	print("Let's go searching the same on one of our users athlets")
	user_id = input("Enter the user's ID")
	return int(user_id)

def convert_str_to_date(date_str):
	parts = date_str.split("-")
    date_parts = map(int, parts)
    date = datetime.date(*date_parts)
    return date

def nearest_by_bd(user, session):
	athletes_list = session.query(Athletes).all()
	athlete_id_bd = {}
	for athelete in athletes_list:
		bd = convert_str_to_date(athlete.birthdate)
		athlete_id_bd[athlete.id] = bd
	user_bd = convert_str_to_date(user.birthdate)
    min_dist = None
    athlete_id = None
    athlete_bd = None

    for i_d, bd in athlete_id_bd.items():
    	dist = abs(user_bd - bd)
    	if min_dist is None or dist < min_dist:
    		min_dist = dist
    		athlete_id = i_d
    		athlete_bd = bd
    	return athlete_id, athlete_bd

def nearest_by_height(user, session):
	athletes_list = session.query(Athletes).all()
	athlete_id_height = {athlete.id: athlete.height for athlete in athletes_list}
	user_height = user.height
	min_dist = None
	athlete_id = None
	athelete_height = None
	for i_d, height in athlete_id_height.items():
		if height is None:
			continue
		dist = abs(user_height - height)
		if min_dist is None or dist < min_dist:
			min_dist = dist
			athlete_id = i_d
			athelete_height = height
	return athlete_id, athelete_height



































main():
	session = connect_db()
	id = input("Enter the id for search: ")
	users_cnt, user_ids, log = find(name, session)
	print(users_cnt, user_ids, log)

if __name__ == "__main__":
	main()
