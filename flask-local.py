import os
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()

@app.route("/")
def home():
    return(render_template("index.html"))

@app.route("/", methods=["GET", "POST"])
def search():
    value = request.form["text"]
    return(redirect("https://search.brave.com/search?q={}&source=web".format(value)))

if __name__ == "__main__":
    app.run(debug=True)
