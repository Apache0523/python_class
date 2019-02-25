#! /user/bin/python3
# -*-coding:UTF-8-*-


class Dream(object):
    name = 'dream'

    def __init__(self,age):
        self.age = age

    def f(self):
        return "hahha:"+self.name+" "+self.age


testOne = Dream("22")
print(testOne.name)
print(testOne.f())
