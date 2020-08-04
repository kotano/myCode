SELECT username, created_at FROM users WHERE birthday < '2018-10-21' ORDER BY birthday DESC LIMIT 2;

SELECT * FROM users
WHERE birthday > '1999-10-23' ORDER BY first_name
LIMIT 3;


CREATE TABLE cars (
user_first_name varchar(255),
brand varchar(150),
model varchar (255));

INSERT INTO users VALUES ('Bruce', 'Lee'), ('Jackie', 'Chan');

INSERT INTO cars VALUES ('Bruce', 'bmw', 'x5'), ('Bruce', 'audi', 'a6'), ('Jackie', 'mercedes', 'xls'), 
('Jackie', 'Lamborghini', 'Super'), ('Jackie', 'Porsche', '911');


CREATE TABLE users (
id bigint PRIMARY KEY,
first_name varchar (255),
created_at timestamp);

INSERT INTO users VALUES (1, 'Tom');

CREATE TABLE orders (
id bigint PRIMARY KEY,
user_first_name varchar(255),
months integer,
created_at timestamp);

INSERT INTO orders VALUES (1, 'Tom', 1), (2, 'Tom', 2);

