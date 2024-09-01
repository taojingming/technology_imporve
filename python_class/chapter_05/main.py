"""
类方法与静态方法
"""


class Student:
    school = "abn"
 #类方法   
    @classmethod
    def hello(cls):
        print(f"hello {cls.__name__}")
#静态方法
    @staticmethod# 用不到self 
    def out():
        print(f'hello {Student.school}')
        
    @staticmethod
    def size(value:int)-> float:
        return value*1.5
    
    def speak(self):
        n=12
        # n = Student.size(n)  
        n =self.size(n)
        print(n)  
         
    
        
def main():
    Student.hello()
    print(Student.school)
    Student.out()
    Student().speak()
    
if __name__ == '__main__':
        main()            