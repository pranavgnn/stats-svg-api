from flask import Flask, request, Response, render_template
import datetime
import svg

app = Flask(__name__)

@app.route("/<username>")
def make_svg(username):
    year = int(request.args.get("year", datetime.date.today().year))
    theme = request.args.get("theme", "light")

    svg_str = svg.make(username, year, theme)
    if not svg_str:
        return Response("Bad parameters", 400)

    return Response(svg_str, mimetype="image/svg+xml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)