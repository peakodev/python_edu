-- query_12.sql
-- The grades of students in a specific group for a specific subject at the last lesson.

SELECT students.name, grades.grade, DATE(grades.received_at) as received_at
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN groups ON students.group_id = groups.id
WHERE groups.name = %s AND subjects.name = %s AND DATE(grades.received_at) = (
    SELECT MAX(DATE(grades.received_at))
    FROM grades
    JOIN students ON grades.student_id = students.id
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE groups.name = %s AND subjects.name = %s
);