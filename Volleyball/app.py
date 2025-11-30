from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Flask is working!"})

if __name__ == "__main__":
    app.run(debug=True)


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/hello")
def hello():
    return jsonify(message="Flask working!")

if __name__ == "__main__":
    app.run(debug=True)