from tools import queryes
from tools.get_executed_query import get_executed_query as geq


def add_student(student: dict):
    """
    Добавляет студента в базу.

    :param student: dict
    :return: Bool
    """
    return geq(queryes.add_student, student['name'], student['birth'])
