from collections import defaultdict
import json

key = ""
level = ""
criterion = defaultdict(dict)

with open('text/SC_S1_2223_M1.txt', 'r') as f:
    for line in f.read().splitlines():
        if "COMMENTS" in line:
            key = line
            criterion[key] = {
                "Weak": [],
                "Average": [],
                "Strong": []
            }
        elif line != '':
            if line.split("=")[1] in ["Weak", "Average", "Strong"]:
                level = line.split("=")[1]
            else:
                criterion[key][level].append(line.split("=")[1].replace("#N", "{name}").replace("#E", "{gender1}").replace("#e", "{gender4}").replace("#h", "{gender2}").replace("#m", "{gender3}"))

with open('text/test.json', 'w') as f:
    f.write(json.dumps(criterion, indent=2))