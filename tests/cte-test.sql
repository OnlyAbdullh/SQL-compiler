
WITH cte_students AS (
    SELECT id, name, age
    FROM students
)
SELECT * FROM cte_students;

WITH cte AS (
    SELECT * FROM students
)
SELECT COUNT(*) FROM cte;

WITH cte_students (student_id, student_name) AS (
    SELECT id, name
    FROM students
)
SELECT student_name FROM cte_students;

WITH
cte_students AS (
    SELECT id, class_id FROM students
),
cte_classes AS (
    SELECT id, name FROM classes
)
SELECT s.id, c.name
FROM cte_students s
JOIN cte_classes c ON s.class_id = c.id;

WITH cte AS (
    SELECT * FROM students WHERE age > 20
)
SELECT * FROM cte;

WITH cte AS (
    SELECT s.name, c.name AS class_name
    FROM students s
    JOIN classes c ON s.class_id = c.id
)
SELECT * FROM cte;

WITH cte AS (
    SELECT class_id, COUNT(*) AS total
    FROM students
    GROUP BY class_id
)
SELECT * FROM cte WHERE total > 10;

WITH cte AS (
    SELECT *
    FROM students
    WHERE age > (SELECT AVG(age) FROM students)
)
SELECT * FROM cte;

WITH
cte1 AS (
    SELECT * FROM students
),
cte2 AS (
    SELECT * FROM cte1 WHERE age > 20
)
SELECT * FROM cte2;

WITH cte_numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1
    FROM cte_numbers
    WHERE n < 10
)
SELECT * FROM cte_numbers;

WITH cte_hierarchy AS (
    SELECT id, parent_id, name
    FROM categories
    WHERE parent_id IS NULL

    UNION ALL

    SELECT c.id, c.parent_id, c.name
    FROM categories c
    JOIN cte_hierarchy h ON c.parent_id = h.id
)
SELECT * FROM cte_hierarchy;

WITH cte AS (
    SELECT * FROM students WHERE age > 18
)
INSERT INTO adult_students
SELECT * FROM cte;

WITH cte AS (
    SELECT * FROM students WHERE age < 18
)
UPDATE cte
SET age = 18;

WITH cte AS (
    SELECT * FROM students WHERE age < 10
)
DELETE FROM cte;

WITH cte AS (
    SELECT * FROM students WHERE age > 20
)
UPDATE cte
SET age = age + 1
OUTPUT INSERTED.*, DELETED.*;

SELECT *
FROM (
    WITH cte AS (
        SELECT * FROM students
    )
    SELECT * FROM cte
) AS sub;

WITH cte AS (
    SELECT * FROM students
    ORDER BY id
    OFFSET 0 ROWS FETCH NEXT 5 ROWS ONLY
)
SELECT * FROM cte;

WITH cte AS (
    SELECT name FROM students
    UNION
    SELECT name FROM teachers
)
SELECT * FROM cte;