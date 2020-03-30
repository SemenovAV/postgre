import psycopg2 as pg


def get_executed_query(connection, query, *args):
    """
    Выполняет запрос к базе переданный вторым аргументом,
    последующие аргументы используются в том случае, если для формирования запроса требуются данные.
    Третий и следующие за ним аргументы, упакованые в args, передаются в метод курсора - "execute" вторым аргументом.
    :param connection:
    :param query: запрос в формате psycopg2.sql (https://www.psycopg.org/docs/sql.html?highlight=sql).
    :return: кортеж с результатом запроса или False в случае неудачи.
    """
    with connection.cursor() as cur:
        try:
            cur.execute(query, args)
            return tuple(cur)
        except pg.Error as e:
            if e.pgerror:
                print(e.pgerror)
