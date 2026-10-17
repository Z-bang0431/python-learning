# names = []

# for i in range(3):
#     name = input("what's your name?")
    # names.append(name)
# print(f"hello,{names}")
# for name in sorted(names):
    # print(f"hello,{name}")
# name = input("what's your name?")
# file = open("names.txt","a")
# file.write(f'{name}\n')
# file.close()

with open("names.txt", "r") as file:     # 这个方法可以不用使用close函数关闭文件，他会自动打开并关闭
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())   # 删除print产生的空行