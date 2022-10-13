import modul3
import math
print("""
       Calculator
       
       Process
       
       1. TOplama 
       2. Cixma
       3. Bolme
       4. Vurma
       5. Ebob tapma 
       6. Ekob tapma 
       7. 2 Ededin toplamanin faktorilaini tapma (Fakt(a+b))
       
       'q' Proqramdan cixis

""")
while True:
    processes = input("ENter the proccess")
    if (processes == "q"):
        print("KalkUlatordan cix")
        break
    elif (processes == "1"):
        a = int(input("\na: "))
        b = int(input("\nb: "))
        one= modul3.toplama(a,b)
        print(one)

    elif (processes == "2"):
        a = int(input("\na: "))
        b = int(input("\nb: "))
        two= modul3.cixma(a,b)
        print(two)
    elif (processes == "3"):
        a = int(input("\na: "))
        b = int(input("\nb: "))
        three= modul3.bolme(a,b)
        print(three)
    elif (processes == "4"):
        a = int(input("\na: "))
        b = int(input("\nb: "))
        four= modul3.vurma(a,b)
        print(four)
    elif (processes == "5"):
        a = int(input("\na: "))
        b = int(input("\nb: "))
        five= modul3.ebob(a,b)
        print(five)
    elif (processes == "6"):
        a = int(input("\na: "))
        b = int(input("\nb: "))
        six= modul3.ekob(a,b)
        print(six)
    elif (processes == "7"):
        a = int(input("\na: "))
        b = int(input("\nb: "))
        n = a + b
        one = modul3.toplama(a,b)
        print(one)
        seven = modul3.factorial(n)
        print(seven)
    else:
        print("Bele bir proses yoxdur")

