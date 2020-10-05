from time import sleep

def main():
    age = 25
    name = "VASU"
    layer = 5
    border = 23
    symbol = "#"
    sleep(0.2)
    printBorder(border,symbol)
    sleep(0.3)
    print("\nHappy BirthDay ",name)
    sleep(0.3)
    printBorder(border,symbol)
    print("")
    sleep(0.2)
    printCandle(age)
    cakeTop(age)
    cakeBottum(age,layer)
    print("")
    sleep(0.2)
    printBorder(border, symbol)
    sleep(0.3)
    print("\nHappy BirthDay ", name)
    sleep(0.3)
    printBorder(border, symbol)
    print("")

def cakeTop(age):
    for i in range(age+2):
        print("=",end="")
        sleep(0.2)
    print("")

def cakeBottum(age,layer):
    for i in range(layer):
        for j in range(age+2):
            print("@",end="")
            sleep(0.2)
        print("")

def printBorder(border,symbol):
    for i in range(border):
        print(symbol,end="")
        sleep(0.2)

def printCandle(age):
    print(" ")
    for i in range(age):
        print(",",end="")
        sleep(0.2)

    print(" ")
    for j in range(age):
        print("|",end="")
        sleep(0.2)
    print("")



print("\n")
print("\n")
main()
print("\n")
print("\n")
