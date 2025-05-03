from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homePage():
    return "Nick's Flask app is up and running"

@app.route("/<name>", methods=["GET"])
def wishUser(name):
    return f"Hey {name}, Nickk wishes you Happy Coding :)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)