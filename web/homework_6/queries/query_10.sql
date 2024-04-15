-- query_10.sql
-- List of courses that a specific student is taught by a specific teacher.

SELECT subjects.name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.name ilike %s AND teachers.name ilike %s
GROUP BY subjects.name;