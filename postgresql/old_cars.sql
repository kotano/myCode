CREATE TABLE brands (
    id bigint PRIMARY KEY,
    name varchar(255),
    discount INTEGER
);

CREATE TABLE cars (
    id bigint PRIMARY KEY,
    brand bigint REFERENCES brands (id),
    model varchar(255),
    price NUMERIC
);


INSERT INTO brands VALUES (1, 'bmw', 5), (2, 'nissan', 10);

INSERT INTO cars VALUES 
(1, 1, 'm5', 5500000),
(2, 2, 'almera', 5500000),
(3, 1, 'x5m', 6000000),
(4, 1, 'm1', 2500000),
(5, 2, 'gt-r', 5000000);

