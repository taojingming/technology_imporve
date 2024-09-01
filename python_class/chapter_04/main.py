

"""
私有属性与函数用途


"""


class Student:
    
    def __init__(self,name):
        #  _XXXX 保护性变量 __XXXX 完全私有变量或者函数  __XXX__ 系统自己带的
        self.__name = name
         
    
    def say_hello(self,msg:str):#实例函数 self 我的
        print(f'Hello {msg},{self.__name}')
        
def main():
    """
    实例函数内通过self 访问实例变量
    在类的外部访问实例变量与函数
    """
    s1 = Student('Jack')
    s1.say_hello('hahhh')
    print(s1._Student__name)# 类的外部访问格式 _classname__attribute
    
if __name__ == '__main__':
        main()            