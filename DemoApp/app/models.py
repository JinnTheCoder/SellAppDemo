from DemoApp.app import db, app
from sqlalchemy import Column, Integer, String

class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

if __name__ == '__main__':
    with app.app_context():
        c1 = Category(name='Mobile')
        c2 = Category(name='Tablet')

        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()
        # db.create_all()