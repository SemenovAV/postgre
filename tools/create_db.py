import psycopg2 as pg
from config import HOST, DB, DB_USER, DB_PASSWORD


def create_db():
    '''
    Создает таблицы.
    :return:
    '''
    try:
        with pg.connect(f'host={HOST} dbname={DB} user={DB_USER} password={DB_PASSWORD}') as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(
                        '''
                        CREATE TABLE student(
                        id serial PRIMARY KEY,
                        name varchar(100),
                        gpa numeric(10, 2),
                        birth timestamp with time zone
                        );

                        '''

                    )

                    cur.execute(
                        '''
                        CREATE TABLE course(
                        id serial PRIMARY KEY,
                        name varchar(100)
                        );

                        '''
                    )
                except pg.Error as e:
                    print(e.pgerror)
                    return False
    except pg.Error as e:
        print('Ошибка подключения к базе данных! Проверьте настройки подключения.')
        return False
    return True
