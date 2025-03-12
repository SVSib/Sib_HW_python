from object import Object


db = Object("postgresql://postgres:sss@localhost:5432/QA")


def test_insert():
    db_result = db.insert_object()
    assert db_result == 1


def test_update():
    db_result = db.update_object()
    assert db_result == 8


def test_delete():
    db_result = db.delete_object()
    assert db_result == 0
