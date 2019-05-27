'''
定义一个学生类
'''
class Student():
    # 一个空类
    pass


# 定义一个对象
zhangzheng = Student()


class PythonStudent():
    name = None
    age = 18
    course = "Python"

    def doHomework(self):
        print("I do homework")
        return None


# 实例化
chenyi = PythonStudent()
print(chenyi.name)
print(chenyi.age)
chenyi.doHomework()

print(PythonStudent.__dict__)
print(chenyi.name)


# 继承
class Person():
    name = "Noname"
    age = 0
    def sleep(self):
        print("Sleeping...")

# 父类写在括号内
class Teacher(Person):
    def make_test(self):
        pass


t = Teacher()
print(t.name)
print(Teacher.name)
