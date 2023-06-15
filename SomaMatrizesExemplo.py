m = []
n = []
r = []
for i in range(2):
    linhaM = []
    linhaN = []
    linhaR = []
    for j in range(2):
        linhaM.append(int(input("M%i%i: " % (i, j))))
        linhaN.append(int(input("N%i%i: " % (i, j))))
        linhaR.append(linhaM[j] + linhaN[j])
    m.append(linhaM)
    m.append(linhaN)
    r.append(linhaR)

#Impressão da matriz:
for i in range(len(r)):
    for j in range(len(r[i])):
        print(r[i][j], end="\t")
    print()