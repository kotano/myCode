CREATE TABLE courses (
name varchar(255),
body text,
created_at timestamp
);

CREATE TABLE users (
first_name varchar(255),
email varchar(255),
manager boolean
);

CREATE TABLE course_members (
user_id integer,
course_id integer,
created_at timestamp
);

CREATE TABLE courses (
name varchar(255),
slug varchar(255),
lessons_count integer,
body text
);