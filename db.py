import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = sqlite3.connect('animal.db', detect_types=sqlite3.PARSE_DECLTYPES)
conn.row_factory = dict_factory


def execute(sql, params):
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()


def select_one(sql):
    cursor = conn.cursor()
    result = cursor.execute(sql).fetchone()
    return result


def select_all(sql):
    cursor = conn.cursor()
    result = cursor.execute(sql).fetchall()
    return result
