from flask import Flask, request, Response
import datetime
import svg

app = Flask(__name__)

@app.route("/<username>")
def get_svg(username):
    year = int(request.args.get("year", datetime.date.today().year))
    theme = request.args.get("theme", "dark")

    svg_str = svg.get(username, year, theme)
    if not svg_str:
        return Response("Bad parameters", 400)

    return Response(svg_str, mimetype="image/svg+xml")

if __name__ == "__main__":
    app.run(debug=True)