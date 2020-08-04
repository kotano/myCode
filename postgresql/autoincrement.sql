CREATE TABLE article_categories (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name text
);

INSERT INTO article_categories (name) VALUES ('value 1'), ('value 2');
