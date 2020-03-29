import psycopg2 as pg
from config import HOST, PORT, DB, DB_USER, DB_PASSWORD


def add_student(student):
    """
    cоздает студента
    """
    try:
        with pg.connect(
                f'host={HOST} '
                f'port={PORT} '
                f'dbname={DB} '
                f' user={DB_USER} '
                f'password={DB_PASSWORD} '
        ) as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(
                        '''
                        INSERT INTO student (name, birth) 
                        values (%s, %s)
                        ''', (student['name'], student['birth'])

                    )

                except pg.Error as e:
                    print(e.pgerror)
                    return False
    except pg.Error as e:
        print('Ошибка подключения к базе данных! Проверьте настройки подключения.')
        return False
    return True
