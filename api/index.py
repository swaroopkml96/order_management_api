from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tinsel Boutique</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Roboto', sans-serif;
      margin: 0;
      padding: 0;
      background: #fefefe;
      color: #333;
    }
    header {
      background: #1a1a1a;
      color: #fff;
      padding: 20px 40px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    header h1 {
      margin: 0;
    }
    nav a {
      color: #fff;
      margin-left: 20px;
      text-decoration: none;
    }
    .hero {
      background: url('https://images.unsplash.com/photo-1541099649105-f69ad21f3246?fit=crop&w=1600&q=80') no-repeat center center/cover;
      height: 80vh;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      text-align: center;
    }
    .hero h2 {
      font-size: 3rem;
      max-width: 600px;
      background-color: rgba(0,0,0,0.5);
      padding: 20px;
    }
    .section {
      padding: 60px 40px;
    }
    .products {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
    }
    .product {
      border: 1px solid #ddd;
      border-radius: 8px;
      overflow: hidden;
      text-align: center;
      background: #fff;
    }
    .product img {
      width: 100%;
      height: 300px;
      object-fit: cover;
    }
    .product h3 {
      margin: 10px 0;
    }
    footer {
      background: #1a1a1a;
      color: #fff;
      text-align: center;
      padding: 20px 0;
    }
  </style>
  <script
    src='//in.fw-cdn.com/32105796/1124000.js'
    chat='true' widgetId='a5ecc622-9123-48be-9c68-8e87f22a454b'>
  </script>
</head>
<body>
  <header>
    <h1>Tinsel Boutique</h1>
    <nav>
      <a href="#men">Men</a>
      <a href="#women">Women</a>
      <a href="#contact">Contact</a>
    </nav>
  </header>

  <div class="hero">
    <h2>Elevate your style with our curated fashion for men & women</h2>
  </div>

  <section class="section" id="men">
    <h2>Men's Collection</h2>
    <div class="products">
      <div class="product">
        <img src="https://images.unsplash.com/photo-1600180758890-6f3f06df6655?fit=crop&w=800&q=80" alt="Men's Shirt">
        <h3>Classic Shirt</h3>
        <p>$45</p>
      </div>
      <div class="product">
        <img src="https://images.unsplash.com/photo-1593032465174-eec73fcd338a?fit=crop&w=800&q=80" alt="Men's Jacket">
        <h3>Urban Jacket</h3>
        <p>$89</p>
      </div>
    </div>
  </section>

  <section class="section" id="women">
    <h2>Women's Collection</h2>
    <div class="products">
      <div class="product">
        <img src="https://images.unsplash.com/photo-1621086893821-3ecb6590c20a?fit=crop&w=800&q=80" alt="Women's Dress">
        <h3>Summer Dress</h3>
        <p>$65</p>
      </div>
      <div class="product">
        <img src="https://images.unsplash.com/photo-1535827841776-24afc1e255ac?fit=crop&w=800&q=80" alt="Women's Blazer">
        <h3>Elegant Blazer</h3>
        <p>$99</p>
      </div>
    </div>
  </section>

  <section class="section" id="contact">
    <h2>Contact Us</h2>
    <p>Email: hello@tinselboutique.com</p>
    <p>Phone: +1 (234) 567-8901</p>
    <p>Follow us on Instagram @tinsel.boutique</p>
  </section>

  <footer>
    <p>&copy; 2025 Tinsel Boutique. All rights reserved.</p>
  </footer>
</body>
</html>
"""

@app.route('/')
def homepage():
    return render_template_string(html_page)


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
