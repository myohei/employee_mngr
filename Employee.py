# -*- coding: utf-8 -*-
__author__ = 'yohei'

id = 0  # あまり良くないけど、ここでID管理


class Employee(object):
    def __init__(self, name, birthday, salary):
        global id
        id += 1
        self.id = id
        self.name = name
        self.birthday = birthday
        self.salary = salary

    def showInformation(self):
        print(str(self.id) + "\t" + self.name + "\t" + self.birthday.strftime('%Y/%m/%d') + "\t" + str(self.salary))
        pass
