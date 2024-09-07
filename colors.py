import math

themes = {
    "dark": {
        "bg": "#161b22",
        1: "#0e4429",
        2: "#006d32",
        3: "#26a641",
        4: "#39d353",
    },
    
    "light": {
        "bg": "#ebedf0",
        1: "#9be9a8",
        2: "#40c463",
        3: "#30a14e",
        4: "#216e39"
    }
}


def get_box_color(theme, value, highest_value):
    if not theme in themes: return

    if value == 0:
        return themes[theme]["bg"]

    i = min(4, math.ceil(4 * value / highest_value))

    return themes[theme][i]