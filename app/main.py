from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_view():
    return "<h1>Lab 2 Turkoliak Viktoriia KN-410</h1>"


