from tools import queryes
from tools.get_executed_query import get_executed_query as geq

get_student = lambda student: geq(queryes.get_student, student)
