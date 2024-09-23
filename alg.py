a = input("number 1: ")
b = input("numeber 2: ")
d = None
while d!=0:
    c = int(a)//int(b)
    d = int(a)%int(b)
    a = b
    b = d
    #print(a, b) 
    if d == 0:
        p = a
print(p)
