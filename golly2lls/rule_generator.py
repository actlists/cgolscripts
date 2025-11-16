import golly as g

# code from https://conwaylife.com/forums/viewtopic.php?f=11&t=4523&p=97698
hensel = {0: {"a": [0, 0, 0, 0, 0, 0, 0, 0]},
          1: {"c": [1, 0, 0, 0, 0, 0, 0, 0], "e": [0, 1, 0, 0, 0, 0, 0, 0]},
          2: {"c": [1, 0, 1, 0, 0, 0, 0, 0], "e": [0, 1, 0, 0, 0, 0, 0, 1],
              "k": [0, 1, 0, 0, 1, 0, 0, 0], "a": [1, 1, 0, 0, 0, 0, 0, 0],
              "i": [0, 1, 0, 0, 0, 1, 0, 0], "n": [1, 0, 0, 0, 1, 0, 0, 0]},
          3: {"c": [1, 0, 1, 0, 1, 0, 0, 0], "e": [0, 1, 0, 1, 0, 0, 0, 1],
              "k": [0, 1, 0, 0, 1, 0, 0, 1], "a": [1, 1, 0, 0, 0, 0, 0, 1],
              "i": [1, 0, 0, 0, 0, 0, 1, 1], "n": [1, 0, 1, 0, 0, 0, 0, 1],
              "y": [1, 0, 1, 0, 0, 1, 0, 0], "q": [1, 0, 0, 0, 1, 0, 0, 1],
              "j": [0, 0, 1, 1, 0, 1, 0, 0], "r": [0, 1, 1, 0, 0, 1, 0, 0]},
          4: {"c": [1, 0, 1, 0, 1, 0, 1, 0], "e": [0, 1, 0, 1, 0, 1, 0, 1],
              "k": [0, 1, 1, 0, 1, 0, 0, 1], "a": [1, 0, 0, 0, 0, 1, 1, 1],
              "i": [1, 0, 1, 1, 0, 0, 0, 1], "n": [1, 0, 0, 0, 1, 0, 1, 1],
              "y": [1, 0, 1, 0, 0, 1, 1, 0], "q": [1, 1, 0, 0, 1, 0, 0, 1],
              "j": [0, 0, 1, 1, 0, 1, 0, 1], "r": [0, 1, 1, 1, 0, 1, 0, 0],
              "t": [1, 1, 1, 0, 0, 1, 0, 0], "w": [1, 0, 0, 0, 1, 1, 0, 1],
              "z": [1, 1, 0, 0, 1, 1, 0, 0]},
          5: {"c": [0, 1, 0, 1, 0, 1, 1, 1], "e": [1, 0, 1, 0, 1, 1, 1, 0],
              "k": [1, 0, 1, 1, 0, 1, 1, 0], "a": [0, 0, 1, 1, 1, 1, 1, 0],
              "i": [0, 1, 1, 1, 1, 1, 0, 0], "n": [0, 1, 0, 1, 1, 1, 1, 0],
              "y": [0, 1, 0, 1, 1, 0, 1, 1], "q": [0, 1, 1, 1, 0, 1, 1, 0],
              "j": [1, 1, 0, 0, 1, 0, 1, 1], "r": [1, 0, 0, 1, 1, 0, 1, 1]},
          6: {"c": [0, 1, 0, 1, 1, 1, 1, 1], "e": [1, 0, 1, 1, 1, 1, 1, 0],
              "k": [1, 0, 1, 1, 0, 1, 1, 1], "a": [0, 0, 1, 1, 1, 1, 1, 1],
              "i": [1, 0, 1, 1, 1, 0, 1, 1], "n": [0, 1, 1, 1, 0, 1, 1, 1]},
          7: {"c": [0, 1, 1, 1, 1, 1, 1, 1], "e": [1, 0, 1, 1, 1, 1, 1, 1]},
          8: {"a": [1, 1, 1, 1, 1, 1, 1, 1]}}


def rotate(neighbours):
    return neighbours[2:8] + neighbours[:2]


def reflect_1(neighbours):
    return [neighbours[2], neighbours[1], neighbours[0], neighbours[7],
            neighbours[6], neighbours[5], neighbours[4], neighbours[3]]


def reflect_2(neighbours):
    return [neighbours[6], neighbours[5], neighbours[4], neighbours[3],
            neighbours[2], neighbours[1], neighbours[0], neighbours[7]]


