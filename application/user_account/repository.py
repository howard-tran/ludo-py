from entities.user import User
from app import db

class Repository:
    def add_data_flush(self, data):
        db.session.add(data)
        db.session.flush()
        db.session.refresh(data)

    def commit(self):
        db.session.commit()

    def get_user_by_username(self, username):
        return db.session.query(User).filter(User.username==username).first()


repository = Repository()
