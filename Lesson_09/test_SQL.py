from sqlalchemy import create_engine, text


db_connection_string = "postgresql://postgres:sss@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_db_connection():
    names = db.table_names()
    assert names[0] == 'users'


def test_insert():
    db = create_engine(db_connection_string)
    len_before = db.execute("select user_email from users").fetchall()
    sql = text("insert into users(\"user_email\") values (:new_user_email)")
    db.execute(sql, new_user_email="nikto@nail.ru")
    len_after = db.execute("select user_email from users").fetchall()
    assert len(len_after) - len(len_before) == 1


def test_update():
    db = create_engine(db_connection_string)
    sql = text("update users set subject_id = :sub_id where user_email = :us_mail")
    db.execute(sql, sub_id="8", us_mail="nikto@nail.ru")
    res = db.execute("select * from users where user_email = 'nikto@nail.ru'").fetchall()
    assert res[0]["subject_id"] == 8


def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from users where user_email = :us_mail")
    db.execute(sql, us_mail="nikto@nail.ru")
    len_after = db.execute("select * from users where user_email = 'nikto@nail.ru'").fetchall()
    assert len(len_after) == 0
