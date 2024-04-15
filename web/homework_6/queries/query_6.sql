-- query_6.sql
-- Find the list of students in a specific group.

SELECT students.name
FROM students
JOIN groups ON students.group_id = groups.id
WHERE groups.name = %s;