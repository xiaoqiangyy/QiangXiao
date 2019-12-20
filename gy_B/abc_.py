#!/usr/bin/env python
# -*- coding:utf-8 -*-



class Man():
    name = '雷阳洪'
    age = 18
    sex = '男'
    def xiedaima(self):
        print(self.name,"写代码")

    def sleep(self):
        print(self.name,"在睡觉")
    def ziwjieshao(self):
        print(self.name,'说：我今年%s'%self.age)

man = Man()
man.xiedaima()


import random