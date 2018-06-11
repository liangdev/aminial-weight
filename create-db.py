import db

sqls = """
CREATE TABLE IF NOT EXISTS animal_weights (
 id integer primary key autoincrement,
 weight float NOT NULL,
 weigh_date  varcha(255) NOT NULL
);

insert into animal_weights 
(id,weight,weigh_date)
values
(null,420,'2018-03-05T12:00:00Z');

insert into animal_weights 
(id,weight,weigh_date)
values
(null,430,'2018-03-07T12:00:00Z');

insert into animal_weights 
(id,weight,weigh_date)
values
(null,490,'2018-03-09T12:00:00Z');

"""


def create_table():
    cursor = db.conn.cursor()
    for sql in sqls.split(';'):
        cursor.execute(sql)
    db.conn.commit()
    db.conn.close()


if __name__ == "__main__":
    create_table()
