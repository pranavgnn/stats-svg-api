import contributions

box_size = 11 # px
padding = 1 # px

def get_box_svg(i, j, value):
    return f"""
    <rect
        id = \"{i}, {j}\"
        width = {box_size}
        height = {box_size}
        rx = 2.5
        transform = "translate({i * (box_size + padding)}, {j * (box_size + padding)})"
        fill = "{"#161b22" if value == 0 else "#26a641"}"
    />
    """

def get(username):
    svg_str = ""

    data = contributions.get(username)
    m, n = 0, 0

    for i, row in enumerate(data):
        if i > m:
            m = i

        for j, value in enumerate(row):
            if j > n:
                n = j

            svg_str += get_box_svg(i, j, value)

    svg_str = f"""
<svg
    width = "{m * box_size + (m - 1) * padding}"
    height = "{n * box_size + (n - 1) * padding}"
    fill = "none"
    xmlns = "http://www.w3.org/2000/svg"
    role = "img"
    aria-labelledby = "descId">
>
    <style>
        rect {{
            shape-renderer: crispEdges;
        }}
    </style>
    """ + svg_str + "\n</svg>"
        
    return svg_str