DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    major VARCHAR(100)
);

CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT,
    title VARCHAR(100),
    post_text TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (user_id, first_name, last_name, major) VALUES (1, 'Charlie', 'Magruder', 'Data Science');
INSERT INTO users (user_id, first_name, last_name, major) VALUES (2, 'Alex', 'Johnson', 'Computer Science');
INSERT INTO users (user_id, first_name, last_name, major) VALUES (3, 'Jamie', 'Smith', 'Statistics');
INSERT INTO users (user_id, first_name, last_name, major) VALUES (4, 'Taylor', 'Brown', 'Economics');
INSERT INTO users (user_id, first_name, last_name, major) VALUES (5, 'Jordan', 'Davis', 'Data Science');
INSERT INTO users (user_id, first_name, last_name, major) VALUES (6, 'Morgan', 'Wilson', 'Bio');
INSERT INTO users (user_id, first_name, last_name, major) VALUES (7, 'Casey', 'Miller', 'Math');
INSERT INTO users (user_id, first_name, last_name, major) VALUES (8, 'Riley', 'Moore', 'Data Science');
INSERT INTO users (user_id, first_name, last_name, major) VALUES (9, 'Avery', 'Taylor', 'Psychology');
INSERT INTO users (user_id, first_name, last_name, major) VALUES (10, 'Sam', 'Anderson', 'History');

INSERT INTO posts (post_id, user_id, title, post_text) VALUES (1, 1, 'First goal', 'Scored my first goal on the club hockey team tonight in a win over VT.');
INSERT INTO posts (post_id, user_id, title, post_text) VALUES (2, 2, 'Long day', 'Had class and then worked on this lab at the library.');
INSERT INTO posts (post_id, user_id, title, post_text) VALUES (3, 3, 'Study group', 'Met with people in shannon.');
INSERT INTO posts (post_id, user_id, title, post_text) VALUES (4, 4, 'First bodos of the year', 'Two bacon egg and cheeses please.');
INSERT INTO posts (post_id, user_id, title, post_text) VALUES (5, 5, 'Good lecture', 'Data science lecture was confusing at first but the examples helped a lot.');
INSERT INTO posts (post_id, user_id, title, post_text) VALUES (6, 6, 'Laundry day', 'Finally did laundry after putting it off for basically the whole week.');
INSERT INTO posts (post_id, user_id, title, post_text) VALUES (7, 7, 'Intramural game', 'Played an intramural basketball game and somehow we won by two.');
INSERT INTO posts (post_id, user_id, title, post_text) VALUES (8, 8, 'Office hours', 'Went to office hours and realized my code error was just a missing comma.');
INSERT INTO posts (post_id, user_id, title, post_text) VALUES (9, 9, 'Dining hall', 'Got dinner at the dining hall and stayed way longer than I planned.');
INSERT INTO posts (post_id, user_id, title, post_text) VALUES (10, 10, 'Almost weekend', 'Finished most of my work tonight so I can relax a little this weekend.');

