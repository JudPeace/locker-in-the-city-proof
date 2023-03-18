from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'
    __table_args__ = (db.UniqueConstraint('brand', 'type'), )
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    brand = db.Column(db.String(200), nullable = False)
    product_type = db.Column('type', db.String(200), nullable = False)
    calories = db.Column(db.Float, nullable = False)
    fats = db.Column(db.Float, nullable = False)
    sugar = db.Column(db.Float, nullable = False)

    def isValid(self):
        if not (self.brand and self.product_type and self.calories and self.fats and self.sugar):
            return False
        if not (self.calories.isnumeric() and isFloat(self.sugar) and isFloat(self.fats) and
            float(self.sugar) <= 100 and float(self.sugar) >= 0 and float(self.fats) <= 100 and float(self.fats) >= 0):
            return False
        return True

    def serialize(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'product_type': self.product_type,
            'calories': self.calories,
            'fats': self.fats,
            'sugar': self.sugar
        }
    
    def modifySomeValues(self, brand, product_type, calories, fats, sugar):
        self.brand = brand if brand else self.brand
        self.product_type = product_type if product_type else self.product_type
        self.calories = calories if calories else self.calories
        self.fats = fats if fats else self.fats
        self.sugar = sugar if sugar else self.sugar



class Establishment(db.Model):
    __tablename__ = 'establishments'
    name = db.Column(db.String(200), primary_key = True)
    address = db.Column(db.String(200), nullable = False)
    opening_time = db.Column(db.String(200), nullable = False)
    closing_time = db.Column(db.String(200), nullable = False)

    def isValid(self):
        if not (self.name and self.address and self.opening_time and self.closing_time):
            return False
        return True

    def serialize(self):
        return {
            'name': self.name,
            'address': self.address,
            'opening_time': self.opening_time,
            'closing_time': self.closing_time
        }



class Price(db.Model):
    __tablename__ = 'prices'
    __table_args__ = (db.UniqueConstraint('fk_product', 'fk_establishment'), )
    id = db.Column('id', db.Integer, primary_key = True, autoincrement = True)
    fk_product = db.Column(db.Integer, db.ForeignKey('products.id'), nullable = False)
    product = db.relationship("Product", backref = "products")
    fk_establishment = db.Column(db.String(200), db.ForeignKey('establishments.name'), nullable=False)
    price = db.Column(db.Float, nullable = False)

    def isValid(self):
        if not (self.fk_product and self.fk_establishment and self.price):
            return False
        if not (self.fk_product.isnumeric() and isFloat(self.price) and float(self.price) >= 0):
            return False
        return True

    def serialize(self):
        return {
            'id': self.id,
            'product': self.product.serialize(),
            'establishment': self.fk_establishment,
            'price': self.price
        }

def isFloat(possible_number):
    try:
        float(possible_number)
        return True
    except:
        return False