Given_List=[1,2,5,7,9,9,0,-1,-2,-2,-4,-6,-7,-9]
i=len(Given_List)-1
temp=0
while Given_List[i] < 0:
    temp+=Given_List[i]
    i-=1 
print(temp)    