
c = True
for j in range(10):
    for i in range(10):
        if i==5:
            c = False
            print(5)
        print("afterBreak")
    if c == False:
        print(j,i)
        break

print("Fin 10")