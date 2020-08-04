ALTER TABLE users DROP COLUMN age;
ALTER TABLE users ADD COLUMN created_at TIMESTAMP;
ALTER TABLE users RENAME COLUMN name TO first_name;
ALTER TABLE users
    ALTER COLUMN first_name SET NOT NULL,
    ADD CONSTRAINT email_uniq UNIQUE (email);


-- MASTER
ALTER TABLE users ADD COLUMN created_at timestamp;
ALTER TABLE users RENAME COLUMN name TO first_name;
ALTER TABLE users DROP COLUMN age;

ALTER TABLE users ALTER COLUMN first_name SET NOT NULL;
ALTER TABLE users ADD UNIQUE (email);
--