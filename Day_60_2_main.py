from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# Accept both GET and POST requests on this route
@app.route("/login", methods=["POST"])
def receive_data():
    if request.method == "POST":
        # Access form input values by their HTML 'name' attributes
        username = request.form["username"]
        password = request.form["password"]

        return f"<h1>Name: {username}, Password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)