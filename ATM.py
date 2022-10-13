password = 4648
balance = 1000000
while True:
    try:
        input_password = int(input("Kodunuzu daxil edin "))
    except ValueError:
        print("Zehmet olmasa reqemlerden ibaret kod daxil edin")
        continue
    if (password == input_password):
        print("""
            1. Balans:
            2. Hesaba depozit
            3. Pul cekmek
            q proqramnan cixish
        
        """
        )
    break
while True:
    proccess = input("Prosesi daxil ediniz")

    if (proccess == "q"):
        print("Proqramnan cixilir")
        break
    elif (proccess == "1"):
        print("Balansiniz {} manatdir".format(balance))
    elif(proccess == "2"):
        miqdar = int(input("Elave elemek istediyiniz mebleg"))
        balance += miqdar
        print("Balansiniz {} manatdir ".format(balance))
    elif (proccess == "3"):
        miqdar = int(input("CEkmek istediyiniz miqdar"))
        if (balance - miqdar < 0):
            print("Kartda bu geder pul yoxdur ")
            continue
        balance -= miqdar
        print("Balansiniz {} manatdir ".format(balance))
    else:
        print("Doqru prossesi daxil ediniz")
