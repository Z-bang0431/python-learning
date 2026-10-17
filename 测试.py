print('你好，张')
import random
i = random.randint(1,3)
print(i)
# print(input("请输入你的名字："))
u = 0
for i in range(0, 10):
    u += i
print(u)

a = 1
while a <= 9:
    b = 1
    while b <=a:
        print(f"{b}*{a}=",a*b, end="\t")
        b += 1
    print()
    a += 1

for i in range(1, 10):
    if i <= 9:
        for j in range(1, 10):
            if j <= i:
                print(f"{i}*{j}=", i*j, end="\t")
                j += 1
            else:
                break
        print()
        i += 1

for a in range(1, 10):
    for b in range(1, a + 1):
        print(f"{b}*{a}=", a * b, end="\t")
    print()