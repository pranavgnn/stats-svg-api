from flask import Flask
import svg

app = Flask(__name__)

@app.route("/<username>")
def home(username):
    return svg.get(username)

if __name__ == "__main__":
    app.run(debug=True)