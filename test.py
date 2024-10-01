temps = 0

def ajt(n):

    global temps

    for _ in range(n):
        temps += 1

ajt(10)

print(temps)