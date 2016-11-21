
class Employee:
    raise_amnt = 1.04
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

    def give_raise(self):
        self.pay *= self.raise_amnt


class Developer(Employee):
    raise_amnt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    raise_amnt = 1.02

def main():
    emp1 = Manager("Sue", "Smith", 50000)
    emp2 = Developer("John", "Jones", 45000, "Python")
    print(emp1)
    emp1.give_raise()
    print(emp1)



if __name__ == '__main__':
    main()