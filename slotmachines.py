""" def slot_machines(q,slot1,slot2,slot3):
    
    Amount = 0
    
    while True:
        if q == 0:
            print("Martha played {Amount} before going broke." )
            break
        if slot1% 35!=0:
            q -= 1
            Amount += 1
        elif slot1% 35==0:
            q+=29
            Amount += 1
        if slot2% 60!=0:
            q -= 1
            Amount += 1
        elif slot2% 60==0:
            q+=59
            Amount += 1
        if slot3%10!=0:
            q -= 1
            Amount += 1
        elif slot3% 10==0:
            q+=8
            Amount += 1
      
slot_machines(77,4,9,3)

 """

print("hi")