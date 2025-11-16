import golly as g

subp = g.getstring("Enter the subperiod to change into (can be 0 or * and have apostrophes as well)", "1")

subp_map = {
    "0": [0, 1],
    "*": [2, 9],
    "1": [3, 10],
    "2": [4, 11],
    "3": [5, 12],
    "4": [6, 13],
    "5": [7, 14],
    "6": [8, 15],
    "0'": [16, 24],
    "*'": [17, 25],
    "1'": [18, 26],
    "2'": [19, 27],
    "3'": [20, 28],
    "4'": [21, 29],
    "5'": [22, 30],
    "6'": [23, 31],
}[subp]

def change_subp(x, y):
    c = g.getcell(x, y)
    if c != 1:
        g.setcell(x, y, subp_map[0])
    else:
        g.setcell(x, y, subp_map[1])

s = g.getselrect()

for x in range(s[0], s[0]+s[2]):
    for y in range(s[1], s[1]+s[3]):
        change_subp(x, y)


   