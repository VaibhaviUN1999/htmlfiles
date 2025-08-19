from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/products")
def get_products():
    data = [
        {"id": 1, "name": "Laptop", "price": 50000},
        {"id": 2, "name": "Mobile", "price": 20000}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
