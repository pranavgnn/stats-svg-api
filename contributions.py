import requests
import datetime
import re
from bs4 import BeautifulSoup

url = "https://github.com/users/USERNAME/contributions"

current_year = datetime.date.today().year

def get_params(year=current_year):
    return {
        "from": f"{year}-01-01",
        "to": f"{year}-12-01",
        "tab": "overview",
    }

def get_boxes(username, year=current_year):
    response = requests.get(url.replace("USERNAME", username), params=get_params(year))
    if response.status_code != 200: return

    soup = BeautifulSoup(response.content, "html.parser")

    return soup.find_all("td", {"tabindex" : "0"})
    
def get_box_indices(box):
    id = box["id"]
    j = int(re.findall("-(\\d+)-", id)[0])
    i = int(re.findall("(\\d+)$", id)[0])

    return i, j

def get_box_value(box):
    tooltip = box.parent.find("tool-tip", {"for": box["id"]})
    if not tooltip: return 0

    value = re.findall("^(\\d)", tooltip.text.strip())
    value = int(value[0]) if value else 0

    return value

def get(username, year=current_year):
    data = []

    boxes = get_boxes(username, year)
    if not boxes: return data

    for box in boxes:
        i, j = get_box_indices(box)

        while len(data) <= i:
            data.append([])

        while len(data[i]) <= j:
            data[i].append(0)

        data[i][j] = get_box_value(box)

    return data