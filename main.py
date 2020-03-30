import psycopg2 as pg

from config import HOST, DB, DB_USER, DB_PASSWORD
from tools import api

try:
    with pg.connect(f'host={HOST} dbname={DB} user={DB_USER} password={DB_PASSWORD}') as conn:
        api.create_db(conn)
        print(
            'Добавил студента:',
            api.add_student(conn, {
                'name': 'Иван Фролов',
                'birth': '2001-12-23',
            })
        )
        print(
            'Добавил курс:',
            api.add_course(conn, {
                'name': 'Java'
            }))
    print(
        'Записал студентов на курс:',
        api.add_students(conn, 1, [
            {
                'name': 'Александр Сидоров',
                'birth': '2000-10-20',
            },
            {
                'name': 'Иван Ранко',
                'birth': '2001-03-12',
            }
        ])
    )
    print('Получил студента по id:', api.get_student(conn, 1))
    print('Получил студентов по id курса:', api.get_students(conn, 1))
except pg.Error as e:
    print('Ошибка подключения к базе данных! Проверьте настройки подключения.')
