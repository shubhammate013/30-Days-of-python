class Employee:  # Define a class named Employee.

    def __init__(self, first, last, pay):  # Define the initialization method with parameters first, last, and pay.
        self.first = first  # Assign the value of the first name to the instance variable 'first'.
        self.last = last  # Assign the value of the last name to the instance variable 'last'.
        self.email = first + '.' + last + '@email.com'  # Generate an email using first and last names and assign it to the instance variable 'email'.
        self.pay = pay  # Assign the value of pay to the instance variable 'pay'.

    def fullname(self):  # Define a method named fullname.
        return '{} {}'.format(self.first, self.last)  # Return the full name by formatting first and last names.

emp_1 = Employee('Corey', 'Schafer', 50000)  # Create an instance of Employee with the provided information.
emp_2 = Employee('Test', 'Employee', 60000)  # Create another instance of Employee with the provided information.
