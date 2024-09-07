import contributions
import colors

box_size = 11 # px
padding = 1 # px

def get_box_svg(i, j, value, tot_value, theme):
    return f"""
    <rect
        id='{i}, {j}'
        width='{box_size}'
        height='{box_size}'
        rx='2.5'
        transform='translate({i * (box_size + padding)}, {j * (box_size + padding)})'
        fill='{colors.get_box_color(theme, value, tot_value)}'
    />
    """

def get(username, year, theme):
    if theme not in colors.themes: return

    svg_str = ""

    data, highest_value = contributions.get(username, year)
    if not data or not highest_value: return

    m, n = 0, 0

    for i, row in data.items():
        m = max(i, m)

        for j, value in row.items():
            n = max(j, n)
            svg_str += get_box_svg(i, j, value, highest_value, theme)

    svg_width = (m + 1) * box_size + m * padding
    svg_height = (n + 1) * box_size + n * padding

    svg_str = f"""
<svg
    xmlns='http://www.w3.org/2000/svg'
    xmlns:xlink='http://www.w3.org/1999/xlink'
    width='{svg_width}'
    height='{svg_height}'
    viewBox='0 0 {svg_width} {svg_height}'
    style='isolation: isolate'
    fill='none'
    role='img'
>
    """ + svg_str + "\n</svg>"
        
    return svg_str