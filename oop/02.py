class A():
    pass

def say(self):
    print("111")

A.say = say
a = A()
a.say()

