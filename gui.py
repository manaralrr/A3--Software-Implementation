import tkinter as tk
from tkinter import messagebox
import pickle

class EventManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management System")
        
        # Load data from binary files
        self.load_data()
        
        self.initialize_components()
        
    def initialize_components(self):
        # Labels
        tk.Label(self.root, text="Employee ID:").grid(row=0, column=0)
        tk.Label(self.root, text="Name:").grid(row=0, column=2)
        tk.Label(self.root, text="Department:").grid(row=0, column=4)
        tk.Label(self.root, text="Job Title:").grid(row=0, column=6)
        
        tk.Label(self.root, text="Event ID:").grid(row=1, column=0)
        tk.Label(self.root, text="Type:").grid(row=1, column=2)
        tk.Label(self.root, text="Theme:").grid(row=1, column=4)
        tk.Label(self.root, text="Date:").grid(row=1, column=6)
        
        tk.Label(self.root, text="Client ID:").grid(row=2, column=0)
        tk.Label(self.root, text="Name:").grid(row=2, column=2)
        tk.Label(self.root, text="Address:").grid(row=2, column=4)
        tk.Label(self.root, text="Contact Details:").grid(row=2, column=6)
        
        tk.Label(self.root, text="Guest ID:").grid(row=3, column=0)
        tk.Label(self.root, text="Name:").grid(row=3, column=2)
        tk.Label(self.root, text="Address:").grid(row=3, column=4)
        tk.Label(self.root, text="Contact Details:").grid(row=3, column=6)
        
        tk.Label(self.root, text="Supplier ID:").grid(row=4, column=0)
        tk.Label(self.root, text="Name:").grid(row=4, column=2)
        tk.Label(self.root, text="Address:").grid(row=4, column=4)
        tk.Label(self.root, text="Contact Details:").grid(row=4, column=6)
        
        # Entry fields
        self.emp_id_entry = tk.Entry(self.root)
        self.emp_id_entry.grid(row=0, column=1)
        self.emp_name_entry = tk.Entry(self.root)
        self.emp_name_entry.grid(row=0, column=3)
        self.emp_dept_entry = tk.Entry(self.root)
        self.emp_dept_entry.grid(row=0, column=5)
        self.emp_job_entry = tk.Entry(self.root)
        self.emp_job_entry.grid(row=0, column=7)
        
        self.event_id_entry = tk.Entry(self.root)
        self.event_id_entry.grid(row=1, column=1)
        self.event_type_entry = tk.Entry(self.root)
        self.event_type_entry.grid(row=1, column=3)
        self.event_theme_entry = tk.Entry(self.root)
        self.event_theme_entry.grid(row=1, column=5)
        self.event_date_entry = tk.Entry(self.root)
        self.event_date_entry.grid(row=1, column=7)
        
        self.client_id_entry = tk.Entry(self.root)
        self.client_id_entry.grid(row=2, column=1)
        self.client_name_entry = tk.Entry(self.root)
        self.client_name_entry.grid(row=2, column=3)
        self.client_address_entry = tk.Entry(self.root)
        self.client_address_entry.grid(row=2, column=5)
        self.client_contact_entry = tk.Entry(self.root)
        self.client_contact_entry.grid(row=2, column=7)
        
        self.guest_id_entry = tk.Entry(self.root)
        self.guest_id_entry.grid(row=3, column=1)
        self.guest_name_entry = tk.Entry(self.root)
        self.guest_name_entry.grid(row=3, column=3)
        self.guest_address_entry = tk.Entry(self.root)
        self.guest_address_entry.grid(row=3, column=5)
        self.guest_contact_entry = tk.Entry(self.root)
        self.guest_contact_entry.grid(row=3, column=7)
        
        self.supplier_id_entry = tk.Entry(self.root)
        self.supplier_id_entry.grid(row=4, column=1)
        self.supplier_name_entry = tk.Entry(self.root)
        self.supplier_name_entry.grid(row=4, column=3)
        self.supplier_address_entry = tk.Entry(self.root)
        self.supplier_address_entry.grid(row=4, column=5)
        self.supplier_contact_entry = tk.Entry(self.root)
        self.supplier_contact_entry.grid(row=4, column=7)
        
        # Buttons
        tk.Button(self.root, text="Add Employee", command=self.add_employee).grid(row=0, column=8)
        tk.Button(self.root, text="Delete Employee", command=self.delete_employee).grid(row=0, column=9)
        tk.Button(self.root, text="Modify Employee", command=self.modify_employee).grid(row=0, column=10)
        tk.Button(self.root, text="Display Employee Details", command=self.display_employee_details).grid(row=0, column=11)
        
        tk.Button(self.root, text="Add Event", command=self.add_event).grid(row=1, column=8)
        tk.Button(self.root, text="Delete Event", command=self.delete_event).grid(row=1, column=9)
        tk.Button(self.root, text="Modify Event", command=self.modify_event).grid(row=1, column=10)
        tk.Button(self.root, text="Display Event Details", command=self.display_event_details).grid(row=1, column=11)
        
        tk.Button(self.root, text="Add Client", command=self.add_client).grid(row=2, column=8)
        tk.Button(self.root, text="Delete Client", command=self.delete_client).grid(row=2, column=9)
        tk.Button(self.root, text="Modify Client", command=self.modify_client).grid(row=2, column=10)
        tk.Button(self.root, text="Display Client Details", command=self.display_client_details).grid(row=2, column=11)
        
        tk.Button(self.root, text="Add Guest", command=self.add_guest).grid(row=3, column=8)
        tk.Button(self.root, text="Delete Guest", command=self.delete_guest).grid(row=3, column=9)
        tk.Button(self.root, text="Modify Guest", command=self.modify_guest).grid(row=3, column=10)
        tk.Button(self.root, text="Display Guest Details", command=self.display_guest_details).grid(row=3, column=11)
        
        tk.Button(self.root, text="Add Supplier", command=self.add_supplier).grid(row=4, column=8)
        tk.Button(self.root, text="Delete Supplier", command=self.delete_supplier).grid(row=4, column=9)
        tk.Button(self.root, text="Modify Supplier", command=self.modify_supplier).grid(row=4, column=10)
        tk.Button(self.root, text="Display Supplier Details", command=self.display_supplier_details).grid(row=4, column=11)
        
    def load_data(self):
        # Load employees
        try:
            with open('employees.dat', 'rb') as file:
                self.employees = pickle.load(file)
        except FileNotFoundError:
            self.employees = {}
            
        # Load events
        try:
            with open('events.dat', 'rb') as file:
                self.events = pickle.load(file)
        except FileNotFoundError:
            self.events = {}
            
        # Load clients
        try:
            with open('clients.dat', 'rb') as file:
                self.clients = pickle.load(file)
        except FileNotFoundError:
            self.clients = {}
            
        # Load guests
        try:
            with open('guests.dat', 'rb') as file:
                self.guests = pickle.load(file)
        except FileNotFoundError:
            self.guests = {}
            
        # Load suppliers
        try:
            with open('suppliers.dat', 'rb') as file:
                self.suppliers = pickle.load(file)
        except FileNotFoundError:
            self.suppliers = {}
        
    def save_data(self):
        # Save employees
        with open('employees.dat', 'wb') as file:
            pickle.dump(self.employees, file)
            
        # Save events
        with open('events.dat', 'wb') as file:
            pickle.dump(self.events, file)
            
        # Save clients
        with open('clients.dat', 'wb') as file:
            pickle.dump(self.clients, file)
            
        # Save guests
        with open('guests.dat', 'wb') as file:
            pickle.dump(self.guests, file)
            
        # Save suppliers
        with open('suppliers.dat', 'wb') as file:
            pickle.dump(self.suppliers, file)
        
    def add_employee(self):
        emp_id = int(self.emp_id_entry.get())
        emp_name = self.emp_name_entry.get()
        emp_dept = self.emp_dept_entry.get()
        emp_job = self.emp_job_entry.get()
        self.employees[emp_id] = {'id': emp_id, 'name': emp_name, 'department': emp_dept, 'job_title': emp_job}
        self.save_data()
        messagebox.showinfo("Success", "Employee added successfully.")
        
    def delete_employee(self):
        try:
            emp_id = int(self.emp_id_entry.get())
            if emp_id in self.employees:
                del self.employees[emp_id]
                self.save_data()
                messagebox.showinfo("Success", "Employee deleted successfully.")
            else:
                messagebox.showerror("Error", "Employee not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Employee ID.")
    
    def display_employee_details(self):
        try:
            emp_id = int(self.emp_id_entry.get())
            if emp_id in self.employees:
                employee_details = self.employees[emp_id]
                messagebox.showinfo("Employee Details", f"ID: {employee_details['id']}\nName: {employee_details['name']}\nDepartment: {employee_details['department']}\nJob Title: {employee_details['job_title']}")
            else:
                messagebox.showerror("Error", "Employee not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Employee ID.")

    def add_event(self):
        try:
            event_id = int(self.event_id_entry.get())
            event_type = self.event_type_entry.get()
            event_theme = self.event_theme_entry.get()
            event_date = self.event_date_entry.get()
            self.events[event_id] = {'id': event_id, 'type': event_type, 'theme': event_theme, 'date': event_date}
            self.save_data()
            messagebox.showinfo("Success", "Event added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Event ID.")
    
    def delete_event(self):
        try:
            event_id = int(self.event_id_entry.get())
            if event_id in self.events:
                del self.events[event_id]
                self.save_data()
                messagebox.showinfo("Success", "Event deleted successfully.")
            else:
                messagebox.showerror("Error", "Event not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Event ID.")
    
    def modify_event(self):
        try:
            event_id = int(self.event_id_entry.get())
            if event_id in self.events:
                event_type = self.event_type_entry.get()
                event_theme = self.event_theme_entry.get()
                event_date = self.event_date_entry.get()
                self.events[event_id]['type'] = event_type
                self.events[event_id]['theme'] = event_theme
                self.events[event_id]['date'] = event_date
                self.save_data()
                messagebox.showinfo("Success", "Event modified successfully.")
            else:
                messagebox.showerror("Error", "Event not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Event ID.")
    
    def display_event_details(self):
        try:
            event_id = int(self.event_id_entry.get())
            if event_id in self.events:
                event_details = self.events[event_id]
                messagebox.showinfo("Event Details", f"ID: {event_details['id']}\nType: {event_details['type']}\nTheme: {event_details['theme']}\nDate: {event_details['date']}")
            else:
                messagebox.showerror("Error", "Event not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Event ID.")

    def add_client(self):
        try:
            client_id = int(self.client_id_entry.get())
            client_name = self.client_name_entry.get()
            client_address = self.client_address_entry.get()
            client_contact = self.client_contact_entry.get()
            self.clients[client_id] = {'id': client_id, 'name': client_name, 'address': client_address, 'contact': client_contact}
            self.save_data()
            messagebox.showinfo("Success", "Client added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Client ID.")

    def delete_client(self):
        try:
            client_id = int(self.client_id_entry.get())
            if client_id in self.clients:
                del self.clients[client_id]
                self.save_data()
                messagebox.showinfo("Success", "Client deleted successfully.")
            else:
                messagebox.showerror("Error", "Client not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Client ID.")

    def modify_client(self):
        try:
            client_id = int(self.client_id_entry.get())
            if client_id in self.clients:
                client_name = self.client_name_entry.get()
                client_address = self.client_address_entry.get()
                client_contact = self.client_contact_entry.get()
                self.clients[client_id]['name'] = client_name
                self.clients[client_id]['address'] = client_address
                self.clients[client_id]['contact'] = client_contact
                self.save_data()
                messagebox.showinfo("Success", "Client modified successfully.")
            else:
                messagebox.showerror("Error", "Client not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Client ID.")

    def display_client_details(self):
        try:
            client_id = int(self.client_id_entry.get())
            if client_id in self.clients:
                client_details = self.clients[client_id]
                messagebox.showinfo("Client Details", f"ID: {client_details['id']}\nName: {client_details['name']}\nAddress: {client_details['address']}\nContact: {client_details['contact']}")
            else:
                messagebox.showerror("Error", "Client not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Client ID.")

    def add_guest(self):
        try:
            guest_id = int(self.guest_id_entry.get())
            guest_name = self.guest_name_entry.get()
            guest_address = self.guest_address_entry.get()
            guest_contact = self.guest_contact_entry.get()
            self.guests[guest_id] = {'id': guest_id, 'name': guest_name, 'address': guest_address, 'contact': guest_contact}
            self.save_data()
            messagebox.showinfo("Success", "Guest added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Guest ID.")
    
    def delete_guest(self):
        try:
            guest_id = int(self.guest_id_entry.get())
            if guest_id in self.guests:
                del self.guests[guest_id]
                self.save_data()
                messagebox.showinfo("Success", "Guest deleted successfully.")
            else:
                messagebox.showerror("Error", "Guest not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Guest ID.")

    def modify_guest(self):
        try:
            guest_id = int(self.guest_id_entry.get())
            if guest_id in self.guests:
                guest_name = self.guest_name_entry.get()
                guest_address = self.guest_address_entry.get()
                guest_contact = self.guest_contact_entry.get()
                self.guests[guest_id]['name'] = guest_name
                self.guests[guest_id]['address'] = guest_address
                self.guests[guest_id]['contact'] = guest_contact
                self.save_data()
                messagebox.showinfo("Success", "Guest modified successfully.")
            else:
                messagebox.showerror("Error", "Guest not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Guest ID.")

    def display_guest_details(self):
        try:
            guest_id = int(self.guest_id_entry.get())
            if guest_id in self.guests:
                guest_details = self.guests[guest_id]
                messagebox.showinfo("Guest Details", f"ID: {guest_details['id']}\nName: {guest_details['name']}\nAddress: {guest_details['address']}\nContact: {guest_details['contact']}")
            else:
                messagebox.showerror("Error", "Guest not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Guest ID.")
    
    def add_supplier(self):
        try:
            supplier_id = int(self.supplier_id_entry.get())
            supplier_name = self.supplier_name_entry.get()
            supplier_address = self.supplier_address_entry.get()
            supplier_contact = self.supplier_contact_entry.get()
            self.suppliers[supplier_id] = {'id': supplier_id, 'name': supplier_name, 'address': supplier_address, 'contact': supplier_contact}
            self.save_data()
            messagebox.showinfo("Success", "Supplier added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Supplier ID.")

    def delete_supplier(self):
        try:
            supplier_id = int(self.supplier_id_entry.get())
            if supplier_id in self.suppliers:
                del self.suppliers[supplier_id]
                self.save_data()
                messagebox.showinfo("Success", "Supplier deleted successfully.")
            else:
                messagebox.showerror("Error", "Supplier not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Supplier ID.")

    def modify_supplier(self):
        try:
            supplier_id = int(self.supplier_id_entry.get())
            if supplier_id in self.suppliers:
                supplier_name = self.supplier_name_entry.get()
                supplier_address = self.supplier_address_entry.get()
                supplier_contact = self.supplier_contact_entry.get()
                self.suppliers[supplier_id]['name'] = supplier_name
                self.suppliers[supplier_id]['address'] = supplier_address
                self.suppliers[supplier_id]['contact'] = supplier_contact
                self.save_data()
                messagebox.showinfo("Success", "Supplier modified successfully.")
            else:
                messagebox.showerror("Error", "Supplier not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Supplier ID.")
    
    def modify_employee(self):
        try:
            employee_id = int(self.employee_id_entry.get())
            if employee_id in self.employees:
                employee_name = self.employee_name_entry.get()
                employee_department = self.employee_department_entry.get()
                employee_job_title = self.employee_job_title_entry.get()
                employee_basic_salary = float(self.employee_basic_salary_entry.get())
                employee_age = int(self.employee_age_entry.get())
                employee_date_of_birth = self.employee_date_of_birth_entry.get()
                employee_passport_details = self.employee_passport_details_entry.get()

                self.employees[employee_id]['name'] = employee_name
                self.employees[employee_id]['department'] = employee_department
                self.employees[employee_id]['job_title'] = employee_job_title
                self.employees[employee_id]['basic_salary'] = employee_basic_salary
                self.employees[employee_id]['age'] = employee_age
                self.employees[employee_id]['date_of_birth'] = employee_date_of_birth
                self.employees[employee_id]['passport_details'] = employee_passport_details

                self.save_data()
                messagebox.showinfo("Success", "Employee modified successfully.")
            else:
                messagebox.showerror("Error", "Employee not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Employee ID.")
        
    def display_supplier_details(self):
        try:
            supplier_id = int(self.supplier_id_entry.get())
            if supplier_id in self.suppliers:
                supplier_details = self.suppliers[supplier_id]
                messagebox.showinfo("Supplier Details", f"ID: {supplier_details['id']}\nName: {supplier_details['name']}\nAddress: {supplier_details['address']}\nContact: {supplier_details['contact']}")
            else:
                messagebox.showerror("Error", "Supplier not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Supplier ID.")




    def __del__(self):
        # Save data before closing the application
        self.save_data()

if __name__ == "__main__":
    root = tk.Tk()
    app = EventManagementGUI(root)
    root.mainloop()
