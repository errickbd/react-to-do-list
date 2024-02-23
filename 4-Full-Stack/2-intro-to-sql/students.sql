DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id serial PRIMARY KEY,
    first_name VARCHAR(10),
    last_name  VARCHAR(10),
    age INT,
    grade CHAR(1)
);

COPY students FROM '/Users/franciscoavila/Desktop/whiskey-demos-and-notes/4-Full-Stack/2-intro-to-sql/resources/data.csv' DELIMITER ',' CSV HEADER;

-- INSERT INTO students (id, first_name, last_name, age, grade) VALUES (6,'francisco', 'avila', '18', 'B');
-- INSERT INTO students (first_name, last_name, age, grade) VALUES ('francisco2', 'avila', '18', 'B');
-- INSERT INTO students (first_name, last_name, age, grade) VALUES ('francisco3', 'avila', '18', 'B');
-- INSERT INTO students (first_name, last_name, age, grade) VALUES ('francisco4', 'avila', '18', 'B');

-- SELECT * FROM students;

-- SELECT first_name, last_name 
-- FROM students
-- WHERE grade in ('A','B') AND age > 18;

-- SELECT grade, COUNT(*) 
-- FROM students
-- GROUP BY grade;

SELECT first_name, last_name
FROM students
ORDER BY last_name DESC
LIMIT 3;