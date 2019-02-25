#! /usr/bin/python3
# -*-coding:UTF-8-*-
class Test(object):
    name = "小明"
    def f(self):
        return "调了"

testOne = Test()
print(testOne.name)
print(testOne.f())

