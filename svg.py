import datetime
from ordinal import ordinal
import contributions
import colors

box_size = 11 # px
box_padding = 2 # px
chart_padding = (10, 30) # px
chart_position = (0.5, 0.825) # %

def get_tooltip_text(value, date):
    tooltip = ""

    tooltip += ("No" if value == 0 else str(value)) + " contributions" # No contributions / {value} contributions
    if value == 1: tooltip = tooltip[:-1] # 1 contribution / n contributions
    tooltip += " on " + date.strftime("%B") + " " + ordinal(date.day) + "." # on MONTH ordinal(day).

    return tooltip

def get_box_svg(i, j, value, tot_value, year, theme):

    date = datetime.date(year, 1, 1) + datetime.timedelta(days=value)

    return f"""
        <rect
            id='{i}, {j}'
            width='{box_size}'
            height='{box_size}'
            rx='2.5'
            transform='translate({i * (box_size + box_padding)}, {j * (box_size + box_padding)})'
            fill='{colors.get_box_color(theme, value, tot_value)}'
        >
            <title>
                {get_tooltip_text(value, date)}
            </title>
        </rect>
    """

def make_chart(username, year, theme):
    svg_str = ""

    data, highest_value = contributions.get(username, year)
    if not data or not highest_value: return None, None, None

    m, n = 0, 0

    for i, row in data.items():
        m = max(i, m)

        for j, value in row.items():
            n = max(j, n)
            svg_str += get_box_svg(i, j, value, highest_value, year, theme)

    chart_width = (m + 1) * box_size + m * box_padding
    chart_height = (n + 1) * box_size + n * box_padding

    svg_str = f"""
    <g
        transform='translate({
            int(2 * chart_position[0] * chart_padding[0])
        }, {
            int(2 * chart_position[1] * chart_padding[1])
        })'
    >
    """ + svg_str + """
    </g>
    """
        
    return svg_str, chart_width, chart_height

def make(username, year, theme):
    if theme not in colors.themes: return

    chart_svg, chart_width, chart_height = make_chart(username, year, theme)
    if not chart_svg or not chart_width or not chart_height: return

    svg_width = chart_width + 2 * chart_padding[0]
    svg_height = chart_height + 2 * chart_padding[1]

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

    <defs>
        <style type="text/css">
            @import url('https://fonts.googleapis.com/css?family=Roboto:400,100,100italic,300,300italic,400italic,500,500italic,700,700italic,900,900italic');
        </style>
    </defs>

    <rect
        fill='{colors.get_bg_color(theme)}'
        stroke='{colors.retrieve(theme, "border")}'
        stroke-width='3'
        width='{svg_width}'
        height='{svg_height}'
        rx='10'
    />

    <g>
        <text
            style='font-family: "Roboto";'
            x='50%' y='27'
            fill='{colors.get_text_color(theme)}'
            dominant-baseline='middle'
            text-anchor='middle'
        >
            Contributions in year {year}
        </text>
    </g>
    """ + chart_svg + "\n</svg>"

    return svg_str