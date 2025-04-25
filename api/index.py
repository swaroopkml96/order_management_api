from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'


# Dummy order storage
orders = {
    "1001": {
        "customer_name": "John Doe",
        "items": ["Men's POLO T-Shirt (1)", "Black Socks (1 Pair)"],
        "delivery_slot": "10 AM - 12 PM"
    },
    "1002": {
        "customer_name": "Jane Smith",
        "items": ["Chanel Handbag (1)"],
        "delivery_slot": "2 PM - 4 PM"
    }
}

@app.route('/order/<order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    if order:
        return jsonify(order)
    return jsonify({"error": "Order not found"}), 404

@app.route('/order/<order_id>/delivery_slot', methods=['POST'])
def update_delivery_slot(order_id):
    data = request.get_json()
    new_slot = data.get('delivery_slot')
    if order_id in orders:
        orders[order_id]['delivery_slot'] = new_slot
        return jsonify({"message": "Delivery slot updated successfully"})
    return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(debug=False)
