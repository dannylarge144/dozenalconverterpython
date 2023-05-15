import math
print("--- Welcome! This is a tool that converts decimal integers to dozenal ---")
while True:
    while True:
        try:
            intDec = int(input("Please enter an interger in decimal:"))
            boolbreak = True
        except ValueError:
            print("Something went wrong.")
            boolbreak = False
        if boolbreak:
            break    
    boolNeg = False
    if intDec < 0:
        boolNeg = True
        intDec = abs(intDec)
    while intDec > 12**9:
        print("Too large.")
        while True:
            try:
                intDec = int(input("Please enter an interger in decimal:"))
                boolbreak = True
            except ValueError:
                print("Something went wrong.")
                boolbreak = False
            if boolbreak:
                break
    strdoz = ""
    if boolNeg:
        strdoz += "-"
    intpow = 9
    boolfsf = True
    while intpow > -1:
        intdigit = (math.floor(intDec/12**intpow))
        strdigit = str(intdigit)
        if (intdigit != 0) or (not boolfsf) or (intpow == 0):
            if intdigit == 10:
                strdigit = "X"
            if intdigit == 11:
                strdigit = "E"
            intDec -= intdigit*(12**intpow)
            strdoz += strdigit
            boolfsf = False
        intpow -= 1
    print("In dozenal that is " + strdoz +".")
    strbreak = input("Would you like to quit? (y/n)")
    if strbreak == "y":
        break
print("--- Goodbye! ---")
    
    

