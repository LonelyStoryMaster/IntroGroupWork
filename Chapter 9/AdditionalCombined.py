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