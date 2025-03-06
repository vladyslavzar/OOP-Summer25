class Person:
  def __init__(self, name, age, adress):
    self.name = name
    self.age = age
    self.adress = adress


class Student(Person):
    def __init__(self, name, age, adress, graduation_year):
        super().__init__( name, age, adress)
        self.graduation_year = graduation_year

    def introduce_yourself(self):
       print("My name is " + self.name + ", I am " + str(self.age) + " years old." + " I live on " + self.adress + " street.")

    def state_graduation_year(self):
       print("My year of graduation is " + str(self.graduation_year))

Vlad = Student("Vlad", 18, "Grojecka", 2028)

Vlad.introduce_yourself()
Vlad.state_graduation_year()