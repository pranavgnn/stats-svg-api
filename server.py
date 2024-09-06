from flask import Flask, Response
import svg

app = Flask(__name__)

@app.route("/<username>")
def get_svg(username):
    svg_str = svg.get(username)
    return Response(svg_str, mimetype="image/svg+xml")

if __name__ == "__main__":
    app.run(debug=True)