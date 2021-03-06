class CellPhone:
    def __init__(self, manufact='none', model='none', retail_price=0.00):
        self.manufact = manufact
        self.model = model
        self.retail_price = retail_price

    def set_manufact(self):
        self.manufact = input('Enter a new manufacturer:\n')

    def set_model(self):
        self.model = input('Enter a new model number:\n')

    def set_retail_price(self):
        self.retail_price = input('Enter a new retail price:\n')

    def get_manufact(self):
        print('The current manufacturer is', self.manufact)

    def get_model(self):
        print('The current model is', self.model)

    def get_retail_price(self):
        print('The current retail price is', self.retail_price)

def menu():        
    print('MENU:')
    print('a - Change name of manufacturer')
    print('b - Change model number')
    print('c - Change retail price')
    print('d - Get manufacturer name')
    print('e - Get model number')
    print('f - Get retail price')

class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id_number

    def get_department(self):
        return self.department

    def get_job_title(self):
        return self.job_title

# For the Employee Class

if __name__ == '__main__':
    employee1 = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
    employee2 = Employee('Mark Jones', 39119, 'IT', 'Programmer')
    employee3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

    employees = [employee1, employee2, employee3]

    print("Name           |ID Number      |Department     |Job Title      ")
    print("---------------------------------------------------------------")
    for employee in employees:
        print("%-15s|%-15d|%-15s|%-20s" % (employee.name, employee.id_number, employee.department, employee.job_title))

if __name__ == "__main__":
    print('Cell Phone Info:')
    print()

    manufact = input('Enter the manufacturer:\n')
    model = input('Enter the model number:\n')
    price = float(input('Enter the retail price:\n'))

    cellphone = CellPhone(manufact, model, price)
    
    print('Here is the date you entered:')
    print('Manufacturer: %s' % manufact)
    print('Model Number: %s' % model)
    print('Retail Price: %0.2f' % price)

    menu()
    ans = input('Enter the menu option you want or q to quit\n')
    
    while ans != 'q':
        if ans == 'a':
            cellphone.set_manufact()
            ans = input('Enter the menu option you want or q to quit\n')
        elif ans == 'b':
            cellphone.set_model()
            ans = input('Enter the menu option you want or q to quit\n')
        elif ans == 'c':
            cellphone.set_retail_price()
            ans = input('Enter the menu option you want or q to quit\n')
        elif ans == 'd':
            cellphone.get_manufact()
            ans = input('Enter the menu option you want or q to quit\n')
        elif ans == 'e':
            cellphone.get_model()
            ans = input('Enter the menu option you want or q to quit\n')
        elif ans == 'f':
            cellphone.get_retail_price()
            ans = input('Enter the menu option you want or q to quit\n')
        else:
            print('ERROR: You entered an incorrect value.')
            ans = input('Enter the menu option you want or q to quit\n')

            