from object import Object


db = Object("postgresql://postgres:sss@localhost:5432/QA")


def test_insert():
    len_before  = db.get_list()
    email = "nikto@nail.ru"
    db.insert_object(email)
    len_after = db.get_list()
    db.delete_object(email)
    assert len_after - len_before == 1


def test_update():
    email = "nikto@nail.ru"
    sub_id = "8"
    db.insert_object(email)
    db_result = db.update_object(email, sub_id)
    db.delete_object(email)
    assert db_result == 8


def test_delete():
    email = "nikto@nail.ru"
    db.insert_object(email)
    db.delete_object(email)
    res = db.get_list_emails(email)
    assert res == 0
