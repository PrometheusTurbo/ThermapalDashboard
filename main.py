from flask import Flask
import database

app = Flask(__name__)

@app.route("/")
def home():
    return database.find({})


if __name__ == "__main__":
    app.run(debug=True)
