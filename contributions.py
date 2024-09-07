import requests
import re
from bs4 import BeautifulSoup

url = "https://github.com/users/USERNAME/contributions"

def get_params(year):
    return {
        "from": f"{year}-01-01",
        "to": f"{year}-12-01",
        "tab": "overview",
    }

def get_boxes(username, year):
    response = requests.get(url.replace("USERNAME", username), params=get_params(year))
    if response.status_code != 200: return

    soup = BeautifulSoup(response.content, "html.parser")

    return soup.find_all("td", {"tabindex" : "0"})

  
def get_box_indices(box):
    id = box["id"]
    i = int(re.findall("(\\d+)$", id)[0])
    j = int(re.findall("-(\\d+)-", id)[0])

    x = i * 53 + j
    i = x // 53
    j = x % 53

    return i, j

def get_box_value(box):
    tooltip = box.parent.find("tool-tip", {"for": box["id"]})
    if not tooltip: return 0

    value = re.findall("^(\\d+)", tooltip.text.strip())
    value = int(value[0]) if value else 0

    return value

def get(username, year):
    data = {}
    highest_value = 0

    boxes = get_boxes(username, year)
    if not boxes: return None, None

    for box in boxes:
        i, j = get_box_indices(box)

        if not i in data:
            data[i] = {}

        value = get_box_value(box)

        data[i][j] = value
        highest_value = max(highest_value, value)

    return data, highest_value