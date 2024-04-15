-- query_2.sql
-- Find the student with the highest average grade in a specific subject.

SELECT students.name, AVG(grades.grade) as average_grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.name = %s
GROUP BY students.name
ORDER BY average_grade DESC
LIMIT 1;