def rotate_4_reflect(neighbours):
    lst = []
    rotate_1 = rotate(neighbours)
    rotate_2 = rotate(rotate_1)
    rotate_3 = rotate(rotate_2)

    lst.append(tuple(neighbours))
    lst.append(tuple(reflect_1(neighbours)))
    lst.append(tuple(reflect_2(neighbours)))

    lst.append(tuple(rotate_1))
    lst.append(tuple(reflect_1(rotate_1)))
    lst.append(tuple(reflect_2(rotate_1)))

    lst.append(tuple(rotate_2))
    lst.append(tuple(reflect_1(rotate_2)))
    lst.append(tuple(reflect_2(rotate_2)))

    lst.append(tuple(rotate_3))
    lst.append(tuple(reflect_1(rotate_3)))
    lst.append(tuple(reflect_2(rotate_3)))
    return lst


def get_trans_moore(string):
    trans = []
    current_num = 0
    subtract = False
    totalistic = False
    for i in string:
        try:
            prev_num = current_num
            current_num = int(i)
            subtract = False
            if totalistic:
                for transition in hensel[prev_num]:
                    trans += rotate_4_reflect(hensel[prev_num][transition])

            if string[-1] == i:
                for transition in hensel[current_num]:
                    trans += rotate_4_reflect(hensel[current_num][transition])

            totalistic = True

        except ValueError:
            totalistic = False
            if i != "-":
                if not subtract:
                    trans += rotate_4_reflect(hensel[current_num][i])
                else:
                    for transition in rotate_4_reflect(hensel[current_num][i]):
                        trans.remove(transition)
            else:
                subtract = True
                for transition in hensel[current_num]:
                    trans += rotate_4_reflect(hensel[current_num][transition])

    return set(trans)

