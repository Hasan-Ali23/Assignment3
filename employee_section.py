from tkinter import messagebox
import pickle

class Employee:
    def __init__(self, name=None, employee_id=None, department=None, job_title=None, basic_salary=None, age=None, date_of_birth=None, passport_details=None, manager_id=None):
        """Initialize Employee object with specified attributes."""
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details
        self.manager_id = manager_id
        self.employees = []  # List to hold employee data

    def add_employee(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, manager_id=None):
        """Add a new employee to the list and pickle the data."""
        employee_data = {
            "name": name,
            "employee_id": employee_id,
            "department": department,
            "job_title": job_title,
            "basic_salary": basic_salary,
            "age": age,
            "date_of_birth": date_of_birth,
            "passport_details": passport_details,
            "manager_id": manager_id
        }
        self.employees.append(employee_data)  # Add employee data to the list

        with open("employees.pickle", "wb") as file:
            pickle.dump(self.employees, file)  # Pickle the updated employee list

    def delete_employee(self, employee_id):
        """Delete an employee based on the employee_id."""
        try:
            with open("employees.pickle", "rb") as file:
                employees = pickle.load(file)  # Load existing employees from file
        except FileNotFoundError:
            messagebox.showerror("Error", "No employees found!")
            return

        for employee in employees:
            if employee["employee_id"] == employee_id:
                employees.remove(employee)  # Remove the specified employee
                break
        else:
            messagebox.showerror("Error", "Employee not found!")
            return

        with open("employees.pickle", "wb") as file:
            pickle.dump(employees, file)  # Save updated employee list

        messagebox.showinfo("Success", "Employee deleted successfully!")

    def modify_employee(self, employee_id, modified_employee_details):
        """Modify employee details identified by employee_id."""
        try:
            with open("employees.pickle", "rb") as file:
                employees = pickle.load(file)  # Load existing employees from file
        except FileNotFoundError:
            messagebox.showerror("Error", "No employees found!")
            return

        for employee in employees:
            if employee["employee_id"] == employee_id:
                employee.update(modified_employee_details)  # Update employee details
                break
        else:
            messagebox.showerror("Error", "Employee not found!")
            return

        with open("employees.pickle", "wb") as file:
            pickle.dump(employees, file)  # Save updated employee list

        messagebox.showinfo("Success", "Employee details modified successfully!")

    @staticmethod
    def display_employee_by_id(employee_id):
        """Retrieve employee details by employee_id."""
        try:
            with open("employees.pickle", "rb") as file:
                employees = pickle.load(file)  # Load existing employees from file

            for employee in employees:
                if employee["employee_id"] == employee_id:
                    return employee  # Return employee details if found

            return None
        except FileNotFoundError:
            messagebox.showerror("Error", "No employees found!")
            return None
