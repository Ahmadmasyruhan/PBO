class Employee:
  empCount = 0
  
  def __init__(self,name,salary):
    self.nama = name
    self.salary = salary
    Employee.empCount +=1
    
    def displayCount(self):
      print("Total Employee %d" % Employee.empcount)
      
    def displayEmployee(self):
      print("Name :",self.nama, ",Salary:",self.salary)
    
emp1 = Employee("Masyruhan" , 10000)
emp2 = Employee("M.irwan" ,7000)
emp1.displayEmployee()
emp2.displayEmployee()
print("total employee %d" % Employee.empCount)
