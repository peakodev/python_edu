-- query_7.sql
-- Find the grades of students in a specific group for a specific subject.

SELECT students.name, grades.grade, DATE(grades.received_at)
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN groups ON students.group_id = groups.id
WHERE groups.name = %s AND subjects.name = %s
ORDER BY grades.received_at DESC;