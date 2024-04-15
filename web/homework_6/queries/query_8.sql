-- query_8.sql
--- Find the average grade that a specific teacher gives for their subjects.

SELECT teachers.name, AVG(grades.grade) as average_grade
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id
JOIN grades ON subjects.id = grades.subject_id
WHERE teachers.name ilike %s
GROUP BY teachers.name;