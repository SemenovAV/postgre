import psycopg2 as pg
from config import HOST, DB, DB_USER, DB_PASSWORD


def create_db():
    """
    Создает таблицы.
    """
    try:
        with pg.connect(f'host={HOST} dbname={DB} user={DB_USER} password={DB_PASSWORD}') as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(
                        '''
                        CREATE TABLE student(
                        id serial PRIMARY KEY ,
                        name varchar(100) NOT NULL,
                        gpa numeric(10, 2) ,
                        birth timestamp with time zone
                        );

                        '''

                    )

                    cur.execute(
                        '''
                        CREATE TABLE course(
                        id serial PRIMARY KEY ,
                        name varchar(100) NOT NULL
                        );

                        '''
                    )

                    cur.execute(
                        '''
                        CREATE TABLE education(
                        id serial PRIMARY KEY,
                        course_id INTEGER REFERENCES course(id) NOT NULL,
                        student_id INTEGER REFERENCES student(id) NOT NULL
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
