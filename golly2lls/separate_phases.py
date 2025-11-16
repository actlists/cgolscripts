import golly as g

period = int(g.getstring("Enter the desired number of steps", "1"))
cells = []

for i in range(period):
    cells.append(g.getcells(g.getselrect()))
    g.run(1)
g.clear(0)
g.clear(1)
for i, c in enumerate(cells):
    g.putcells(c, i * g.getselrect()[2], 0)