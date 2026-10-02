# class Student:
#      name="aman sharma"

# s1=Student()
# print(s1.name)   






# class Student:


# # Parameterized Constructor
#   def __init__(self,name,marks):
#     self.name=name
#     self.marks=marks
#     print("adding new student in database....")


# s1=Student("aman",100)
# print(s1.name,s1.marks)

# s2=Student("sharma",90)
# print(s2.name,s2.marks)





class Student:


# Parameterized Constructor
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks 
  def Welcome(self):
    print("welcome Student,", self.name)

  def get_marks(self):
      return self.marks


s1=Student("Aman",99)

s1.Welcome()
print(s1.get_marks())



del s1;

print(s1.get_marks())



