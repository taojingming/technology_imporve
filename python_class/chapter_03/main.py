class Student:
    
    def __init__(self,name):
        #初始化参数，调用时候需要传递参数
        self.name = name
         
    
    def say_hello(self,msg:str):#实例函数 self 我的
        print(f'Hello {msg},{self.name}')
        
def main():
    """
    实例函数内通过self 访问实例变量
    在类的外部访问实例变量与函数
    """
    s1 = Student('Jack')
    s2 = Student('Tom')
    s1.say_hello('hahhh')
    #增加对象新的属性
    s1.gender  = 'Male'
    print(s1.gender)
    
if __name__ == '__main__':
        main()            