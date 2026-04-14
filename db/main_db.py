import sqlite3

from config import path_db
from db import queries


def init_db():
    conn = sqlite3.connect(path_db)     # Соединение к БД
    cursor = conn.cursor()              # Исполнитель который относит запросы к БД
    cursor.execute(queries.tasks_table)
    # cursor.execute('select * from tasks')
    conn.commit()                       # Зафиксировать измения в БД
    conn.close()                        # Закрываем соедение
