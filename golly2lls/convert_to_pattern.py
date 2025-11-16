import golly as g

period = int(g.getstring("Enter the duration of the pattern.", "1"))
subperiods = list(map(int, g.getstring("Enter the subperiod(s) of the pattern.", "999 999 999 999 999 999").split(" ")))
translation = list(map(int, g.getstring("Enter the translation of the pattern.", "0 0").split(" ")))
loop_duration = g.getstring("Is the pattern periodic?", "y") # If True, then it places generation 0 at the end of the final pattern.
separate_phases = True # If True, then stack phases side by side. (Usually on by default. There's a helper script for this.)

file_path = r"\\wsl.localhost\Ubuntu\home\sylvani\logic-life-search\pattern.txt"


# Actual code starts here
state_map = ["0", "1", "*", "S1", "S2", "S3", "S4", "S5", "S6", "*", "S1", "S2", "S3", "S4", "S5", "S6", "0'", "1'", "*'", "S1'", "S2'", "S3'", "S4'", "S5'", "S6'", "*'", "S1'", "S2'", "S3'", "S4'", "S5'", "S6'"]
bbox = g.getselrect()

s = ""
s2 = ""

def get(x, y, p):
    c = state_map[g.getcell(x+bbox[0]+p*separate_phases*bbox[2], y+bbox[1])]
    if c.startswith("S"):
        if subperiods[int(c[1])-1] == 1:
            c2 = f"{c}_{x}_{y}"
        elif p % subperiods[int(c[1])-1] == 0:
            c2 = f"{c}_{x}_{y}"
        else:
            c2 = "*"
        if c.endswith("'"):
            c2 += "'"
        return c2
    else:
        return c

if loop_duration.lower().strip().startswith("y"):
    for j in range(bbox[3]):
        s2 += " ".join(get(k + translation[0], j + translation[1], 0) for k in range(bbox[2])) + "\n"
    s2 += "\n"
        
for i in range(period):
    for j in range(bbox[3]):
        s += " ".join(get(k, j, i) for k in range(bbox[2])) + "\n"
    s += "\n"
    if not separate_phases: g.run(1)

with open(file_path, "w") as f:
    f.write(s + s2)