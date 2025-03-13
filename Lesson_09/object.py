from sqlalchemy import create_engine, text


class Object:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_list(self):
        res = self.db.execute("select user_email from users").fetchall()
        return len(res)

    def insert_object(self, us_email):
        sql = text("insert into users(\"user_email\") values (:email)")
        self.db.execute(sql, email=us_email)

    def update_object(self, us_mail, subject_id):
        sql = text("update users set subject_id = :sub_id where user_email = :email")
        self.db.execute(sql, sub_id=subject_id, email=us_mail)
        res = self.db.execute(text("select * from users where user_email = :email"),email = us_mail).fetchall()
        return res[0]["subject_id"]

    def delete_object(self, us_mail):
        sql = text("delete from users where user_email = :email")
        self.db.execute(sql, email=us_mail)

    def get_list_emails(self, us_mail):
        sql =  self.db.execute(text("select * from users where user_email = :email"),email = us_mail).fetchall()
        return len(sql)
