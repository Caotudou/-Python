# -*-conding:utf-8-*-
'''由于Python是动态语言，根据类创建的实例可以任意绑定属性。

给实例绑定属性的方法是通过实例变量，或者通过self变量：'''
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
