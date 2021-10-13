class EmployeeRecord:
    
    record = []

    def __init__(self):
        self.record.append(HREmployee('Adam', 'Małysz'))
        self.record.append(ITEmployee('Kamik', 'Stoch', 'Zniszczenie Świata'))

    @classmethod
    def present(cls):
        for employee in cls.record:
            print(employee)


class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Name: {self.name}, Surname: {self.surname}'


    # @staticmethod
    # def present():
        

    

class HREmployee(Employee):

    position = 'HR guy'

    def __init__(self, name, surname):
        Employee.__init__(self, name, surname)

    def __str__(self):
        return super().__str__() + f', Position: {self.position}'

class ITEmployee(Employee):

    position = 'IT guy'

    def __init__(self, name, surname, project):
        Employee.__init__(self, name, surname) #why I cant put super() here?
        self.project = project

    def __str__(self):
        return super().__str__() + f', Position: {self.position}, Current Project: {self.project}'





e = EmployeeRecord()
e.present()





