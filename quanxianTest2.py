#! /user/bin/python3
# -*-coding:UTF-8-*-


class TestTwo(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def show(self):
        return self.name+"%s" % self.age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self,name):
        self.__name = name

    def set_age(self,age):
        if 0<age<100:
            self.__age = age
        else:
            print("请重新输入年龄")


test = TestTwo("小鸿", 30)
print(test.get_age())
print(test.get_name())
test.set_age(110)
test.set_name("小张")
print(test.get_name())
print(test.get_age())
