import random
result=0
for item in range(1000000):
    item=random.randrange(0,2)
    if item==1:
        result+=1
result_percentage=result/1000000*100
print("The percentage of heads is: ")
print(result_percentage)
print("the percentage of tails is: ")
print(100-result_percentage)