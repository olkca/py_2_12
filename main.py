import random

size=int(input("add num"))
begin = -10
end = 10
sms=[]
for i in range(size):
    sms.append(random.randint(begin, end))
random.shuffle(sms)
print(sms)

data={1:lambda lst: max(lst), 2: lambda lst:min(lst)}
print(data[1](sms))
print(data[2](sms))
