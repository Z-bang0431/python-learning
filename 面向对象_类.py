"""面向对象
  语法：
    1、先定义类
                class 类名：  (这里类名首字母要大写)
                pass
    2、创建对象
                对象名 = 类名（）
                对象名.属性名1 = 属性值1
                对象名.属性名2 = 属性值2
例子：
class Car:
    pass

c1 = Car()
c1.brand = 'BWM'
c1.name = 'X5'
c1.price = 500000
print(c1.__dict__)   __dict__是python中用户自定义类实例的一个特殊属性,用于以字典形式存储对象的属性
                     使用c1.__dict__能将对象的所有属性以字典的形式打印输出


                     ——————正确使用方法——————
    1、先定义类
                class 类名：  (这里类名首字母要大写)
                    def __init__(self, 参数列表)
                    self.属性名 = 参数值
                    self.属性名 = 参数值
    2、创建对象
                对象名 = 类名（参数列表）

例子：
class Car:
    def __init__(self, c_brand, c_name, c_price)
    self.brand = c_brand
    self.name = c_name
    self.price = c_price

c1 = Car("BWM", "X5", "50000")
print(c1.__dict__)    
"""

class Car:
    def __init__(self, c_color, c_brand, c_name,  c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price

c1 = Car("红色", "BWM", "X7", 800000)
print(c1.__dict__)

c2 = Car("黑色", "奔驰", "E300", 500000)
print(c2.__dict__)

# class Student:  
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house


# def main():
#     student = get_student()
#     print(f"{student.name} form {student.house}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)

# if __name__ == "__main__":
#     main() 



class Car1:
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand =  c_brand
        self.name = c_name
        self.price = c_price

    def running(self):
        print(f"{self.brand}{self.name}正在高速行驶中····")

    def total_cost(self, discount, rate):
        total_cost = self.price * discount + self.price * rate
        return total_cost

c3 = Car1("红色", "BWM", "X7", 800000)
c3.running()
total = c3.total_cost(0.9, 0.1)
print("提车的总费用为：", total)