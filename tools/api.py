from tools import queries
from tools.get_executed_query import get_executed_query as geq

create_db = lambda con: geq(con, queries.create_tables)
add_course = lambda con, course: geq(
    con,
    queries.add_course,
    course['name'],
)
add_student = lambda con, student: geq(
    con,
    queries.add_student,
    student['name'],
    student['birth']
)
get_student = lambda con, student_id: geq(
    con,
    queries.get_student,
    student_id,
)
add_students = lambda con, course_id, students: tuple(
        map(
            lambda student: geq(
                con,
                queries.add_students,
                student['name'],
                student['birth'],
                course_id,
                student['name'],
                student['birth'],
            ), students
        )
)
get_students = lambda con, course_id: geq(con, queries.get_students, course_id)


