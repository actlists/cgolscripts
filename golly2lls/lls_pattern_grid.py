import golly as g
r = g.getselrect()
s = ""
p, tx, ty = g.getstring("""Enter period, x velocity, y velocity (P,X,Y) - Examples:
4,1,1 - Glider
4,0,2 - XWSS
3,0,1 - c/3o
6,2,1 - (2,1)c/6""", "4,1,1").split(",")
s1, s2, s3, s4, s5, s6 = g.getstring("Enter subperiods (or skip)", "1,0,0 2,0,0 3,0,0 4,0,0 5,0,0 6,0,0").split(" ")
p, tx, ty, s1, s2, s3, s4, s5, s6 = int(p), int(tx), int(ty), s1.split(","), s2.split(","), s3.split(","), s4.split(","), s5.split(","), s6.split(",")
w = r[2]
h = r[3]
for k in range(p+1):
    for i in range(h):
        for j in range(w):
            c = g.getcell(j+r[0], i+r[1]+h*k)
            d = c
            if (c > 9): d = c - 8
            if (c > 18): d = c - 17
            ss0 = f"v_{(j+[0,tx][k==p])%w}_{(i+[0,ty][k==p])%h}_,"
            sk1 = (int(s1[1]) if int(s1[1]) != 0 else 999999, int(s1[2]) if int(s1[2]) != 0 else 999999)
            sk2 = (int(s2[1]) if int(s2[1]) != 0 else 999999, int(s2[2]) if int(s2[2]) != 0 else 999999)
            sk3 = (int(s3[1]) if int(s3[1]) != 0 else 999999, int(s3[2]) if int(s3[2]) != 0 else 999999)
            sk4 = (int(s4[1]) if int(s4[1]) != 0 else 999999, int(s4[2]) if int(s4[2]) != 0 else 999999)
            sk5 = (int(s5[1]) if int(s5[1]) != 0 else 999999, int(s5[2]) if int(s5[2]) != 0 else 999999)
            sk6 = (int(s6[1]) if int(s6[1]) != 0 else 999999, int(s6[2]) if int(s6[2]) != 0 else 999999)
            
            ss1 = f"v_{(j+[0,tx][k==p])%w+k//sk1[0]}_{(i+[0,ty][k==p])%h+k//sk1[1]}_s1," if k%int(s1[0]) == 0 else "*,"
            ss2 = f"v_{(j+[0,tx][k==p])%w+k//sk1[0]}_{(i+[0,ty][k==p])%h+k//sk2[1]}_s2," if k%int(s2[0]) == 0 else "*,"
            ss3 = f"v_{(j+[0,tx][k==p])%w+k//sk1[0]}_{(i+[0,ty][k==p])%h+k//sk3[1]}_s3," if k%int(s3[0]) == 0 else "*,"
            ss4 = f"v_{(j+[0,tx][k==p])%w+k//sk1[0]}_{(i+[0,ty][k==p])%h+k//sk4[1]}_s4," if k%int(s4[0]) == 0 else "*,"
            ss5 = f"v_{(j+[0,tx][k==p])%w+k//sk1[0]}_{(i+[0,ty][k==p])%h+k//sk5[1]}_s5," if k%int(s5[0]) == 0 else "*,"
            ss6 = f"v_{(j+[0,tx][k==p])%w+k//sk1[0]}_{(i+[0,ty][k==p])%h+k//sk6[1]}_s6," if k%int(s6[0]) == 0 else "*,"
            s += ["0,", "1,", "*,", ss0, ss1, ss2, ss3, ss4, ss5, ss6, "1,"][d]
        s += "\n"
    s += "\n"

with open(r"//wsl.localhost/Ubuntu/home/sylvani/logic-life-search/pattern.txt", "w") as f:
    f.write(s)