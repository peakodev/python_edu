-- query_11.sql
-- The average grade that a specific teacher gives to a specific student.

SELECT students.name as student, AVG(grades.grade) as average_grade, teachers.name as teacher
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
JOIN students ON grades.student_id = students.id
WHERE students.name ilike %s AND teachers.name ilike %s
GROUP BY students.name, teachers.name;
