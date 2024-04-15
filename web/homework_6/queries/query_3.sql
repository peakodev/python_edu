-- query_3.sql
-- Find the average grade in groups for a specific subject.

SELECT groups.name, AVG(grades.grade) as average_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.name = %s
GROUP BY groups.name;