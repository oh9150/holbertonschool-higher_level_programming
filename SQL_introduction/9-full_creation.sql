CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	VARCHAR(256) name,
	score INT
);
INSERT INTO second_table (id, name, score)
VALUES
	(1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8);
