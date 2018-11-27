firstName = " "
lastName = " "
myIncome = 0
taxRate = 0.00
taxes = 0.00

firstName = input("Please enter your firstname: ")
lastName = input("Please type in your lastname: ")

def validate():
    val: str = input("Please type in your monthly income: ")
    global myIncome
    try:
        myIncome = int(val)
    except ValueError:
        print("Please only use numbers")
        validate()

def checkTax(value):
    global taxRate
    if value < 10000: taxRate = 0.4
    elif value > 10000 & value < 30000: taxRate = 0.55
    elif value > 30000 & value < 70000: taxRate = 0.75
    else: taxRate = 0.82

def calculateTax(a,b):
    global taxes
    taxes = a * b


validate()
checkTax(myIncome)
calculateTax(myIncome,taxRate)

print("Der Steuerzahler " + firstName + " " + lastName +
" muss für das laufende Jahr " + str(taxes) + " Dublonen dem Steueramt bezahlen.")




