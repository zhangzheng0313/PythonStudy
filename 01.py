'''
定义一个学生类
'''
class Student():
    #一个空类
    pass

#定义一个对象
zhaangzheng = Student()

class PythonStudent():
    name = None
    age = 18
    course = "Python"

    def doHomework(self):
        print("I do homework")
        return None

#实例化
chenyi = PythonStudent()
print(chenyi.name)
print(chenyi.age)
chenyi.doHomework()