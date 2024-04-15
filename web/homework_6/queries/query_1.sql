-- query_1.sql
-- Find the top 5 students with the highest average grade across all subjects.

SELECT students.name, AVG(grades.grade) as average_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.name
ORDER BY average_grade DESC
LIMIT 5;