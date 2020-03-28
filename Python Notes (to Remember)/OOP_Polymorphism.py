# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:54:58 2020

@author: alkan
"""


class Employee():
    
    def raisee(self):
        raise_rate = 0.1
        result =  100 + 100 * raise_rate
        print("Employee: ", result)        
        
class computerEngineer(Employee):
    
    def raisee(self):
        raise_rate = 0.2
        result =  100 + 100 * raise_rate
        print("Computer E: ", result)

class mechatronicsEngineer(Employee):
    def raisee(self):
        raise_rate = 0.3
        result =  100 + 100 * raise_rate
        print("Mechatronics E: ", result)

e1 = Employee()

ce = computerEngineer()

me = mechatronicsEngineer()

employee_list = [ce,me]

# for i in range(5):   # 0dan 5e kadar olan sayıları yazdırır
#     print(i)

for employee in employee_list:
    employee.raisee()