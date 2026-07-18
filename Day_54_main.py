from flask import Flask

# 1. Create an instance of the Flask class.
# This represents your core web application configuration.
app = Flask(__name__)

# 2. Define a route using a decorator (@app.route)
# This tells Flask which web address URL should trigger this specific function.
@app.route("/")
def home():
    """Triggers when someone visits http://127.0.0.1:5000/"""
    return "<h1>Hello, World!</h1><p>Welcome to my first web app built with Flask.</p>"

# 3. Create a second route to show how paths work
@app.route("/about")
def about():
    """Triggers when someone visits http://127.0.0.1:5000/about"""
    return "<h2>About Page</h2><p>Flask makes creating backend paths incredibly easy!</p>"


if __name__ == "__main__":
    # Run the application on your local machine
    # debug=True automatically reloads the server whenever you save code changes.
    app.run(debug=True)