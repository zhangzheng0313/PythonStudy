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
    _petname = "ergou"
    __score = 0

    def sleep(self):
        print("Sleeping...")

    def work(self):
        print("make some money")


# 父类写在括号内
class Teacher(Person):
    teacher_id = "123"

    def make_test(self):
        print("111")

# 扩充父类功能
    def work(self):
        # 方法一
        # Person.work(self)
        # 方法二
        super().work()
        self.make_test()


t = Teacher()
print(t.name)
print(t._petname)
t.sleep()
print(t.teacher_id)
t.make_test()
t.work()


class A():
    def __init__(self):
        print("A")


class B(A):
    def __init__(self, name):
        print("B")
        print(name)


class C(B):
    def __init__(self, name):
        B.__init__(self, name)
        print("lalala")


c = C(111)


class A():
    def __init__(self, name=0):
        print("lalalala")

    def __str__(self):
        return "111"


a = A()
print(a)
