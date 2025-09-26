from flask import Flask, render_template, request
import json, csv, sqlite3

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

def read_products_sql():
    products = []
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for r in rows:
            products.append({
                "id": r[0],
                "name": r[1],
                "category": r[2],
                "price": r[3]
            })
        conn.close()
    except Exception as e:
        return None, str(e)
    return products, None

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    data = None
    error = None

    if source == "json":
        try:
            data = read_products_json()
        except Exception as e:
            error = str(e)
    elif source == "csv":
        try:
            data = read_products_csv()
        except Exception as e:
            error = str(e)
    elif source == "sql":
        data, error = read_products_sql()
    else:
        return render_template("product_display.html", error="Wrong source", products=None)

    if error:
        return render_template("product_display.html", error=error, products=None)

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
    # app.run(debug=True,host= "0.0.0.0", port=80)
    app.run(debug=True, port=5000)
