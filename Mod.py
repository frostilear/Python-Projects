x=int(input("Range pls"))
given_list=range(0,x)
temp=[]
i=0
while i<x: 
    if given_list[i]%3 == 0 or given_list[i]%5 == 0:
        temp.append(i)
    i+=1 
print(temp)    



