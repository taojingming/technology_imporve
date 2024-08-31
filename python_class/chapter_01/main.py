class Student:
    pass
class Person:
    pass

def main():
    print(Student)
    print(type(Student))# 类本身也是对象，是type的对象
    #创建对象 实例
    student_1 = Student()
    print(Student)#两个不同的对象，存储的地址是不一样的
    student_1 = Student()
    print(hex(id(student_1)))#ID 函数取数对象的唯一识别符 hex转换成16进制
    print(isinstance(student_1,Person))#判断对象是否是这个类
    
if __name__ == '__main__':
        main()