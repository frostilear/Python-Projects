import random
import time
with open("Thoughts.txt","r") as file:
    filelist=str(file.read()).split(";")
    while True:
        print(filelist[random.randrange(0,16)])
        time.sleep(random.randrange(2,4))