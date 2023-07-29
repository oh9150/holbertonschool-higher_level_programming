-- Lists all records in the table "second_table" where name != "".
SELECT score, name
FROM second_table
WHERE name <> ''
ORDER BY score DESC;
