from random import randint
arr=[]
size=int(input("add num"))
for i in range(size):
    arr.append(randint(-10, 10))
print(arr)
arr.reverse()
print("res",arr)
