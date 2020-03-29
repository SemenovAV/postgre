import psycopg2 as pg


def create_db():
    '''
    Создает таблицы.
    :return:
    '''
    with pg.connect("dbname=netology_db user=netology_user password=pass") as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE student (id serial PRIMARY KEY, name varchar(100),
                 gpa numeric(10, 2), birth timestamp with time zone);
                 """)


if __name__ == '__main__':
    create_db()
