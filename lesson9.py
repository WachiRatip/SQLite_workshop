import os 
import re

path = os.path.join(".", "examples", "mock_data.txt")

with open(path, "r") as file:
    raw = file.read()

list_raw = raw.split("\n")

data = []

for item in list_raw:
    years = ''.join(re.findall(r"^.*?\([^\d]*(\d+)[^\d]*\).*$", item))
    temps = ''.join(re.findall(r"=([^\=]\d+)", item)).replace(" ", "")
    data.append(
        (int(years), float(temps))
    )

print(data, type(data))