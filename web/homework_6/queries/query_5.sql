-- query_5.sql
-- Find which courses a specific teacher teaches.

SELECT subjects.name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE teachers.name ilike %s;