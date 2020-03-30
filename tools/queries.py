from psycopg2 import sql

create_tables = sql.SQL(
    'CREATE TABLE student('
    'id serial PRIMARY KEY ,'
    'name varchar(100) NOT NULL,'
    'gpa numeric(10, 2) NULL ,'
    'birth timestamp with time zone'
    ');'
    'CREATE TABLE course('
    'id serial PRIMARY KEY ,'
    'name varchar(100) NOT NULL,'
    'UNIQUE(name)'
    ');'
    'CREATE TABLE education('
    'course_id INTEGER NOT NULL REFERENCES course(id) ON DELETE CASCADE ,'
    'student_id INTEGER NOT NULL REFERENCES student(id) ON DELETE CASCADE ,'
    'PRIMARY KEY (course_id,student_id)'
    ');'


)
add_course = sql.SQL(
    'INSERT INTO course (name)'
    'VALUES (%s)'
    'RETURNING id,name'
)
add_student = sql.SQL(
    'INSERT INTO student (name, birth) '
    'VALUES (%s, %s)'
    'RETURNING id,name,gpa,birth'
)
get_student = sql.SQL(
    'SELECT * FROM student '
    'WHERE id = %s'
)
add_students = sql.SQL(
    'INSERT INTO student(name, birth) '
    'VALUES (%s,%s)'
    'RETURNING id,name,gpa,birth; '
    'INSERT INTO education(course_id, student_id) '
    'VALUES (%s,'
    '(SELECT id '
    'FROM student '
    'WHERE name=%s '
    'AND birth=%s)'
    ') '
    'RETURNING course_id,student_id;'
)
get_students = sql.SQL(
    'SELECT DISTINCT id,name,gpa,birth '
    'FROM student, education '
    'WHERE education.course_id = %s '
    'AND education.student_id = student.id'
)
