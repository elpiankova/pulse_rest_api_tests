
class Person:
    # property = ["Earth", "rfsdgd"]
    def __init__(self, name="", surname="", age=None):
        if type(name) is not str:
            raise TypeError
        self.name = name
        self.age = age
        self.surname = surname

    def what_is_self(self):
        print(self)

    def full_name(self):
        return f"{self.name} {self.surname}"

    def get_older(self, years=1):
        if self.age is None:
            self.age = years
        self.age = self.age + years

    def __str__(self):
        return f"Person object with name={self.name} surname={self.surname} age={self.age}"


class Employee(Person):
    def __init__(self, name="", surname="", age=None, position="", salary=None):
        super().__init__(name, surname, age)
        self.position = position
        self.salary = salary

    def income(self, N):
        """ Return income for N months """
        if self.salary is None:
            return 0
        return self.salary * N

    def __str__(self):
        return super().__str__().replace("Person", "Employee")


class InfopulseEmployee(Employee):
    def __init__(self, *args, skills, **kwargs):
        super().__init__(*args, **kwargs)
        self.skills = skills



if __name__ == "__main__":
    p = Person("Bob", "Petrov")
    # p.get_older()
    # print(p.age)
    # print(p)

    e = Employee("Bob", "Black", position="QA", salary=2000)
    print(e.salary)
    print(e.full_name())
    print(e)
    # p2 = Person()
    # print(p2.name)
    # print(p2.age)
    # p2.what_is_self()
    # print(p2)



    # print(dir(l))
    # l = list()
    # l.sort()

