import psycopg2 as pg
from config import HOST, DB, DB_USER, DB_PASSWORD


def get_executed_query(query, *args):
    """
    Выполняет запрос переданный первым аргументом,
    последующие аргументы используются в том случае, если для формирования запроса требуются данные.
    Второй и следующие за ним ргументы, упакованые в args, передаются в метод курсора - "execute" вторым аргументом.
    :param query: запрос в формате psycopg2.sql (https://www.psycopg.org/docs/sql.html?highlight=sql).
    :return: кортеж с результатом запроса или False в случае неудачи.
    """
    try:
        with pg.connect(f'host={HOST} dbname={DB} user={DB_USER} password={DB_PASSWORD}') as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(query, args)
                    return tuple(cur)
                except pg.Error as e:
                    print(e.pgerror)
                    return False
    except pg.Error as e:
        print('Ошибка подключения к базе данных! Проверьте настройки подключения.')
        return False
