class EmployeeRecord:
    
    record = []

    def __init__(self):
        self.record.append(HREmployee('Adam', 'Małysz'))
        self.record.append(ITEmployee('Kamil', 'Stoch', 'Zniszczenie Świata'))
        self.record.append(Manager('Apoloniusz', 'Tajner'))

        


    
    def present(self):
        for employee in self.record:
            print(employee)

    def add_employees_to_manager(self):
        for employee in self.record:
            if type(employee) is Manager:
                employee.managed = [employee for employee in self.record if type(employee) is not Manager]
    
    

        


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

class Manager(Employee):

    position = 'Manager'

    managed = []

    def __init__(self, name, surname):
        Employee.__init__(self, name, surname)

    def __str__(self):
        return super().__str__() + f', Position: {self.position}, Manager of {self.managed}'





e = EmployeeRecord()
e.add_employees_to_manager()
e.present()





