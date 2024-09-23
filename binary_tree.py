import time
Input=[4,5,7,1,5,6,1,3,6,9]
root=Input[0]
Arranged=[]
prev_value=root
for value in Input:
    if value < prev_value:
        Arranged.append("{} is on the left of {}".format(value,prev_value))
        prev_value=value
    elif value > prev_value:
        Arranged.append("{} is on the right of {}".format(value,prev_value))
        prev_value=value
    elif value == prev_value:
        Arranged.append("{} is an exeption".format(value))
        prev_value=value
print(Arranged)