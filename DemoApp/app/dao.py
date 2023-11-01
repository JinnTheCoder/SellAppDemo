from DemoApp.app.models import Category, Product

def load_categories():
    return Category.query.all()

def load_product(kw=None):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    return products.all()