import contributions

box_size = 11 # px
padding = 1 # px

def get_box_svg(i, j, value):
    return f"""
    <rect
        id="{i}, {j}"
        width={box_size}
        height={box_size}
        rx=2.5
        transform="translate({i * (box_size + padding)}, {j * (box_size + padding)})"
        fill="{"#161b22" if value == 0 else "#26a641"}"
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

    svg_width = m * box_size + (m - 1) * padding
    svg_height = n * box_size + (n - 1) * padding

    svg_str = f"""
<svg
    width="{svg_width}"
    height="{svg_height}"
    viewBox="0 0 {svg_width} {svg_height}"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    style="isolation: isolate"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    role="img"
    aria-labelledby="descId">
>
    """ + svg_str + "\n</svg>"
        
    return svg_str