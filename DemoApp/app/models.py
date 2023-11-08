from DemoApp.app import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(255))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Laptop')
        # c4 = Category(name='PC')
        # db.session.add_all([c1, c2, c3, c4])
        # p1 = Product(name='iPhone 7 Plus', price='3000000', image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg', category_id='1')
        # p2 = Product(name='iPad Pro 2020', price='10000000', image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg', category_id='2')
        # p3 = Product(name='Galaxy Note 10 Plus', price='2500000', image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg', category_id='1')
        # p4 = Product(name='iPhone 10 Plus', price='4500000', image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg', category_id='1')
        # p5 = Product(name='iPad Pro 2021', price='15000000', image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg', category_id='2')
        # db.session.add_all([p1, p2, p3, p4, p5])
        # db.session.commit()
        db.create_all()