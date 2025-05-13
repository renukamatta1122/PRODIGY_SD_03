employee contact: 
        
        employee = Employee( name, emailid, contact)
        self.employees[id] = employee
        print("Employee added successfully!")

    def view_employees(self):
        if not self.employees:
            print("No employees in the system.")
            return
        
        for id, employee in self.employees.items():
            print(f"Name: {employee.name}")
            print(f"emailid: {employee.emailid}")
            print(f"contact: {employee.contact}")
            print("------------------------")

    def update_employee(self):
        
        employee = self.employees[id]
        print("Enter new details (leave blank to keep current value):")
        
        name = input(f"Name ({employclass Employee:
    def _init_(self, name, emailid, contact):
        self.name = name
        self.emailid = emailid
        self.contact = contact

class ManagementSystem:
    def _init_(self):
        self.employees = {}
