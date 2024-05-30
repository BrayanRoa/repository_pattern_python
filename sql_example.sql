create table users (
	id serial PRIMARY key,
	name varchar(50),
	lastname VARCHAR(50),
	age INTEGER,
	created_at TIMESTAMP,
	updated_at TIMESTAMP
)