from tools import queryes
from tools.get_executed_query import get_executed_query as geq


def add_students(course_id: int, students: list):
    """
    Создает студентов и записывает их на курс
    :param course_id: int - id курса
    :param students: list - Список обьектов студентов
    :return: Кортеж результатов.
    """

    return tuple(
        map(
            lambda student: geq(
                queryes.add_students,
                student['name'],
                student['birth'],
                course_id,
                student['name'],
                student['birth'],
            ), students
        )
    )