rule_string = g.getstring("Enter a rulestring. Must be outer-totalistic or isotropic non-totalistic.", g.getrule().split(":")[0])
rule_table = """@RULE EmulatedLLS

# State 0,1 -> 0,1
# State 2 -> *
# State 3-8,9-16 -> S(1-6)_x_y,*
# State 0,1 -> 0',1'
# State 2 -> *'
# State 3-8,9-16 -> S(1-6)_x_y',*'

@COLORS
0   48  48  48
1  255 255 255
2  128 128 128
3  255  48  48
4   48 255  48
5   48  48 255
6  255 255  48
7   48 255 255
8  255  48 255
9   64  64  64
10 128  24  24
11  24 128  24
12  24  24 128
13 128 128  24
14  24 128 128
15 128  24 128
16  48  48  48
17 255 255 255
18 128 128 128
19 255  48  48
20  48 255  48
21  48  48 255
22 255 255  48
23  48 255 255
24 255  48 255
25  64  64  64
26 128  24  24
27  24 128  24
28  24  24 128
29 128 128  24
30  24 128 128
31 128  24 128

@ICONS
XPM
"15 480 2 2"
".. c #000000"
"AA c #FFFFFF"

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

"AAAA......................AAAA"
"AAAAAA..................AAAAAA"
"..AAAAAA..............AAAAAA.."
"....AAAAAA..........AAAAAA...."
"......AAAAAA......AAAAAA......"
"........AAAAAA..AAAAAA........"
"..........AAAAAAAAAA.........."
"............AAAAAA............"
"..........AAAAAAAAAA.........."
"........AAAAAA..AAAAAA........"
"......AAAAAA......AAAAAA......"
"....AAAAAA..........AAAAAA...."
"..AAAAAA..............AAAAAA.."
"AAAAAA..................AAAAAA"
"AAAA......................AAAA"

"AAAA......................AAAA"
"AAAAAA..................AAAAAA"
"..AAAAAA..............AAAAAA.."
"....AAAAAA..........AAAAAA...."
"......AAAAAA......AAAAAA......"
"........AAAAAA..AAAAAA........"
"..........AAAAAAAAAA.........."
"............AAAAAA............"
"..........AAAAAAAAAA.........."
"........AAAAAA..AAAAAA........"
"......AAAAAA......AAAAAA......"
"....AAAAAA..........AAAAAA...."
"..AAAAAA..............AAAAAA.."
"AAAAAA..................AAAAAA"
"AAAA......................AAAA"

"AAAA......................AAAA"
"AAAAAA..................AAAAAA"
"..AAAAAA..............AAAAAA.."
"....AAAAAA..........AAAAAA...."
"......AAAAAA......AAAAAA......"
"........AAAAAA..AAAAAA........"
"..........AAAAAAAAAA.........."
"............AAAAAA............"
"..........AAAAAAAAAA.........."
"........AAAAAA..AAAAAA........"
"......AAAAAA......AAAAAA......"
"....AAAAAA..........AAAAAA...."
"..AAAAAA..............AAAAAA.."
"AAAAAA..................AAAAAA"
"AAAA......................AAAA"

"AAAA......................AAAA"
"AAAAAA..................AAAAAA"
"..AAAAAA..............AAAAAA.."
"....AAAAAA..........AAAAAA...."
"......AAAAAA......AAAAAA......"
"........AAAAAA..AAAAAA........"
"..........AAAAAAAAAA.........."
"............AAAAAA............"
"..........AAAAAAAAAA.........."
"........AAAAAA..AAAAAA........"
"......AAAAAA......AAAAAA......"
"....AAAAAA..........AAAAAA...."
"..AAAAAA..............AAAAAA.."
"AAAAAA..................AAAAAA"
"AAAA......................AAAA"

"AAAA......................AAAA"
"AAAAAA..................AAAAAA"
"..AAAAAA..............AAAAAA.."
"....AAAAAA..........AAAAAA...."
"......AAAAAA......AAAAAA......"
"........AAAAAA..AAAAAA........"
"..........AAAAAAAAAA.........."
"............AAAAAA............"
"..........AAAAAAAAAA.........."
"........AAAAAA..AAAAAA........"
"......AAAAAA......AAAAAA......"
"....AAAAAA..........AAAAAA...."
"..AAAAAA..............AAAAAA.."
"AAAAAA..................AAAAAA"
"AAAA......................AAAA"

"AAAA......................AAAA"
"AAAAAA..................AAAAAA"
"..AAAAAA..............AAAAAA.."
"....AAAAAA..........AAAAAA...."
"......AAAAAA......AAAAAA......"
"........AAAAAA..AAAAAA........"
"..........AAAAAAAAAA.........."
"............AAAAAA............"
"..........AAAAAAAAAA.........."
"........AAAAAA..AAAAAA........"
"......AAAAAA......AAAAAA......"
"....AAAAAA..........AAAAAA...."
"..AAAAAA..............AAAAAA.."
"AAAAAA..................AAAAAA"
"AAAA......................AAAA"

"AAAA......................AAAA"
"AAAAAA..................AAAAAA"
"..AAAAAA..............AAAAAA.."
"....AAAAAA..........AAAAAA...."
"......AAAAAA......AAAAAA......"
"........AAAAAA..AAAAAA........"
"..........AAAAAAAAAA.........."
"............AAAAAA............"
"..........AAAAAAAAAA.........."
"........AAAAAA..AAAAAA........"
"......AAAAAA......AAAAAA......"
"....AAAAAA..........AAAAAA...."
"..AAAAAA..............AAAAAA.."
"AAAAAA..................AAAAAA"
"AAAA......................AAAA"

"AAAA......................AAAA"
"AAAAAA..................AAAAAA"
"..AAAAAA..............AAAAAA.."
"....AAAAAA..........AAAAAA...."
"......AAAAAA......AAAAAA......"
"........AAAAAA..AAAAAA........"
"..........AAAAAAAAAA.........."
"............AAAAAA............"
"..........AAAAAAAAAA.........."
"........AAAAAA..AAAAAA........"
"......AAAAAA......AAAAAA......"
"....AAAAAA..........AAAAAA...."
"..AAAAAA..............AAAAAA.."
"AAAAAA..................AAAAAA"
"AAAA......................AAAA"

"AAAA......................AAAA"
"AAAAAA..................AAAAAA"
"..AAAAAA..............AAAAAA.."
"....AAAAAA..........AAAAAA...."
"......AAAAAA......AAAAAA......"
"........AAAAAA..AAAAAA........"
"..........AAAAAAAAAA.........."
"............AAAAAA............"
"..........AAAAAAAAAA.........."
"........AAAAAA..AAAAAA........"
"......AAAAAA......AAAAAA......"
"....AAAAAA..........AAAAAA...."
"..AAAAAA..............AAAAAA.."
"AAAAAA..................AAAAAA"
"AAAA......................AAAA"

"AAAA......................AAAA"
"AAAAAA..................AAAAAA"
"..AAAAAA..............AAAAAA.."
"....AAAAAA..........AAAAAA...."
"......AAAAAA......AAAAAA......"
"........AAAAAA..AAAAAA........"
"..........AAAAAAAAAA.........."
"............AAAAAA............"
"..........AAAAAAAAAA.........."
"........AAAAAA..AAAAAA........"
"......AAAAAA......AAAAAA......"
"....AAAAAA..........AAAAAA...."
"..AAAAAA..............AAAAAA.."
"AAAAAA..................AAAAAA"
"AAAA......................AAAA"

"AAAA......................AAAA"
"AAAAAA..................AAAAAA"
"..AAAAAA..............AAAAAA.."
"....AAAAAA..........AAAAAA...."
"......AAAAAA......AAAAAA......"
"........AAAAAA..AAAAAA........"
"..........AAAAAAAAAA.........."
"............AAAAAA............"
"..........AAAAAAAAAA.........."
"........AAAAAA..AAAAAA........"
"......AAAAAA......AAAAAA......"
"....AAAAAA..........AAAAAA...."
"..AAAAAA..............AAAAAA.."
"AAAAAA..................AAAAAA"
"AAAA......................AAAA"

"AAAA......................AAAA"
"AAAAAA..................AAAAAA"
"..AAAAAA..............AAAAAA.."
"....AAAAAA..........AAAAAA...."
"......AAAAAA......AAAAAA......"
"........AAAAAA..AAAAAA........"
"..........AAAAAAAAAA.........."
"............AAAAAA............"
"..........AAAAAAAAAA.........."
"........AAAAAA..AAAAAA........"
"......AAAAAA......AAAAAA......"
"....AAAAAA..........AAAAAA...."
"..AAAAAA..............AAAAAA.."
"AAAAAA..................AAAAAA"
"AAAA......................AAAA"

"AAAA......................AAAA"
"AAAAAA..................AAAAAA"
"..AAAAAA..............AAAAAA.."
"....AAAAAA..........AAAAAA...."
"......AAAAAA......AAAAAA......"
"........AAAAAA..AAAAAA........"
"..........AAAAAAAAAA.........."
"............AAAAAA............"
"..........AAAAAAAAAA.........."
"........AAAAAA..AAAAAA........"
"......AAAAAA......AAAAAA......"
"....AAAAAA..........AAAAAA...."
"..AAAAAA..............AAAAAA.."
"AAAAAA..................AAAAAA"
"AAAA......................AAAA"

"AAAA......................AAAA"
"AAAAAA..................AAAAAA"
"..AAAAAA..............AAAAAA.."
"....AAAAAA..........AAAAAA...."
"......AAAAAA......AAAAAA......"
"........AAAAAA..AAAAAA........"
"..........AAAAAAAAAA.........."
"............AAAAAA............"
"..........AAAAAAAAAA.........."
"........AAAAAA..AAAAAA........"
"......AAAAAA......AAAAAA......"
"....AAAAAA..........AAAAAA...."
"..AAAAAA..............AAAAAA.."
"AAAAAA..................AAAAAA"
"AAAA......................AAAA"

"AAAA......................AAAA"
"AAAAAA..................AAAAAA"
"..AAAAAA..............AAAAAA.."
"....AAAAAA..........AAAAAA...."
"......AAAAAA......AAAAAA......"
"........AAAAAA..AAAAAA........"
"..........AAAAAAAAAA.........."
"............AAAAAA............"
"..........AAAAAAAAAA.........."
"........AAAAAA..AAAAAA........"
"......AAAAAA......AAAAAA......"
"....AAAAAA..........AAAAAA...."
"..AAAAAA..............AAAAAA.."
"AAAAAA..................AAAAAA"
"AAAA......................AAAA"

"AAAA......................AAAA"
"AAAAAA..................AAAAAA"
"..AAAAAA..............AAAAAA.."
"....AAAAAA..........AAAAAA...."
"......AAAAAA......AAAAAA......"
"........AAAAAA..AAAAAA........"
"..........AAAAAAAAAA.........."
"............AAAAAA............"
"..........AAAAAAAAAA.........."
"........AAAAAA..AAAAAA........"
"......AAAAAA......AAAAAA......"
"....AAAAAA..........AAAAAA...."
"..AAAAAA..............AAAAAA.."
"AAAAAA..................AAAAAA"
"AAAA......................AAAA"

@TABLE
n_states:32
neighborhood:Moore
symmetries:none

var S0a={0,2,3,4,5,6,7,8,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var S0b=S0a
var S0c=S0a
var S0d=S0a
var S0e=S0a
var S0f=S0a
var S0g=S0a
var S0h=S0a

var S1a={1,9,10,11,12,13,14,15}
var S1b=S1a
var S1c=S1a
var S1d=S1a
var S1e=S1a
var S1f=S1a
var S1g=S1a
var S1h=S1a

var S2a={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var S2b=S2a
var S2c=S2a
var S2d=S2a
var S2e=S2a
var S2f=S2a
var S2g=S2a
var S2h=S2a

"""

