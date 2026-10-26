def slot_machines(q,slot1,slot2,slot3):

    while True:
        Amount = 0
        if q == 0:
            print("Martha played", str(Amount),"before going broke." )
            break
    if slot1% 35!=0:
        q -= 1
        slot1 += 1
        Amount += 1
    elif slot1% 35==0:
        q+=29
        slot1 += 1
        Amount += 1
    if slot2% 60!=0:
        q -= 1
        slot2 +=1
        Amount += 1
    elif slot2% 60==0:
        q+=59
        slot2 += 1
        Amount += 1
    if slot3%10!=0:
        q -= 1
        slot3 += 1
        Amount += 1
    elif slot3% 10==0:
        q+=8
        slot3 += 1
        Amount += 1
              
   
int(slot_machines(0,4,9,3))