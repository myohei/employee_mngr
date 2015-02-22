# -*- coding: utf-8 -*-
from datetime import datetime

from Employee import Employee


__author__ = 'yohei'


class EmployeeManager:
    def __init__(self):
        self.employesList = []


    def createEmployee(self):
        name = self._inputName()
        birthday = self._inputBirthday()
        salary = self._inputSalary()
        newEmployee = Employee(name, birthday, salary)
        self.employesList.append(newEmployee)
        self.showEmployee()

    def showEmployee(self):
        print("""
*******************************************************************
ID      名前               生年月日               給与
*******************************************************************
        """)
        for emp in self.employesList:
            emp.showInformation()
        return True

    def deleteEmployee(self):
        print("ID>>")
        idStr = input()
        try:
            id = int(idStr)
        except ValueError:
            print("不正な入力です")
            return
        for emp in self.employesList:
            if id == emp.id:
                self.employesList.remove(emp)
                break
        self.showEmployee()

    def _inputName(self):
        while True:
            print("名前>>")
            name = input()
            if name == None or name == "":
                continue
            return name

    def _inputBirthday(self):
        while True:
            print("・生年月日(2000/12/23, 20001223で入力)>>")
            birthday = input()
            # str2date
            try:
                dt = datetime.strptime(birthday, "%Y/%m/%d")
                dt.isoformat()
            except ValueError:
                print("不正な値です。")
                continue
            date = dt.date()
            date.isoformat()
            print(date)
            return date

    def _inputSalary(self):
        while True:
            print("給与>>")
            salarStr = input()
            try:
                salary = int(salarStr)
            except ValueError:
                print("不正な値です。")
                continue
            if salary > 0:
                return salary