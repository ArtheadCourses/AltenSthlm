
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + "." + last.lower() + "@company.com"
        self.pay = pay

    def get_full_name(self):
        return self.first + " " + self.last

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return self.get_full_name() + " has a sallery of " + str(self.pay)

    def __add__(self, other):
        return Employee(self.first, other.last, self.pay + other.pay)


def main():
    emp1 = Employee("Sue", "Smith", 50000)
    emp2 = Employee("John", "Jones", 45000)
    emp3 = Employee("Jack", "Nelson", 30000)
    emp4 = Employee("Anna", "Miller", 55000)
    print(emp1)
    print(emp2)

    result = emp1 + emp2 + emp3 + emp4
    print(result)


if __name__ == '__main__':
    main()