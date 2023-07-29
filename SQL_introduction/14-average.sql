-- Computes the average of the "score" column in the "second_table" table and saves it in a new column "average"
UPDATE second_table
SET average = SELECT AVG(score) FROM grades;