for transition in get_trans_moore(rule_string.lower().split("/")[0].replace("b", "")):
    new_transition = transition[1:] + transition[0:1]
    rule_table += "0, " + ", ".join([("S1" if x else "S0") + "abcdefgh"[i] for i, x in enumerate(new_transition)]) + ", 1\n"
    rule_table += "2, " + ", ".join([("S1" if x else "S0") + "abcdefgh"[i] for i, x in enumerate(new_transition)]) + ", 9\n"
    rule_table += "3, " + ", ".join([("S1" if x else "S0") + "abcdefgh"[i] for i, x in enumerate(new_transition)]) + ", 10\n"
    rule_table += "4, " + ", ".join([("S1" if x else "S0") + "abcdefgh"[i] for i, x in enumerate(new_transition)]) + ", 11\n"
    rule_table += "5, " + ", ".join([("S1" if x else "S0") + "abcdefgh"[i] for i, x in enumerate(new_transition)]) + ", 12\n"
    rule_table += "6, " + ", ".join([("S1" if x else "S0") + "abcdefgh"[i] for i, x in enumerate(new_transition)]) + ", 13\n"
    rule_table += "7, " + ", ".join([("S1" if x else "S0") + "abcdefgh"[i] for i, x in enumerate(new_transition)]) + ", 14\n"
    rule_table += "8, " + ", ".join([("S1" if x else "S0") + "abcdefgh"[i] for i, x in enumerate(new_transition)]) + ", 15\n"

