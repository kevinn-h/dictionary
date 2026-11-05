W = [2, 3, 4, 4, 5, 6, 1, 2, 2, 2, 1, 8, 2]

def emeralds(N,W):
    sum = 0
    highest = 0
    for i in range(N):
        if W[i] % 2 == 0:
            sum+=W[i]
            if highest < sum:
                highest = sum
        elif W[i] % 2 == 1:
            sum = 0

    return highest

print(emeralds(13, W))
