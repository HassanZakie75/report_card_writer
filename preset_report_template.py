# template for report writing by Hassan Zakie
# acknoledgment for Murthadza code contribution
from collections import defaultdict

SUBJECT = "SC"
LEVEL = "M4"

def read_text(subject, level):
    key = ""
    grade = ""
    criterion = defaultdict(dict)

    with open(f'text/{subject}_S1_2223_{level}.txt', 'r') as f:
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
                    grade = line.split("=")[1]
                else:
                    criterion[key][grade].append(line.split("=")[1].replace("#N", "{name}").replace("#E", "{name}").replace("#e", "{gender4}").replace("#h", "{gender2}").replace("#m", "{gender3}"))
    return criterion

CRITERION = read_text(SUBJECT, LEVEL)

def get_crit_a_weak(name, gender1, gender2, gender3, gender4):
    return [s.format(name=name, gender1=gender1, gender2=gender2, gender3=gender3, gender4=gender4) for s in CRITERION[f"COMMENTS: S1 {SUBJECT} 22/23 {LEVEL} 01. Crit A"]["Weak"]]

def get_crit_a_average(name, gender1, gender2, gender3, gender4):
    return [s.format(name=name, gender1=gender1, gender2=gender2, gender3=gender3, gender4=gender4) for s in CRITERION[f"COMMENTS: S1 {SUBJECT} 22/23 {LEVEL} 01. Crit A"]["Average"]]

def get_crit_a_strong(name, gender1, gender2, gender3, gender4):
    return [s.format(name=name, gender1=gender1, gender2=gender2, gender3=gender3, gender4=gender4) for s in CRITERION[f"COMMENTS: S1 {SUBJECT} 22/23 {LEVEL} 01. Crit A"]["Strong"]]

def get_crit_b_weak(name, gender1, gender2, gender3, gender4):
    return [s.format(name=name, gender1=gender1, gender2=gender2, gender3=gender3, gender4=gender4) for s in CRITERION[f"COMMENTS: S1 {SUBJECT} 22/23 {LEVEL} 02. Crit B"]["Weak"]]

def get_crit_b_average(name, gender1, gender2, gender3, gender4):
    return [s.format(name=name, gender1=gender1, gender2=gender2, gender3=gender3, gender4=gender4) for s in CRITERION[f"COMMENTS: S1 {SUBJECT} 22/23 {LEVEL} 02. Crit B"]["Average"]]

def get_crit_b_strong(name, gender1, gender2, gender3, gender4):
    return [s.format(name=name, gender1=gender1, gender2=gender2, gender3=gender3, gender4=gender4) for s in CRITERION[f"COMMENTS: S1 {SUBJECT} 22/23 {LEVEL} 02. Crit B"]["Strong"]]

def get_crit_c_weak(name, gender1, gender2, gender3, gender4):
    return [s.format(name=name, gender1=gender1, gender2=gender2, gender3=gender3, gender4=gender4) for s in CRITERION[f"COMMENTS: S1 {SUBJECT} 22/23 {LEVEL} 03. Crit C"]["Weak"]]

def get_crit_c_average(name, gender1, gender2, gender3, gender4):
    return [s.format(name=name, gender1=gender1, gender2=gender2, gender3=gender3, gender4=gender4) for s in CRITERION[f"COMMENTS: S1 {SUBJECT} 22/23 {LEVEL} 03. Crit C"]["Average"]]

def get_crit_c_strong(name, gender1, gender2, gender3, gender4):
    return [s.format(name=name, gender1=gender1, gender2=gender2, gender3=gender3, gender4=gender4) for s in CRITERION[f"COMMENTS: S1 {SUBJECT} 22/23 {LEVEL} 03. Crit C"]["Strong"]]

def get_crit_d_weak(name, gender1, gender2, gender3, gender4):
    return [s.format(name=name, gender1=gender1, gender2=gender2, gender3=gender3, gender4=gender4) for s in CRITERION[f"COMMENTS: S1 {SUBJECT} 22/23 {LEVEL} 04. Crit D"]["Weak"]]

def get_crit_d_average(name, gender1, gender2, gender3, gender4):
    return [s.format(name=name, gender1=gender1, gender2=gender2, gender3=gender3, gender4=gender4) for s in CRITERION[f"COMMENTS: S1 {SUBJECT} 22/23 {LEVEL} 04. Crit D"]["Average"]]

def get_crit_d_strong(name, gender1, gender2, gender3, gender4):
    return [s.format(name=name, gender1=gender1, gender2=gender2, gender3=gender3, gender4=gender4) for s in CRITERION[f"COMMENTS: S1 {SUBJECT} 22/23 {LEVEL} 04. Crit D"]["Strong"]]