for transition in get_trans_moore(rule_string.lower().split("/")[1].replace("s", "")):
    new_transition = transition[1:] + transition[0:1]
    rule_table += "1, " + ", ".join([("S1" if x else "S0") + "abcdefgh"[i] for i, x in enumerate(new_transition)]) + ", 1\n"
    rule_table += "9, " + ", ".join([("S1" if x else "S0") + "abcdefgh"[i] for i, x in enumerate(new_transition)]) + ", 9\n"
    rule_table += "10, " + ", ".join([("S1" if x else "S0") + "abcdefgh"[i] for i, x in enumerate(new_transition)]) + ", 10\n"
    rule_table += "11, " + ", ".join([("S1" if x else "S0") + "abcdefgh"[i] for i, x in enumerate(new_transition)]) + ", 11\n"
    rule_table += "12, " + ", ".join([("S1" if x else "S0") + "abcdefgh"[i] for i, x in enumerate(new_transition)]) + ", 12\n"
    rule_table += "13, " + ", ".join([("S1" if x else "S0") + "abcdefgh"[i] for i, x in enumerate(new_transition)]) + ", 13\n"
    rule_table += "14, " + ", ".join([("S1" if x else "S0") + "abcdefgh"[i] for i, x in enumerate(new_transition)]) + ", 14\n"
    rule_table += "15, " + ", ".join([("S1" if x else "S0") + "abcdefgh"[i] for i, x in enumerate(new_transition)]) + ", 15\n"
    
rule_table += "1, " + ", ".join([("S2") + "abcdefgh"[i] for i in range(8)]) +  ", 0\n" 
rule_table += "9, " + ", ".join([("S2") + "abcdefgh"[i] for i in range(8)]) +  ", 2\n" 
rule_table += "10, " + ", ".join([("S2") + "abcdefgh"[i] for i in range(8)]) + ", 3\n"
rule_table += "11, " + ", ".join([("S2") + "abcdefgh"[i] for i in range(8)]) + ", 4\n"
rule_table += "12, " + ", ".join([("S2") + "abcdefgh"[i] for i in range(8)]) + ", 5\n"
rule_table += "13, " + ", ".join([("S2") + "abcdefgh"[i] for i in range(8)]) + ", 6\n"
rule_table += "14, " + ", ".join([("S2") + "abcdefgh"[i] for i in range(8)]) + ", 7\n"
rule_table += "15, " + ", ".join([("S2") + "abcdefgh"[i] for i in range(8)]) + ", 8\n"

with open(g.getdir("rules") + "EmulatedLLS.rule", "w") as file:
    file.write(rule_table)
g.setclipstr(rule_table)
g.setrule("EmulatedLLS")
