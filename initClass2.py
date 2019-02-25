#! /usr/bin/python3
# -*-coding:UTF-8-*-


class InitClass(object):
    name = "xiaomming"

    def __init__(self):
        print("调用了构造方法")

    def test(self):
        return "年龄是："+self.name


testTwo = InitClass()
print(testTwo.name)
print(testTwo.test())
