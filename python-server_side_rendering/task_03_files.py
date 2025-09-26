from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)

def read_products_json():
    with open("products.json", encoding="utf-8") as f:
        return json.load(f)

def read_products_csv():
    products = []
    with open("products.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        data = read_products_json()
    elif source == "csv":
        data = read_products_csv()
    else:
        return render_template("product_display.html", error="Wrong source", products=None)

    if product_id:
        try:
            pid = int(product_id)
            data = [p for p in data if p["id"] == pid]
            if not data:
                return render_template("product_display.html", error="Product not found", products=None)
        except ValueError:
            return render_template("product_display.html", error="Invalid id", products=None)

    return render_template("product_display.html", products=data, error=None)

if __name__ == '__main__':
    #app.run(debug=True,host= "0.0.0.0", port=80)
    app.run(debug=True, port=5000)
