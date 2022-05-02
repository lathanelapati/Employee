emp_list = [['rita','singh',25,30],['tim','cruse',24,35]]
class Employee ():
  def __init__(self,employee=[]):
    self.fname = employee[0]
    self.lname = employee[1]
    self.hrate = employee[2]
    self.hrs_worked = employee[3]

  def calc_wages(self):
    wages = self.hrate * self.hrs_worked
    name = self.fname+""+self.lname
    print(name,wages)

for employees in emp_list:
  emp = Employee(employee)
  emp.calc_wages()
  