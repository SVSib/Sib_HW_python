from sqlalchemy import create_engine, text


class Object:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def insert_object(self):
        len_before = self.db.execute("select user_email from users").fetchall()
        sql = text("insert into users(\"user_email\") values (:new_user_email)")
        self.db.execute(sql, new_user_email="nikto@nail.ru")
        len_after = self.db.execute("select user_email from users").fetchall()
        result = len(len_after) - len(len_before)
        return result

    def update_object(self):
        sql = text("update users set subject_id = :sub_id where user_email = :us_mail")
        self.db.execute(sql, sub_id="8", us_mail="nikto@nail.ru")
        res = self.db.execute("select * from users where user_email = 'nikto@nail.ru'").fetchall()
        return res[0]["subject_id"]

    def delete_object(self):
        sql = text("delete from users where user_email = :us_mail")
        self.db.execute(sql, us_mail="nikto@nail.ru")
        len_after = self.db.execute("select * from users where user_email = 'nikto@nail.ru'").fetchall()
        return len(len_after)
