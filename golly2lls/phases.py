import golly as g

x, y, w, h = g.getselrect()
c = g.getcells(g.getselrect())
p = int(g.getstring("Enter the period of the pattern", "4"))
for i in range(p):
    c = g.evolve(c, 1)
    g.putcells(c, 0, (i + 1) * h)
