class Person:
 
  def __init__(self,name,age,gender):
    self.name = name
    self.age = age
    self.gender = gender
 
  def person_details(self):
    print(f'Person Name: {self.name} \nPerson Age: {self.age} \nPerson Gender: {self.gender}\n')

p1 = Person("Check", "26", "M")

p1.person_details()
