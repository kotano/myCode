CREATE TABLE countries (
    id BIGINT PRIMARY KEY,
    name VARCHAR
);

CREATE TABLE country_regions (
    id BIGINT PRIMARY KEY,
    country_id BIGINT REFERENCES countries (id),
    name VARCHAR
);

CREATE TABLE country_region_cities (
    id BIGINT PRIMARY KEY,
    country_region_id BIGINT REFERENCES country_regions (id),
    name VARCHAR
);


INSERT INTO countries VALUES (1, 'Россия');
INSERT INTO country_regions VALUES (1, 1, 'Татарстан'), (2, 1, 'Самарская область');
INSERT INTO country_region_cities VALUES (1, 1, 'Бугульма'), (2, 1, 'Казань'), (3, 2, 'Тольятти');