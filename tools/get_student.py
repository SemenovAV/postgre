from tools import queryes
from tools.get_executed_query import get_executed_query as geq


def get_student(student_id: int):
    """
    Получает студента из базы.
    :param student_id: int
    :return: tuple или False в случае неудачи
    """
    return geq(queryes.get_student, student_id)
