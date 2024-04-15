-- query_9.sql
-- Find the list of courses a student attends.

SELECT subjects.name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
WHERE students.name ilike %s
GROUP BY subjects.name;