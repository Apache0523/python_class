#! /user/bin/python3
# -*-coding:UTF-8-*-


class TestQX(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return self.name, "%s" % self.age


testThree = TestQX("小王", 22)
print(testThree.show())
testThree.name = '小李'
testThree.age = '25'
print(testThree.show())
