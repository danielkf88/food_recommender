import sqlite3
import datetime

create_users_table = '''CREATE TABLE IF NOT EXISTS USER(
	user_id		varchar		PRIMARY KEY	NOT NULL,
	user_name	varchar 	NOT NULL,
	gender		varchar 	NOT NULL,
	height		int			NOT NULL CHECK
		(height between 80 and 220),
	weight		int			NOT NULL CHECK
		(weight between 30 and 200),
	age         int			NOT NULL CHECK
		(age	between 16 and 120),
	email		varchar		UNIQUE NOT NULL CHECK
		(email like '_%@__%.__%'),
    password	varchar		NOT NULL
		);'''

create_activities_table = '''CREATE TABLE  IF NOT EXISTS ACTIVITY_STEP (
	user_id		varchar		NOT NULL,
	entry_date	date		NOT NULL,
	step		int			NOT NULL CHECK
		(step < 100000),
    PRIMARY KEY (user_id, entry_date),
	FOREIGN KEY (user_id)
		REFERENCES USER(user_id)
			ON UPDATE CASCADE
			ON DELETE CASCADE
			);'''

create_food_list_table = '''CREATE TABLE IF NOT EXISTS FOOD_LIST (
	food_id			int     		PRIMARY KEY,
	food_name		varchar			UNIQUE NOT NULL,
	category		varchar			NOT NULL,
	calories		int				NOT NULL,
	protein			int				NOT NULL,
	total_fat		int				NOT NULL,
	saturated_fat	int				NULL,
	trans_fat		int				NULL,
	cholesterol		int				NULL,
	total_carb		int				NOT NULL,
	total_sugar		int				NULL,
	dietary_fibre	int				NOT NULL,
	sodium			int				NOT NULL
	);'''

create_food_diary_table = '''CREATE TABLE IF NOT EXISTS FOOD_DIARY (
	user_id		varchar			NOT NULL,
	entry_date	date			NOT NULL,
	meal_of_day	varchar(9)		NOT NULL,
	food_id		int				NOT NULL,
	PRIMARY KEY (user_id, entry_date),
	FOREIGN KEY (user_id)
		REFERENCES USER(user_id)
			ON UPDATE CASCADE
			ON DELETE CASCADE,
	FOREIGN KEY (food_id)
		REFERENCES FOOD_LIST(food_id)
			ON UPDATE CASCADE
			ON DELETE NO ACTION	
		);'''
# connect to the database and create the tables
with sqlite3.connect('health.db') as conn:

    # create the user table
    conn.execute(create_users_table)

    # create the activity table
    conn.execute(create_activities_table)

    # create the food list table
    conn.execute(create_food_list_table)

    # create the food diary table
    conn.execute(create_food_diary_table)

    conn.commit()