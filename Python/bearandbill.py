ques = []
while True:
    try: 
        line = input()
    except EOFError:
        break
    ques.append(line)

res = []

for i in ques:
    I = 0
    R = 0
    V = 0
    if('I=' in i):
        indexOfI = int(i.index('I=')+2)
        while(i[indexOfI] != 'A'):
            I = I * 10 + int(i[indexOfI])
            indexOfI += 1
    if('R=' in i):
        indexOfR = int(i.index('R=')+2)
        while(i[indexOfR] != 'O'):
            R = R * 10 + int(i[indexOfR])
            indexOfR += 1
    if('V=' in i):
        indexOfV = int(i.index('V=')+2)
        while(i[indexOfV] != 'V'):
            V = V * 10 + int(i[indexOfV])
            indexOfV += 1
    if not I:
        res.append("I={0:.2f}A".format(V / R))
    elif not V:
        res.append("V={0:.2f}V".format(I * R))
    else:
        res.append("R={0:.2f}O".format(V / I))

print(*res, sep="\n")