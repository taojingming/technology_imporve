from pprint import pprint
class Student:
    student_count= 0
    
    
class Person:
    pass

def main():
    print(Student.__name__)#类变量，类本身的属性，所有该类的对象都共享类变量
    print(Student.student_count)
    print(getattr(Student,"student_count") )
    print(getattr(Student,"student_count","error"))#找不到类变量值，就返回error
    
    Student.student_count = 89
    setattr(Student,"student_count",100)
    print(Student.student_count)
    
    Student.newattribute = 'hello'
    print(Student.newattribute)

    # del Student.newsttribute
    delattr(Student,"newattribute") 
    # print(Student.newattribute)
    
    #类变量的存储全部都在类变量 __dict__ 字典中,不等直接修改其内容
    s1 = Student()
    s2 = Student()
    Student.student_count = 4
    print(s1.student_count)
    print(s2.student_count)
    
    pprint(Student.__dict__)
    
    
    
    
if __name__ == '__main__':
        main()