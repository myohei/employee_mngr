# -*- coding: utf-8 -*-
from EmployeeManager import EmployeeManager

__author__ = 'yohei'


def showMenu():
    print("""
<MENU>
======================================
1. 登録
2. 紹介
3. 削除
4. 更新（←時間なかったら実装しなくてもいい）
======================================
    """)
    return True


def main():
    empMng = EmployeeManager()
    while True:
        showMenu()
        print(">>")
        i = input()
        if i == '1':
            empMng.createEmployee()
            pass
        elif i == '2':
            print("show")
            empMng.showEmployee()
            pass
        elif i == '3':
            empMng.deleteEmployee()
            print("delete")
            pass
        elif i == '4':
            print("update")
            pass
        else:
            print("不正な入力です")


if __name__ == '__main__':
    main()
