1、介绍
FastAPI 是一个高性能的，
基于python 3.8+ 的WEB框架快速，高效，简单，标准化
![alt text](image/image.png)
web 界面可查看：
http://127.0.0.1:8000/docs
![alt text](image/web.png)
注意: ctrl+s 重新登陆

2、路径参数
设置特定类型
设置枚举类型

3、查询参数
查询参数存在URI
可选查询参数 Optional[int] = 10

4、请求体
get不可以适应个体请求发送请求体
发送请求体类型可以是 POST PUT DELETE PATCH
如果在路径参数中定义了参数，那么相同参数则选择路径参数
如果参数类型为int /str 基本类型，则为查询参数
如果是pydanict 模型类型，则为请求体

5、参数验证
path Query
... 表示是必须有，必须要输出，内容不管
alias 别名 为了适应语法问题，可以在传入参数中又称
#正则化约束参数

6、深入请求体









