# 1、介绍
FastAPI 是一个高性能的，
基于python 3.8+ 的WEB框架快速，高效，简单，标准化
![alt text](image/image.png)
web 界面可查看：
http://127.0.0.1:8000/docs
![alt text](image/web.png)
注意: ctrl+s 重新登陆

# 2、路径参数
设置特定类型
设置枚举类型

# 3、查询参数
查询参数存在URI
可选查询参数 Optional[int] = 10

# 4、请求体
get不可以适应个体请求发送请求体
发送请求体类型可以是 POST PUT DELETE PATCH
如果在路径参数中定义了参数，那么相同参数则选择路径参数
如果参数类型为int /str 基本类型，则为查询参数
如果是pydanict 模型类型，则为请求体

# 5、参数验证
path Query
... 表示是必须有，必须要输出，内容不管
alias 别名 为了适应语法问题，可以在传入参数中又称
#正则化约束参数

# 6、深入请求体
单一类型的请求体
请求体模型嵌套
模型内使用list,set等

# 7、实例数据
1、examples
2、model_config 优先级高于examples
3、body 可以写examples * 表示后面的参数必须关键字传递参数 如uername='fsdf'    

# 8、Cookie 与Header 参数
Swagger UI 中的cookie 参数当前无法发送，可以通过Postman 测试 ,或者通过程序中的set cookie测试
Cookie header 参数名字不要使用下划线 ，如果用，使用alias 做别名处理

# 9、响应模型
返回的参数需要符合约束条件
response_model_exclude = {"id"} 除了这几个都要
response_model_include={"id","useranme"} 只要这几个参数
response_model_exclude_unset=True 没有设置的参数不要  

# 10、状态码和异常处理
返回指定的状态码
自定义异常状态码





