from tools import queryes
from tools.get_executed_query import get_executed_query as geq


def get_students(course_id):
    """
    Получает всех студентов курса содержащегося в таблице course с id равным course_id.
    :param course_id: int - id курса
    :return: tuple
    """
    return geq(queryes.get_students, course_id)
