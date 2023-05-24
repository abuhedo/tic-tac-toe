bored = [["-"], ["-"], ["-"],
         ["-"], ["-"], ["-"],
         ["-"], ["-"], ["-"]]
bored_num = [["1"], ["2"], ["3"],
             ["4"], ["5"], ["6"],
             ["7"], ["8"], ["9"]]
def bored_filled():
    for empty in bored:
        if "-" in  empty:
            return False
    return True
def win_game():
    if (bored[0][0] == "x" and bored[1][0] == "x" and bored[2][0] == "x") or (bored[0][0] == "o" and bored[1][0] == "o" and bored[2][0] == "o"):
        return True
    if (bored[0][0] == "x" and bored[4][0] == "x" and bored[8][0] == "x") or (bored[0][0] == "o" and bored[4][0] == "o" and bored[8][0] == "o"):
        return True
    if (bored[2][0] == "x" and bored[5][0] == "x" and bored[8][0] == "x") or (bored[2][0] == "o" and bored[5][0] == "o" and bored[8][0] == "o"):
        return True
    if (bored[2][0] == "x" and bored[4][0] == "x" and bored[6][0] == "x") or (bored[2][0] == "o" and bored[4][0] == "o" and bored[6][0] == "o"):
        return True
    if (bored[3][0] == "x" and bored[4][0] == "x" and bored[5][0] == "x") or (bored[3][0] == "o" and bored[4][0] == "o" and bored[5][0] == "o"):
        return True
    if (bored[6][0] == "x" and bored[7][0] == "x" and bored[8][0] == "x") or (bored[6][0] == "o" and bored[7][0] == "o" and bored[8][0] == "o"):
        return True
    if (bored[1][0] == "x" and bored[4][0] == "x" and bored[7][0] == "x") or (bored[1][0] == "o" and bored[4][0] == "o" and bored[7][0] == "o"):
        return True
    if (bored[0][0] == "x" and bored[3][0] == "x" and bored[6][0] == "x") or (bored[0][0] == "o" and bored[3][0] == "o" and bored[6][0] == "o"):
        return True
    return False
    
for i in range(len(bored_num)):
    print(bored_num[i], end="")
    if (i + 1)%3 == 0:
        print("")
plyer2 = ""
plyer1 = ""
print("Hello to a tic tac toe game from ahmad alhadeed")
print("press the number to place your {}".format(plyer1))

plyer1 = str(input("plyer one chose \'x\' or \'o\' :"))
if plyer1 == "x":
    plyer2 = "o"
else:
    plyer2 = "x"

print("plyer one chose \"{}\", and plyer two chose \"{}\"".format(plyer1, plyer2))

for i in range(len(bored_num)):
        print(bored_num[i], end="")
        if (i + 1)%3 == 0:
            print("")
while True:
    print("press the number to place your {}".format(plyer1))
    index = int(input())
    bored[index-1] = plyer1
    for i in range(len(bored)):
        if "-" not in bored[i]:
            print("[" + str(bored[i]) + "]" , end="-")
            if (i + 1)%3 == 0:
                print("")
        else:
            print(bored[i], end="-")
            if (i + 1)%3 == 0:
                print("")
    if win_game():
        print("plyer one win !!!!")
        break
    print("press the number to place your {}".format(plyer2))
    index = int(input())
    bored[index-1] = plyer2
    for i in range(len(bored)):
        if "-" not in bored[i]:
            print("[" + str(bored[i]) + "]" , end="-")
            if (i + 1)%3 == 0:
                print("")
        else:
            print(bored[i], end="-")
            if (i + 1)%3 == 0:
                print("")
    if win_game():
        print("plyer two win !!!!")
        break
    


