import golly as g
r = g.getrect()
s = ""
p, tx, ty = g.getstring("""Enter period, x velocity, y velocity (P,X,Y) - Examples:
4,1,1 - Glider
4,0,2 - XWSS
3,0,1 - c/3o
6,2,1 - (2,1)c/6""", "4,1,1").split(",")
s1, s2, s3, s4, s5, s6 = g.getstring("Enter subperiods (or skip)", "1,2,3,4,5,6").split(",")
p, tx, ty, s1, s2, s3, s4, s5, s6 = int(p), int(tx), int(ty), int(s1), int(s2), int(s3), int(s4), int(s5), int(s6)
w = r[2]//(p+1)
h = r[3]
for k in range(p+1):
    for i in range(r[3]):
        for j in range(r[2]):
            c = g.getcell(j+r[0], i+r[1])
            ss0 = f"v_{j+[0,tx][k==p]}_{i+[0,ty][k==p]}_{k%p},"
            ss1 = f"v_{j+[0,tx][k==p]}_{i+[0,ty][k==p]}_{k%s1}_s1,"
            ss2 = f"v_{j+[0,tx][k==p]}_{i+[0,ty][k==p]}_{k%s2}_s2,"
            ss3 = f"v_{j+[0,tx][k==p]}_{i+[0,ty][k==p]}_{k%s3}_s3,"
            ss4 = f"v_{j+[0,tx][k==p]}_{i+[0,ty][k==p]}_{k%s4}_s4,"
            ss5 = f"v_{j+[0,tx][k==p]}_{i+[0,ty][k==p]}_{k%s5}_s5,"
            ss6 = f"v_{j+[0,tx][k==p]}_{i+[0,ty][k==p]}_{k%s6}_s6,"
            s += ["0,", "1,", "*,", ss0, ss1, ss2, ss3, ss4, ss5, ss6][c]
        s += "\n"
    s += "\n"
    if k != p: g.run(1)

with open(r"//wsl.localhost/Ubuntu/home/user/logic-life-search/pattern.txt", "w") as f: # Example path (used for WSL2)
    f.write(s)