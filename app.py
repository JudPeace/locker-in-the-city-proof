from flask import Flask, jsonify, make_response, request
from Models import db, Product, Establishment, Price
from responses import responseObject, responseBadRequest, responseServerError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///judith.db"
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/api/products", methods=["POST"])
def addProduct():
    try:
        brand = request.form.get("brand")
        product_type = request.form.get("type")
        calories = request.form.get("calories")
        fats = request.form.get("fats")
        sugar = request.form.get("sugar")

        product = Product.query.filter_by(brand=brand, product_type=product_type).first()

        if product:
            return responseBadRequest()

        product = Product(
            brand=brand,
            product_type=product_type,
            calories=calories,
            fats=fats,
            sugar=sugar
        )
        if product.isValid():
            db.session.add(product)
            db.session.commit()
            return responseObject(product.serialize())
        else:
            return responseBadRequest()

    except Exception as e:
        return responseServerError()

@app.route("/api/products/<id>", methods=["PATCH"])
def editProduct(id):
    try:
        brand = request.form.get("brand")
        product_type = request.form.get("type")
        calories = request.form.get("calories")
        fats = request.form.get("fats")
        sugar = request.form.get("sugar")

        product = Product.query.filter_by(id=id).first()
        if not product:
            return responseBadRequest()

        product.modifySomeValues(brand, product_type, calories, fats, sugar)
        if product.isValid():
            db.session.commit()
            return responseObject(product.serialize())
        else:
            return responseBadRequest()
    except Exception as e:
        return responseServerError()

@app.route("/api/establishments", methods=["POST"])
def addEstablishment():
    try:
        name = request.form.get("name")
        address = request.form.get("address")
        opening_time = request.form.get("opening_time")
        closing_time = request.form.get("closing_time")

        establishment = Establishment.query.filter_by(name=name).first()

        if establishment:
            return responseBadRequest()

        establishment = Establishment(
            name=name,
            address=address,
            opening_time=opening_time,
            closing_time=closing_time
        )
        if establishment.isValid():
            db.session.add(establishment)
            db.session.commit()
            return responseObject(establishment.serialize())
        else:
            return responseBadRequest()
    except Exception as e:
        return responseServerError()

@app.route("/api/establishments/<name>/products/<id>/prices", methods=["POST"])
def addPrice(name,id):
    try:
        price_value = request.form.get("price")

        product = Product.query.filter_by(id=id).first()
        establishment = Establishment.query.filter_by(name=name).first()
        price = Price.query.filter_by(fk_product=id, fk_establishment=name).first()

        if not product or not establishment or price:
            return responseBadRequest()

        price = Price(
            fk_product=id,
            fk_establishment=name,
            price=price_value
        )
        if price.isValid():
            db.session.add(price)
            db.session.commit()
            return responseObject(price.serialize())
        else:
            return responseBadRequest()
    except Exception as e:
        return responseServerError()

@app.route("/api/establishments/<name>/products/prices", methods=["GET"])
def getAllPricesForEstablishment(name):
    try:
        prices = Price.query.filter_by(fk_establishment=name).all()
        json_prices = [price.serialize() for price in prices if price.product]
        return responseObject(json_prices)
    except Exception as e:
        return responseServerError()

if __name__ == '__main__':
    app.run(debug=True)