# Import tkinter library
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
# Import functions from other files
from employee_section import Employee
from event_section import Event
from client_section import Client
from guest_section import Guest
from supplier_section import Supplier
from venue_section import Venue
from check_credentials import authenticate, create_account


class MainMenu:
    # Defining the initialization method for the MainMenu class
    def __init__(self, master):
        self.master = master
        # Create Instances of imported classes
        self.employee = Employee()
        self.event = Event()
        self.client = Client()
        self.guest = Guest()
        self.supplier = Supplier()
        self.venue = Venue()
        self.master.title("Main Menu")
        self.master.geometry("400x500")
        self.master.configure(bg="Dark Green")

       # Load the background image
        bg_image = Image.open("DisplayPhoto.jpeg")

        # Resize the image to match the window size
        bg_image = bg_image.resize((400, 300))

        # Convert the image for Tkinter display
        self.background_image = ImageTk.PhotoImage(bg_image)

        # Create a label to hold the background image
        self.bg_label = tk.Label(master, image=self.background_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill the entire window with the image

        # Title label widget
        self.title_label = tk.Label(master, text="Data Warehouse", font=("Arial", 15, "bold"), bg="Green", fg="white")
        self.title_label.pack(pady=20)

        # Create sign-in button
        self.btn_signin = tk.Button(master, text="Sign In", width=20, command=self.open_signin_window)
        self.btn_signin.pack(pady=10)

        # Create sign-up button
        self.btn_signup = tk.Button(master, text="Sign Up", width=20, command=self.open_signup_window)
        self.btn_signup.pack(pady=10)

        # Initially disable menu buttons
        self.menu_buttons = []

    def open_signin_window(self):
        signin_window = tk.Toplevel(self.master)
        signin_window.title("Sign In")
        signin_window.geometry("300x200")
        signin_window.configure(bg="Dark Green")

        # Create entry widgets for username and password
        lbl_username = tk.Label(signin_window, text="Username:")
        lbl_username.pack(pady=10)
        entry_username = tk.Entry(signin_window)
        entry_username.pack(pady=5)

        lbl_password = tk.Label(signin_window, text="Password:")
        lbl_password.pack(pady=10)
        entry_password = tk.Entry(signin_window, show="*")
        entry_password.pack(pady=5)

        # Create sign-in button
        btn_signin = tk.Button(signin_window, text="Sign In", command=lambda: self.signin(entry_username.get(), entry_password.get()))
        btn_signin.pack(pady=10)

    def open_signup_window(self):
        signup_window = tk.Toplevel(self.master)
        signup_window.title("Sign Up")
        signup_window.geometry("300x200")
        signup_window.configure(bg="Dark Green")

        # Create entry widgets for username and password
        lbl_username = tk.Label(signup_window, text="Username:")
        lbl_username.pack(pady=10)
        entry_username = tk.Entry(signup_window)
        entry_username.pack(pady=5)

        lbl_password = tk.Label(signup_window, text="Password:")
        lbl_password.pack(pady=10)
        entry_password = tk.Entry(signup_window, show="*")
        entry_password.pack(pady=5)

        # Create sign-up button
        btn_signup = tk.Button(signup_window, text="Sign Up", command=lambda: self.signup(entry_username.get(), entry_password.get()))
        btn_signup.pack(pady=10)

    def signin(self, username, password):
        if authenticate(username, password):
            messagebox.showinfo("Success", "Sign in successful!")
            self.enable_menu_access()
        else:
            messagebox.showerror("Error", "Invalid credentials.")

    def signup(self, username, password):
        if create_account(username, password):
            messagebox.showinfo("Success", "Account created successfully!")
        else:
            messagebox.showerror("Error", "Username already exists.")

    def enable_menu_access(self):
        if not self.menu_buttons:
            # Create buttons for menu items
            self.btn_employees = tk.Button(self.master, text="EMPLOYEES", width=20,command=self.open_employee_submenu)
            self.btn_events = tk.Button(self.master, text="EVENTS", width=20,command=self.open_event_submenu)
            self.btn_clients = tk.Button(self.master, text="CLIENTS", width=20,command=self.open_client_submenu)
            self.btn_guests = tk.Button(self.master, text="GUESTS", width=20,command=self.open_guest_submenu)
            self.btn_suppliers = tk.Button(self.master, text="SUPPLIERS", width=20, command=self.open_supplier_submenu)
            self.btn_venues = tk.Button(self.master, text="VENUES", width=20, command=self.open_venue_submenu)

            # Place buttons on the screen
            self.btn_employees.pack(pady=10)
            self.btn_events.pack(pady=10)
            self.btn_clients.pack(pady=10)
            self.btn_guests.pack(pady=10)
            self.btn_suppliers.pack(pady=10)
            self.btn_venues.pack(pady=10)

            # Store menu buttons to enable/disable later
            self.menu_buttons = [
                self.btn_employees, self.btn_events, self.btn_clients,
                self.btn_guests, self.btn_suppliers, self.btn_venues
            ]

#*****************************Clients Section**************************************

    def open_client_submenu(self):
        # Create a new window for the client submenu
        client_submenu = tk.Toplevel(self.master)
        client_submenu.title("SubMenu_Client")
        client_submenu.geometry("400x300")
        client_submenu.configure(bg="Dark Green")


        # Create buttons for client submenu
        btn_add_client = tk.Button(client_submenu, text="ADD", width=20, command=self.open_add_client_window)
        btn_delete_client = tk.Button(client_submenu, text="DELETE", width=20, command= self.open_delete_client_window)
        btn_modify_client = tk.Button(client_submenu, text="MODIFY", width=20, command = self.open_modify_client_window)
        btn_display_client = tk.Button(client_submenu, text="DISPLAY", width=20, command=self.open_display_client_window)

        # Place buttons on the screen
        btn_add_client.pack(pady=10)
        btn_delete_client.pack(pady=10)
        btn_modify_client.pack(pady=10)
        btn_display_client.pack(pady=10)

    def open_modify_client_window(self):
        def fetch_client_details():
            client_id = entry_client_id.get()
            client = Client.display_client_by_id(client_id)

            if client:
                # entry fields with client details
                entry_new_name.delete(0, tk.END)
                entry_new_name.insert(0, client['name'])
                entry_new_address.delete(0, tk.END)
                entry_new_address.insert(0, client['address'])
                entry_new_contact_details.delete(0, tk.END)
                entry_new_contact_details.insert(0, client['contact_details'])
                entry_new_budget.delete(0, tk.END)
                entry_new_budget.insert(0, client['budget'])
            else:
                messagebox.showerror("Error", "Client not found!")

        def modify_client_details():
            modified_client_details = {
                "name": entry_new_name.get(),
                "address": entry_new_address.get(),
                "contact_details": entry_new_contact_details.get(),
                "budget": entry_new_budget.get()
            }
            client_id = entry_client_id.get()
            Client().modify_client(client_id, modified_client_details)

        modify_client_window = tk.Toplevel(self.master)
        modify_client_window.title("Modify_Client")
        modify_client_window.geometry("400x400")
        modify_client_window.configure(bg="Dark Green")

        lbl_client_id = tk.Label(modify_client_window, text="Client ID:", width=15)
        lbl_client_id.grid(row=0, column=0, pady=10, padx=10, sticky="e")
        entry_client_id = tk.Entry(modify_client_window, width=30)
        entry_client_id.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        lbl_new_name = tk.Label(modify_client_window, text="New Name:", width=15)
        lbl_new_name.grid(row=1, column=0, pady=10, padx=10, sticky="e")
        entry_new_name = tk.Entry(modify_client_window, width=30)
        entry_new_name.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        lbl_new_address = tk.Label(modify_client_window, text="New Address:", width=15)
        lbl_new_address.grid(row=2, column=0, pady=10, padx=10, sticky="e")
        entry_new_address = tk.Entry(modify_client_window, width=30)
        entry_new_address.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        lbl_new_contact_details = tk.Label(modify_client_window, text="New Contact Details:", width=15)
        lbl_new_contact_details.grid(row=3, column=0, pady=10, padx=10, sticky="e")
        entry_new_contact_details = tk.Entry(modify_client_window, width=30)
        entry_new_contact_details.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        lbl_new_budget = tk.Label(modify_client_window, text="New Budget:", width=15)
        lbl_new_budget.grid(row=4, column=0, pady=10, padx=10, sticky="e")
        entry_new_budget = tk.Entry(modify_client_window, width=30)
        entry_new_budget.grid(row=4, column=1, pady=10, padx=10, sticky="w")

        btn_fetch_details = tk.Button(modify_client_window, text="Fetch Details", width=20, command=fetch_client_details)
        btn_fetch_details.grid(row=5, column=0, columnspan=2, pady=20)

        btn_modify = tk.Button(modify_client_window, text="MODIFY", width=20, command=modify_client_details)
        btn_modify.grid(row=6, column=0, columnspan=2, pady=20)


    def open_add_client_window(self):
        # Create a new window for adding a client
        add_client_window = tk.Toplevel(self.master)
        add_client_window.title("Add_Client")
        add_client_window.geometry("340x250")
        add_client_window.configure(bg="Dark Green")

        # Client details input fields
        lbl_client_id = tk.Label(add_client_window, text="Client ID:", width=15)
        lbl_client_id.grid(row=0, column=0, pady=(20, 5), padx=10, sticky="e")
        entry_client_id = tk.Entry(add_client_window, width=30)
        entry_client_id.grid(row=0, column=1, pady=(20, 5), padx=10, sticky="w")

        lbl_name = tk.Label(add_client_window, text="Name:", width=15)
        lbl_name.grid(row=1, column=0, pady=5, padx=10, sticky="e")
        entry_name = tk.Entry(add_client_window, width=30)
        entry_name.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        lbl_address = tk.Label(add_client_window, text="Address:", width=15)
        lbl_address.grid(row=2, column=0, pady=5, padx=10, sticky="e")
        entry_address = tk.Entry(add_client_window, width=30)
        entry_address.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        lbl_contact_details = tk.Label(add_client_window, text="Contact Details:", width=15)
        lbl_contact_details.grid(row=3, column=0, pady=5, padx=10, sticky="e")
        entry_contact_details = tk.Entry(add_client_window, width=30)
        entry_contact_details.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        lbl_budget = tk.Label(add_client_window, text="Budget:", width=15)
        lbl_budget.grid(row=4, column=0, pady=5, padx=10, sticky="e")
        entry_budget = tk.Entry(add_client_window, width=30)
        entry_budget.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        # Submit button
        btn_submit = tk.Button(add_client_window, text="Submit", width=20, command=lambda: self.submit_client(
            entry_client_id.get(), entry_name.get(), entry_address.get(),
            entry_contact_details.get(), entry_budget.get()
        ))
        btn_submit.grid(row=5, column=0, columnspan=2, pady=20)

    def submit_client(self, client_id, name, address, contact_details, budget):
        # Create a Client object with provided details
        new_client = Client(client_id, name, address, contact_details, budget)
        
        # Add client details
        new_client.add_client()
        
        # Show a message box indicating successful addition
        messagebox.showinfo("Success", "Client added successfully!")
        
    def open_display_client_window(self):
        # Create a new window for displaying client details
        display_client_window = tk.Toplevel(self.master)
        display_client_window.title("Display_Client")
        display_client_window.geometry("300x100")
        display_client_window.configure(bg="Dark Green")

        # Label and Entry for client ID
        lbl_client_id = tk.Label(display_client_window, text="Enter Client ID:", width=15)
        lbl_client_id.grid(row=0, column=0, padx=10, pady=10)
        entry_client_id = tk.Entry(display_client_window, width=20)
        entry_client_id.grid(row=0, column=1, padx=10, pady=10)

        # Submit button
        btn_submit = tk.Button(display_client_window, text="Submit", width=10, command=lambda: self.display_client(entry_client_id.get()))
        btn_submit.grid(row=1, column=0, columnspan=2, pady=10)

    def display_client(self, client_id):
        # Get the client details by ID
        client = Client.display_client_by_id(client_id)

        if client:
            # Create a new window for displaying client details
            display_window = tk.Toplevel(self.master)
            display_window.title("Details_Client")
            display_window.geometry("400x150")
            display_window.configure(bg="Dark Green")

            # Display client details
            lbl_client_details = tk.Label(display_window, text=f"Client ID: {client['client_id']}\n"
                                                                f"Name: {client['name']}\n"
                                                                f"Address: {client['address']}\n"
                                                                f"Contact Details: {client['contact_details']}\n"
                                                                f"Budget: {client['budget']}",
                                          width=40)
            lbl_client_details.pack(pady=10)
        else:
            messagebox.showerror("Error", "Client not found!")
            
    def open_delete_client_window(self):
        # Create a new window for deleting a client
        delete_client_window = tk.Toplevel(self.master)
        delete_client_window.title("Delete_Client")
        delete_client_window.geometry("300x100")
        delete_client_window.configure(bg="Dark Green")

        # Label and Entry for client ID
        lbl_client_id = tk.Label(delete_client_window, text="Enter Client ID:", width=15)
        lbl_client_id.grid(row=0, column=0, padx=10, pady=10)
        entry_client_id = tk.Entry(delete_client_window, width=20)
        entry_client_id.grid(row=0, column=1, padx=10, pady=10)

        # Submit button
        btn_submit = tk.Button(delete_client_window, text="DELETE", width=10, command=lambda: self.client.delete_client(entry_client_id.get()))
        btn_submit.grid(row=1, column=0, columnspan=2, pady=10)


#*****************************Events Section***************************************
            
    def open_event_submenu(self):
        # Create a new window for the event submenu
        event_submenu = tk.Toplevel(self.master)
        event_submenu.title("Event Submenu")
        event_submenu.geometry("400x300")
        event_submenu.configure(bg="Dark Green")

        # Create buttons for event submenu
        btn_add_event = tk.Button(event_submenu, text="ADD", width=20, command=self.open_add_event_window)
        btn_delete_event = tk.Button(event_submenu, text="DELETE", width=20,command=self.open_delete_event_window)
        btn_modify_event = tk.Button(event_submenu, text="MODIFY", width=20, command = self.open_modify_event_window)
        btn_display_event = tk.Button(event_submenu, text="DISPLAY", width=20, command=self.open_display_event_window)

        # Place buttons on the screen
        btn_add_event.pack(pady=10)
        btn_delete_event.pack(pady=10)
        btn_modify_event.pack(pady=10)
        btn_display_event.pack(pady=10)

    def open_add_event_window(self):
        # Create a new window for adding an event
        add_event_window = tk.Toplevel(self.master)
        add_event_window.title("Add_Event")
        add_event_window.geometry("350x550")
        add_event_window.configure(bg="Dark Green")

        # Event details input fields
        lbl_event_id = tk.Label(add_event_window, text="Event ID:", width=20)
        lbl_event_id.grid(row=0, column=0, pady=(20, 5), padx=20, sticky="e")
        entry_event_id = tk.Entry(add_event_window, width=20)
        entry_event_id.grid(row=0, column=1, pady=(20, 5), padx=20, sticky="w")

        lbl_event_type = tk.Label(add_event_window, text="Event Type:", width=20)
        lbl_event_type.grid(row=1, column=0, pady=5, padx=20, sticky="e")
        entry_event_type = tk.Entry(add_event_window, width=20)
        entry_event_type.grid(row=1, column=1, pady=5, padx=20, sticky="w")

        lbl_theme = tk.Label(add_event_window, text="Theme:", width=20)
        lbl_theme.grid(row=2, column=0, pady=5, padx=20, sticky="e")
        entry_theme = tk.Entry(add_event_window, width=20)
        entry_theme.grid(row=2, column=1, pady=5, padx=20, sticky="w")

        lbl_date = tk.Label(add_event_window, text="Date:", width=20)
        lbl_date.grid(row=3, column=0, pady=5, padx=20, sticky="e")
        entry_date = tk.Entry(add_event_window, width=20)
        entry_date.grid(row=3, column=1, pady=5, padx=20, sticky="w")

        lbl_time = tk.Label(add_event_window, text="Time:", width=20)
        lbl_time.grid(row=4, column=0, pady=5, padx=20, sticky="e")
        entry_time = tk.Entry(add_event_window, width=20)
        entry_time.grid(row=4, column=1, pady=5, padx=20, sticky="w")

        lbl_duration = tk.Label(add_event_window, text="Duration:", width=20)
        lbl_duration.grid(row=5, column=0, pady=5, padx=20, sticky="e")
        entry_duration = tk.Entry(add_event_window, width=20)
        entry_duration.grid(row=5, column=1, pady=5, padx=20, sticky="w")

        lbl_venue_address = tk.Label(add_event_window, text="Venue Address:", width=20)
        lbl_venue_address.grid(row=6, column=0, pady=5, padx=20, sticky="e")
        entry_venue_address = tk.Entry(add_event_window, width=20)
        entry_venue_address.grid(row=6, column=1, pady=5, padx=20, sticky="w")

        lbl_client_id = tk.Label(add_event_window, text="Client ID:", width=20)
        lbl_client_id.grid(row=7, column=0, pady=5, padx=20, sticky="e")
        entry_client_id = tk.Entry(add_event_window, width=20)
        entry_client_id.grid(row=7, column=1, pady=5, padx=20, sticky="w")

        lbl_guest_list = tk.Label(add_event_window, text="Guest List:", width=20)
        lbl_guest_list.grid(row=8, column=0, pady=5, padx=20, sticky="e")
        entry_guest_list = tk.Entry(add_event_window, width=20)
        entry_guest_list.grid(row=8, column=1, pady=5, padx=20, sticky="w")

        lbl_catering_company = tk.Label(add_event_window, text="Catering Company:", width=20)
        lbl_catering_company.grid(row=9, column=0, pady=5, padx=20, sticky="e")
        entry_catering_company = tk.Entry(add_event_window, width=20)
        entry_catering_company.grid(row=9, column=1, pady=5, padx=20, sticky="w")

        lbl_cleaning_company = tk.Label(add_event_window, text="Cleaning Company:", width=20)
        lbl_cleaning_company.grid(row=10, column=0, pady=5, padx=20, sticky="e")
        entry_cleaning_company = tk.Entry(add_event_window, width=20)
        entry_cleaning_company.grid(row=10, column=1, pady=5, padx=20, sticky="w")

        lbl_decorations_company = tk.Label(add_event_window, text="Decorations Company:", width=20)
        lbl_decorations_company.grid(row=11, column=0, pady=5, padx=20, sticky="e")
        entry_decorations_company = tk.Entry(add_event_window, width=20)
        entry_decorations_company.grid(row=11, column=1, pady=5, padx=20, sticky="w")

        lbl_entertainment_company = tk.Label(add_event_window, text="Entertainment Company:", width=20)
        lbl_entertainment_company.grid(row=12, column=0, pady=5, padx=20, sticky="e")
        entry_entertainment_company = tk.Entry(add_event_window, width=20)
        entry_entertainment_company.grid(row=12, column=1, pady=5, padx=20, sticky="w")

        lbl_furniture_company = tk.Label(add_event_window, text="Furniture Company:", width=20)
        lbl_furniture_company.grid(row=13, column=0, pady=5, padx=20, sticky="e")
        entry_furniture_company = tk.Entry(add_event_window, width=20)
        entry_furniture_company.grid(row=13, column=1, pady=5, padx=20, sticky="w")

        lbl_invoice = tk.Label(add_event_window, text="Invoice:", width=20)
        lbl_invoice.grid(row=14, column=0, pady=5, padx=20, sticky="e")
        entry_invoice = tk.Entry(add_event_window, width=20)
        entry_invoice.grid(row=14, column=1, pady=5, padx=20, sticky="w")

        # Submit button
        btn_submit = tk.Button(add_event_window, text="Submit", width=20, command=lambda: self.submit_event(
            entry_event_id.get(), entry_event_type.get(), entry_theme.get(), entry_date.get(),
            entry_time.get(), entry_duration.get(), entry_venue_address.get(), entry_client_id.get(),
            entry_guest_list.get(), entry_catering_company.get(), entry_cleaning_company.get(),
            entry_decorations_company.get(), entry_entertainment_company.get(), entry_furniture_company.get(),
            entry_invoice.get()
        ))
        btn_submit.grid(row=15, column=0, columnspan=2, pady=20)

    
    def submit_event(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company, cleaning_company, decorations_company, entertainment_company, furniture_company, invoice):
        # Create an Event object with provided details
        new_event = Event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company, cleaning_company, decorations_company, entertainment_company, furniture_company, invoice)
        
        # Add event details
        new_event.add_event()
        
        # Show a message box indicating successful addition
        messagebox.showinfo("Success", "Event added successfully!")
        
    def open_display_event_window(self):
        # Create a new window for displaying event details
        display_event_window = tk.Toplevel(self.master)
        display_event_window.title("Display_Event")
        display_event_window.geometry("300x100")
        display_event_window.configure(bg="Dark Green")

        # Label and Entry for event ID
        lbl_event_id = tk.Label(display_event_window, text="Enter Event ID:", width=15)
        lbl_event_id.grid(row=0, column=0, padx=10, pady=10)
        entry_event_id = tk.Entry(display_event_window, width=20)
        entry_event_id.grid(row=0, column=1, padx=10, pady=10)

        # Submit button
        btn_submit = tk.Button(display_event_window, text="Submit", width=10, command=lambda: self.display_event(entry_event_id.get()))
        btn_submit.grid(row=1, column=0, columnspan=2, pady=10)

    def display_event(self, event_id):
        # Get the event details by ID
        event = Event.display_event_by_id(event_id)

        if event:
            # Create a new window for displaying event details
            display_window = tk.Toplevel(self.master)
            display_window.title("Event Details")
            display_window.geometry("400x300")
            display_window.configure(bg="Dark Green")

            # Display event details
            lbl_event_details = tk.Label(display_window, text=f"Event ID: {event['event_id']}\n"
                                                               f"Event Type: {event['event_type']}\n"
                                                               f"Theme: {event['theme']}\n"
                                                               f"Date: {event['date']}\n"
                                                               f"Time: {event['time']}\n"
                                                               f"Duration: {event['duration']}\n"
                                                               f"Venue Address: {event['venue_address']}\n"
                                                               f"Client ID: {event['client_id']}\n"
                                                               f"Guest List: {event['guest_list']}\n"
                                                               f"Catering Company: {event['catering_company']}\n"
                                                               f"Cleaning Company: {event['cleaning_company']}\n"
                                                               f"Decorations Company: {event['decorations_company']}\n"
                                                               f"Entertainment Company: {event['entertainment_company']}\n"
                                                               f"Furniture Company: {event['furniture_company']}\n"
                                                               f"Invoice: {event['invoice']}",
                                          width=40)
            lbl_event_details.pack(pady=10)
        else:
            messagebox.showerror("Error", "Event not found!")
            
            
    def open_delete_event_window(self):
        # Create a new window for deleting an event
        delete_event_window = tk.Toplevel(self.master)
        delete_event_window.title("Delete_Event")
        delete_event_window.geometry("300x100")
        delete_event_window.configure(bg="Dark Green")

        # Label and Entry for event ID
        lbl_event_id = tk.Label(delete_event_window, text="Enter Event ID:", width=15)
        lbl_event_id.grid(row=0, column=0, padx=10, pady=10)
        entry_event_id = tk.Entry(delete_event_window, width=20)
        entry_event_id.grid(row=0, column=1, padx=10, pady=10)

        # Submit button
        btn_submit = tk.Button(delete_event_window, text="DELETE", width=10, command=lambda: self.event.delete_event(entry_event_id.get()))
        btn_submit.grid(row=1, column=0, columnspan=2, pady=10)

    def open_modify_event_window(self):
        def fetch_event_details():
            # Get the event details by ID
            event_id = entry_event_id.get()
            event = Event.display_event_by_id(event_id)
            
            if event:
                # entry fields with event details
                entry_new_event_type.delete(0, tk.END)
                entry_new_event_type.insert(0, event['event_type'])
                entry_new_theme.delete(0, tk.END)
                entry_new_theme.insert(0, event['theme'])
                entry_new_date.delete(0, tk.END)
                entry_new_date.insert(0, event['date'])
                entry_new_time.delete(0, tk.END)
                entry_new_time.insert(0, event['time'])
                entry_new_duration.delete(0, tk.END)
                entry_new_duration.insert(0, event['duration'])
                entry_new_venue_address.delete(0, tk.END)
                entry_new_venue_address.insert(0, event['venue_address'])
                entry_new_client_id.delete(0, tk.END)
                entry_new_client_id.insert(0, event['client_id'])
                entry_new_guest_list.delete(0, tk.END)
                entry_new_guest_list.insert(0, event['guest_list'])
                entry_new_catering_company.delete(0, tk.END)
                entry_new_catering_company.insert(0, event['catering_company'])
                entry_new_cleaning_company.delete(0, tk.END)
                entry_new_cleaning_company.insert(0, event['cleaning_company'])
                entry_new_decorations_company.delete(0, tk.END)
                entry_new_decorations_company.insert(0, event['decorations_company'])
                entry_new_entertainment_company.delete(0, tk.END)
                entry_new_entertainment_company.insert(0, event['entertainment_company'])
                entry_new_furniture_company.delete(0, tk.END)
                entry_new_furniture_company.insert(0, event['furniture_company'])
                entry_new_invoice.delete(0, tk.END)
                entry_new_invoice.insert(0, event['invoice'])
                
            else:
                messagebox.showerror("Error", "Event not found!")

        def modify_event_details():
            # Get the modified event details
            modified_event_details = {
                "event_type": entry_new_event_type.get(),
                "theme": entry_new_theme.get(),
                "date": entry_new_date.get(),
                "time": entry_new_time.get(),
                "duration": entry_new_duration.get(),
                "venue_address": entry_new_venue_address.get(),
                "client_id": entry_new_client_id.get(),
                "guest_list": entry_new_guest_list.get(),
                "catering_company": entry_new_catering_company.get(),
                "cleaning_company": entry_new_cleaning_company.get(),
                "decorations_company": entry_new_decorations_company.get(),
                "entertainment_company": entry_new_entertainment_company.get(),
                "furniture_company": entry_new_furniture_company.get(),
                "invoice": entry_new_invoice.get()
            }
            # Call the modify_event method
            event_id = entry_event_id.get()
            Event().modify_event(event_id, modified_event_details)

        # Create a new window for modifying an event
        modify_event_window = tk.Toplevel(self.master)
        modify_event_window.title("Modify_Event")
        modify_event_window.geometry("400x600")
        modify_event_window.configure(bg="Dark Green")

        # Labels and Entries for event details
        lbl_event_id = tk.Label(modify_event_window, text="Event ID:", width=15)
        lbl_event_id.grid(row=0, column=0, pady=10, padx=10, sticky="e")
        entry_event_id = tk.Entry(modify_event_window, width=30)
        entry_event_id.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        lbl_new_event_type = tk.Label(modify_event_window, text="New Event Type:", width=15)
        lbl_new_event_type.grid(row=1, column=0, pady=10, padx=10, sticky="e")
        entry_new_event_type = tk.Entry(modify_event_window, width=30)
        entry_new_event_type.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        lbl_new_theme = tk.Label(modify_event_window, text="New Theme:", width=15)
        lbl_new_theme.grid(row=2, column=0, pady=10, padx=10, sticky="e")
        entry_new_theme = tk.Entry(modify_event_window, width=30)
        entry_new_theme.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        lbl_new_date = tk.Label(modify_event_window, text="New Date:", width=15)
        lbl_new_date.grid(row=3, column=0, pady=10, padx=10, sticky="e")
        entry_new_date = tk.Entry(modify_event_window, width=30)
        entry_new_date.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        lbl_new_time = tk.Label(modify_event_window, text="New Time:", width=15)
        lbl_new_time.grid(row=4, column=0, pady=10, padx=10, sticky="e")
        entry_new_time = tk.Entry(modify_event_window, width=30)
        entry_new_time.grid(row=4, column=1, pady=10, padx=10, sticky="w")

        lbl_new_duration = tk.Label(modify_event_window, text="New Duration:", width=15)
        lbl_new_duration.grid(row=5, column=0, pady=10, padx=10, sticky="e")
        entry_new_duration = tk.Entry(modify_event_window, width=30)
        entry_new_duration.grid(row=5, column=1, pady=10, padx=10, sticky="w")

        lbl_new_venue_address = tk.Label(modify_event_window, text="New Venue Address:", width=15)
        lbl_new_venue_address.grid(row=6, column=0, pady=10, padx=10, sticky="e")
        entry_new_venue_address = tk.Entry(modify_event_window, width=30)
        entry_new_venue_address.grid(row=6, column=1, pady=10, padx=10, sticky="w")

        lbl_new_client_id = tk.Label(modify_event_window, text="New Client ID:", width=15)
        lbl_new_client_id.grid(row=7, column=0, pady=10, padx=10, sticky="e")
        entry_new_client_id = tk.Entry(modify_event_window, width=30)
        entry_new_client_id.grid(row=7, column=1, pady=10, padx=10, sticky="w")

        lbl_new_guest_list = tk.Label(modify_event_window, text="New Guest List:", width=15)
        lbl_new_guest_list.grid(row=8, column=0, pady=10, padx=10, sticky="e")
        entry_new_guest_list = tk.Entry(modify_event_window, width=30)
        entry_new_guest_list.grid(row=8, column=1, pady=10, padx=10, sticky="w")

        lbl_new_catering_company = tk.Label(modify_event_window, text="New Catering Company:", width=15)
        lbl_new_catering_company.grid(row=9, column=0, pady=10, padx=10, sticky="e")
        entry_new_catering_company = tk.Entry(modify_event_window, width=30)
        entry_new_catering_company.grid(row=9, column=1, pady=10, padx=10, sticky="w")

        lbl_new_cleaning_company = tk.Label(modify_event_window, text="New Cleaning Company:", width=15)
        lbl_new_cleaning_company.grid(row=10, column=0, pady=10, padx=10, sticky="e")
        entry_new_cleaning_company = tk.Entry(modify_event_window, width=30)
        entry_new_cleaning_company.grid(row=10, column=1, pady=10, padx=10, sticky="w")

        lbl_new_decorations_company = tk.Label(modify_event_window, text="New Decorations Company:", width=15)
        lbl_new_decorations_company.grid(row=11, column=0, pady=10, padx=10, sticky="e")
        entry_new_decorations_company = tk.Entry(modify_event_window, width=30)
        entry_new_decorations_company.grid(row=11, column=1, pady=10, padx=10, sticky="w")

        lbl_new_entertainment_company = tk.Label(modify_event_window, text="New Entertainment Company:", width=15)
        lbl_new_entertainment_company.grid(row=12, column=0, pady=10, padx=10, sticky="e")
        entry_new_entertainment_company = tk.Entry(modify_event_window, width=30)
        entry_new_entertainment_company.grid(row=12, column=1, pady=10, padx=10, sticky="w")

        lbl_new_furniture_company = tk.Label(modify_event_window, text="New Furniture Company:", width=15)
        lbl_new_furniture_company.grid(row=13, column=0, pady=10, padx=10, sticky="e")
        entry_new_furniture_company = tk.Entry(modify_event_window, width=30)
        entry_new_furniture_company.grid(row=13, column=1, pady=10, padx=10, sticky="w")

        lbl_new_invoice = tk.Label(modify_event_window, text="New Invoice:", width=15)
        lbl_new_invoice.grid(row=14, column=0, pady=10, padx=10, sticky="e")
        entry_new_invoice = tk.Entry(modify_event_window, width=30)
        entry_new_invoice.grid(row=14, column=1, pady=10, padx=10, sticky="w")

        # Button to fetch event details
        btn_fetch_details = tk.Button(modify_event_window, text="Fetch Details", width=20,
                                    command=fetch_event_details)
        btn_fetch_details.grid(row=15, column=0, columnspan=2, pady=10)

        # Submit button to modify event details
        btn_modify = tk.Button(modify_event_window, text="MODIFY", width=20,
                            command=modify_event_details)
        btn_modify.grid(row=16, column=0, columnspan=2, pady=10)

    
#******************************Employee Section*****************************************

    def open_employee_submenu(self):
        # Create a new window for the employee submenu
        employee_submenu = tk.Toplevel(self.master)
        employee_submenu.title("SubMenu_Employee")
        employee_submenu.geometry("400x300")
        employee_submenu.configure(bg="Dark Green")

        # Create buttons for employee submenu
        btn_add_employee = tk.Button(employee_submenu, text="ADD", width=20, command=self.open_add_employee_window)
        btn_delete_employee = tk.Button(employee_submenu, text="DELETE", width=20, command = self.open_delete_employee_window)
        btn_modify_employee = tk.Button(employee_submenu, text="MODIFY", width=20, command=self.open_modify_employee_window)
        btn_display_employee = tk.Button(employee_submenu, text="DISPLAY", width=20, command=self.open_display_employee_window)

        # Place buttons on the screen
        btn_add_employee.pack(pady=10)
        btn_delete_employee.pack(pady=10)
        btn_modify_employee.pack(pady=10)
        btn_display_employee.pack(pady=10)

    def open_add_employee_window(self):
        # Create a new window for adding an employee
        add_employee_window = tk.Toplevel(self.master)
        add_employee_window.title("Add_Employee")
        add_employee_window.geometry("340x350")
        add_employee_window.configure(bg="Dark Green")

        # Employee details input fields
        lbl_name = tk.Label(add_employee_window, text="Name:", width=15)
        lbl_name.grid(row=0, column=0, pady=(20, 5), padx=10, sticky="e")
        entry_name = tk.Entry(add_employee_window, width=30)
        entry_name.grid(row=0, column=1, pady=(20, 5), padx=10, sticky="w")

        lbl_employee_id = tk.Label(add_employee_window, text="Employee ID:", width=15)
        lbl_employee_id.grid(row=1, column=0, pady=5, padx=10, sticky="e")
        entry_employee_id = tk.Entry(add_employee_window, width=30)
        entry_employee_id.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        lbl_department = tk.Label(add_employee_window, text="Department:", width=15)
        lbl_department.grid(row=2, column=0, pady=5, padx=10, sticky="e")
        entry_department = tk.Entry(add_employee_window, width=30)
        entry_department.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        lbl_job_title = tk.Label(add_employee_window, text="Job Title:", width=15)
        lbl_job_title.grid(row=3, column=0, pady=5, padx=10, sticky="e")
        entry_job_title = tk.Entry(add_employee_window, width=30)
        entry_job_title.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        lbl_basic_salary = tk.Label(add_employee_window, text="Basic Salary:", width=15)
        lbl_basic_salary.grid(row=4, column=0, pady=5, padx=10, sticky="e")
        entry_basic_salary = tk.Entry(add_employee_window, width=30)
        entry_basic_salary.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        lbl_age = tk.Label(add_employee_window, text="Age:", width=15)
        lbl_age.grid(row=5, column=0, pady=5, padx=10, sticky="e")
        entry_age = tk.Entry(add_employee_window, width=30)
        entry_age.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        lbl_date_of_birth = tk.Label(add_employee_window, text="Date of Birth:", width=15)
        lbl_date_of_birth.grid(row=6, column=0, pady=5, padx=10, sticky="e")
        entry_date_of_birth = tk.Entry(add_employee_window, width=30)
        entry_date_of_birth.grid(row=6, column=1, pady=5, padx=10, sticky="w")

        lbl_passport_details = tk.Label(add_employee_window, text="Passport Details:", width=15)
        lbl_passport_details.grid(row=7, column=0, pady=5, padx=10, sticky="e")
        entry_passport_details = tk.Entry(add_employee_window, width=30)
        entry_passport_details.grid(row=7, column=1, pady=5, padx=10, sticky="w")
        
        lbl_manager_id = tk.Label(add_employee_window, text="Manager ID:", width=15)
        lbl_manager_id.grid(row=8, column=0, pady=5, padx=10, sticky="e")
        entry_manager_id = tk.Entry(add_employee_window, width=30)
        entry_manager_id.grid(row=8, column=1, pady=5, padx=10, sticky="w")

        # Submit button
        btn_submit = tk.Button(add_employee_window, text="Submit", width=20, command=lambda: self.submit_employee(
            entry_name.get(), entry_employee_id.get(), entry_department.get(), entry_job_title.get(),
            entry_basic_salary.get(), entry_age.get(), entry_date_of_birth.get(), entry_passport_details.get(), 
            entry_manager_id.get()
        ))
        btn_submit.grid(row=9, column=0, columnspan=2, pady=20)
    
    def submit_employee(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, manager_id):
        # Create an Employee object with provided details
        new_employee = Employee(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details,manager_id)
        
        # Add employee details
        new_employee.add_employee(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details,manager_id)
        
        # Show a message box indicating successful addition
        messagebox.showinfo("Success", "Employee added successfully!")

    def open_display_employee_window(self):
        # Create a new window for displaying employee details
        display_employee_window = tk.Toplevel(self.master)
        display_employee_window.title("Display_Employee")
        display_employee_window.geometry("300x100")
        display_employee_window.configure(bg="Dark Green")

        # Label and Entry for employee ID
        lbl_employee_id = tk.Label(display_employee_window, text="Enter Employee ID:", width=15)
        lbl_employee_id.grid(row=0, column=0, padx=10, pady=10)
        entry_employee_id = tk.Entry(display_employee_window, width=20)
        entry_employee_id.grid(row=0, column=1, padx=10, pady=10)

        # Submit button
        btn_submit = tk.Button(display_employee_window, text="Submit", width=10, command=lambda: self.display_employee(entry_employee_id.get()))
        btn_submit.grid(row=1, column=0, columnspan=2, pady=10)

    def display_employee(self, employee_id):
        # Get the employee details by ID
        employee = Employee.display_employee_by_id(employee_id)

        if employee:
            # Create a new window for displaying employee details
            display_window = tk.Toplevel(self.master)
            display_window.title("Employee Details")
            display_window.geometry("400x200")
            display_window.configure(bg="Dark Green")

            # Display employee details
            lbl_employee_details = tk.Label(display_window, text=f"Employee ID: {employee['employee_id']}\n"
                                                                  f"Name: {employee['name']}\n"
                                                                  f"Department: {employee['department']}\n"
                                                                  f"Job Title: {employee['job_title']}\n"
                                                                  f"Basic Salary: {employee['basic_salary']}\n"
                                                                  f"Age: {employee['age']}\n"
                                                                  f"Date of Birth: {employee['date_of_birth']}\n"
                                                                  f"Passport Details: {employee['passport_details']}\n"
                                                                  f"Manager ID: {employee['manager_id']}",
                                                                    
                                             width=40)
            lbl_employee_details.pack(pady=10)
        else:
            messagebox.showerror("Error", "Employee not found!")
            
    def open_delete_employee_window(self):
        # Create a new window for deleting an employee
        delete_employee_window = tk.Toplevel(self.master)
        delete_employee_window.title("Delete_Employee")
        delete_employee_window.geometry("340x150")
        delete_employee_window.configure(bg="Dark Green")

        # Employee ID input field
        lbl_employee_id = tk.Label(delete_employee_window, text="Employee ID:", width=15)
        lbl_employee_id.grid(row=0, column=0, pady=(20, 5), padx=10, sticky="e")
        entry_employee_id = tk.Entry(delete_employee_window, width=30)
        entry_employee_id.grid(row=0, column=1, pady=(20, 5), padx=10, sticky="w")

        # Delete button
        btn_delete = tk.Button(delete_employee_window, text="DELETE", width=20, command=lambda: self.employee.delete_employee(entry_employee_id.get()))
        btn_delete.grid(row=1, column=0, columnspan=2, pady=20)
        
        
    def open_modify_employee_window(self):
        def fetch_employee_details():
            # Get the employee details by ID
            employee_id = entry_employee_id.get()
            employee = Employee.display_employee_by_id(employee_id)

            if employee:
                # entry fields with employee details
                entry_new_name.delete(0, tk.END)
                entry_new_name.insert(0, employee['name'])
                entry_new_department.delete(0, tk.END)
                entry_new_department.insert(0, employee['department'])
                entry_new_job_title.delete(0, tk.END)
                entry_new_job_title.insert(0, employee['job_title'])
                entry_new_basic_salary.delete(0, tk.END)
                entry_new_basic_salary.insert(0, employee['basic_salary'])
                entry_new_age.delete(0, tk.END)
                entry_new_age.insert(0, employee['age'])
                entry_new_date_of_birth.delete(0, tk.END)
                entry_new_date_of_birth.insert(0, employee['date_of_birth'])
                entry_new_passport_details.delete(0, tk.END)
                entry_new_passport_details.insert(0, employee['passport_details'])
                entry_new_manager_id.delete(0, tk.END)
                entry_new_manager_id.insert(0, employee['manager_id'])

            else:
                messagebox.showerror("Error", "Employee not found!")

        def modify_employee_details():
            # Get the modified employee details
            modified_employee_details = {
                "name": entry_new_name.get(),
                "department": entry_new_department.get(),
                "job_title": entry_new_job_title.get(),
                "basic_salary": entry_new_basic_salary.get(),
                "age":entry_new_age.get(),
                "date_of_birth": entry_new_date_of_birth.get(),
                "passport_details": entry_new_passport_details.get(),
                "manager_id":entry_new_manager_id.get()
                # Add other modified details similarly
            }
            # Call the modify_employee method
            employee_id = entry_employee_id.get()
            Employee().modify_employee(employee_id, modified_employee_details)

        # Create a new window for modifying an employee
        modify_employee_window = tk.Toplevel(self.master)
        modify_employee_window.title("Modify_Employee")
        modify_employee_window.geometry("400x400")
        modify_employee_window.configure(bg="Dark Green")

        # Labels and Entries for employee details
        lbl_employee_id = tk.Label(modify_employee_window, text="Employee ID:", width=15)
        lbl_employee_id.grid(row=0, column=0, pady=10, padx=10, sticky="e")
        entry_employee_id = tk.Entry(modify_employee_window, width=30)
        entry_employee_id.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        lbl_new_name = tk.Label(modify_employee_window, text="New Name:", width=15)
        lbl_new_name.grid(row=1, column=0, pady=10, padx=10, sticky="e")
        entry_new_name = tk.Entry(modify_employee_window, width=30)
        entry_new_name.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        lbl_new_department = tk.Label(modify_employee_window, text="New Department:", width=15)
        lbl_new_department.grid(row=2, column=0, pady=10, padx=10, sticky="e")
        entry_new_department = tk.Entry(modify_employee_window, width=30)
        entry_new_department.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        lbl_new_job_title = tk.Label(modify_employee_window, text="New Job Title:", width=15)
        lbl_new_job_title.grid(row=3, column=0, pady=10, padx=10, sticky="e")
        entry_new_job_title = tk.Entry(modify_employee_window, width=30)
        entry_new_job_title.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        lbl_new_basic_salary = tk.Label(modify_employee_window, text="New Basic Salary:", width=15)
        lbl_new_basic_salary.grid(row=4, column=0, pady=10, padx=10, sticky="e")
        entry_new_basic_salary = tk.Entry(modify_employee_window, width=30)
        entry_new_basic_salary.grid(row=4, column=1, pady=10, padx=10, sticky="w")
        
        lbl_new_age = tk.Label(modify_employee_window, text="New Age:", width=15)
        lbl_new_age.grid(row=5, column=0, pady=10, padx=10, sticky="e")
        entry_new_age = tk.Entry(modify_employee_window, width=30)
        entry_new_age.grid(row=5, column=1, pady=10, padx=10, sticky="w")

        lbl_new_date_of_birth = tk.Label(modify_employee_window, text="New Date of Birth:", width=15)
        lbl_new_date_of_birth.grid(row=6, column=0, pady=10, padx=10, sticky="e")
        entry_new_date_of_birth = tk.Entry(modify_employee_window, width=30)
        entry_new_date_of_birth.grid(row=6, column=1, pady=10, padx=10, sticky="w")

        lbl_new_passport_details = tk.Label(modify_employee_window, text="New Passport Details:", width=15)
        lbl_new_passport_details.grid(row=7, column=0, pady=10, padx=10, sticky="e")
        entry_new_passport_details = tk.Entry(modify_employee_window, width=30)
        entry_new_passport_details.grid(row=7, column=1, pady=10, padx=10, sticky="w")
        
        lbl_new_manager_id = tk.Label(modify_employee_window, text="New Manager ID:", width=15)
        lbl_new_manager_id.grid(row=8, column=0, pady=10, padx=10, sticky="e")
        entry_new_manager_id = tk.Entry(modify_employee_window, width=30)
        entry_new_manager_id.grid(row=8, column=1, pady=10, padx=10, sticky="w")

        
        # Button to fetch employee details
        btn_fetch_details = tk.Button(modify_employee_window, text="Fetch Details", width=20,
                                      command=fetch_employee_details)
        btn_fetch_details.grid(row=9, column=0, columnspan=2, pady=20)

        # Submit button to modify employee details
        btn_modify = tk.Button(modify_employee_window, text="MODIFY", width=20,
                               command=modify_employee_details)
        btn_modify.grid(row=10, column=0, columnspan=2, pady=20)

#**************************GUESTS Section*************************************************
        
    def open_guest_submenu(self):
        # Create a new window for the guest submenu
        guest_submenu = tk.Toplevel(self.master)
        guest_submenu.title("SubMenu_Guest")
        guest_submenu.geometry("400x300")
        guest_submenu.configure(bg="Dark Green")

        # Create buttons for guest submenu
        btn_add_guest = tk.Button(guest_submenu, text="ADD", width=20, command=self.open_add_guest_window)
        btn_delete_guest = tk.Button(guest_submenu, text="DELETE", width=20, command = self.open_delete_guest_window)
        btn_modify_guest = tk.Button(guest_submenu, text="MODIFY", width=20, command=self.open_modify_guest_window)
        btn_display_guest = tk.Button(guest_submenu, text="DISPLAY", width=20, command=self.open_display_guest_window)

        # Place buttons on the screen
        btn_add_guest.pack(pady=10)
        btn_delete_guest.pack(pady=10)
        btn_modify_guest.pack(pady=10)
        btn_display_guest.pack(pady=10)

    def open_add_guest_window(self):
        # Create a new window for adding a guest
        add_guest_window = tk.Toplevel(self.master)
        add_guest_window.title("Add_Guest")
        add_guest_window.geometry("340x250")
        add_guest_window.configure(bg="Dark Green")

        # Guest details input fields
        lbl_guest_id = tk.Label(add_guest_window, text="Guest ID:", width=15)
        lbl_guest_id.grid(row=0, column=0, pady=(20, 5), padx=10, sticky="e")
        entry_guest_id = tk.Entry(add_guest_window, width=30)
        entry_guest_id.grid(row=0, column=1, pady=(20, 5), padx=10, sticky="w")

        lbl_name = tk.Label(add_guest_window, text="Name:", width=15)
        lbl_name.grid(row=1, column=0, pady=5, padx=10, sticky="e")
        entry_name = tk.Entry(add_guest_window, width=30)
        entry_name.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        lbl_address = tk.Label(add_guest_window, text="Address:", width=15)
        lbl_address.grid(row=2, column=0, pady=5, padx=10, sticky="e")
        entry_address = tk.Entry(add_guest_window, width=30)
        entry_address.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        lbl_contact_details = tk.Label(add_guest_window, text="Contact Details:", width=15)
        lbl_contact_details.grid(row=3, column=0, pady=5, padx=10, sticky="e")
        entry_contact_details = tk.Entry(add_guest_window, width=30)
        entry_contact_details.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        # Submit button
        btn_submit = tk.Button(add_guest_window, text="SUBMIT", width=20, command=lambda: self.submit_guest(
            entry_guest_id.get(), entry_name.get(), entry_address.get(), entry_contact_details.get()
        ))
        btn_submit.grid(row=4, column=0, columnspan=2, pady=20)

    def submit_guest(self, guest_id, name, address, contact_details):
        # Create a Guest object with provided details
        new_guest = Guest(guest_id, name, address, contact_details)
        
        # Add guest details
        new_guest.add_guest()
        
        # Show a message box indicating successful addition
        messagebox.showinfo("Success", "Guest added successfully!")
        
    def open_display_guest_window(self):
        # Create a new window for displaying guest details
        display_guest_window = tk.Toplevel(self.master)
        display_guest_window.title("Guest_Display")
        display_guest_window.geometry("300x100")
        display_guest_window.configure(bg="Dark Green")

        # Label and Entry for guest ID
        lbl_guest_id = tk.Label(display_guest_window, text="Enter Guest ID:", width=15)
        lbl_guest_id.grid(row=0, column=0, padx=10, pady=10)
        entry_guest_id = tk.Entry(display_guest_window, width=20)
        entry_guest_id.grid(row=0, column=1, padx=10, pady=10)

        # Submit button
        btn_submit = tk.Button(display_guest_window, text="SUBMIT", width=10, command=lambda: self.display_guest(entry_guest_id.get()))
        btn_submit.grid(row=1, column=0, columnspan=2, pady=10)

    def display_guest(self, guest_id):
        # Get the guest details by ID
        guest = Guest.display_guest_by_id(guest_id)

        if guest:
            # Create a new window for displaying guest details
            display_window = tk.Toplevel(self.master)
            display_window.title("Details_Guest")
            display_window.geometry("400x200")
            display_window.configure(bg="Dark Green")

            # Display guest details
            lbl_guest_details = tk.Label(display_window, text=f"Guest ID: {guest['guest_id']}\n"
                                                               f"Name: {guest['name']}\n"
                                                               f"Contact Details: {guest['contact_details']}\n"
                                                               f"Address: {guest['address']}\n",
                                         width=40)
            lbl_guest_details.pack(pady=10)
        else:
            messagebox.showerror("Error", "Guest not found!")
            
    def open_delete_guest_window(self):
        # Create a new window for deleting a client
        delete_guest_window = tk.Toplevel(self.master)
        delete_guest_window.title("Guest_Delete")
        delete_guest_window.geometry("300x100")
        delete_guest_window.configure(bg="Dark Green")

        # Label and Entry for client ID
        lbl_guest_id = tk.Label(delete_guest_window, text="Enter Guest ID:", width=15)
        lbl_guest_id.grid(row=0, column=0, padx=10, pady=10)
        entry_guest_id = tk.Entry(delete_guest_window, width=20)
        entry_guest_id.grid(row=0, column=1, padx=10, pady=10)

        # Submit button
        btn_submit = tk.Button(delete_guest_window, text="Delete", width=10, command=lambda: self.guest.delete_guest(entry_guest_id.get()))
        btn_submit.grid(row=1, column=0, columnspan=2, pady=10)

    def open_modify_guest_window(self):
        def fetch_guest_details():
            guest_id = entry_guest_id.get()
            guest = Guest.display_guest_by_id(guest_id)

            if guest:
                # entry fields with guest details
                entry_new_name.delete(0, tk.END)
                entry_new_name.insert(0, guest['name'])
                entry_new_address.delete(0, tk.END)
                entry_new_address.insert(0, guest['address'])
                entry_new_contact_details.delete(0, tk.END)
                entry_new_contact_details.insert(0, guest['contact_details'])
            else:
                messagebox.showerror("Error", "guest not found!")

        def modify_guest_details():
            modified_guest_details = {
                "name": entry_new_name.get(),
                "address": entry_new_address.get(),
                "contact_details": entry_new_contact_details.get()
            }
            guest_id = entry_guest_id.get()
            Guest().modify_guest(guest_id, modified_guest_details)

        modify_guest_window = tk.Toplevel(self.master)
        modify_guest_window.title("Guest_Modify")
        modify_guest_window.geometry("400x400")
        modify_guest_window.configure(bg="Dark Green")

        lbl_guest_id = tk.Label(modify_guest_window, text="Guest ID:", width=15)
        lbl_guest_id.grid(row=0, column=0, pady=10, padx=10, sticky="e")
        entry_guest_id = tk.Entry(modify_guest_window, width=30)
        entry_guest_id.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        lbl_new_name = tk.Label(modify_guest_window, text="New Name:", width=15)
        lbl_new_name.grid(row=1, column=0, pady=10, padx=10, sticky="e")
        entry_new_name = tk.Entry(modify_guest_window, width=30)
        entry_new_name.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        lbl_new_address = tk.Label(modify_guest_window, text="New Address:", width=15)
        lbl_new_address.grid(row=2, column=0, pady=10, padx=10, sticky="e")
        entry_new_address = tk.Entry(modify_guest_window, width=30)
        entry_new_address.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        lbl_new_contact_details = tk.Label(modify_guest_window, text="New Contact Details:", width=15)
        lbl_new_contact_details.grid(row=3, column=0, pady=10, padx=10, sticky="e")
        entry_new_contact_details = tk.Entry(modify_guest_window, width=30)
        entry_new_contact_details.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        btn_fetch_details = tk.Button(modify_guest_window, text="FETCH DETAILS", width=20, command=fetch_guest_details)
        btn_fetch_details.grid(row=5, column=0, columnspan=2, pady=20)

        btn_modify = tk.Button(modify_guest_window, text="MODIFY", width=20, command=modify_guest_details)
        btn_modify.grid(row=6, column=0, columnspan=2, pady=20)

#*******************************Suppliers Section************************************

    def open_supplier_submenu(self):
        # Create a new window for the supplier submenu
        supplier_submenu = tk.Toplevel(self.master)
        supplier_submenu.title("SubMenu_Supplier")
        supplier_submenu.geometry("400x300")
        supplier_submenu.configure(bg="Dark Green")

        # Create buttons for supplier submenu
        btn_add_supplier = tk.Button(supplier_submenu, text="ADD", width=20, command=self.open_add_supplier_window)
        btn_delete_supplier = tk.Button(supplier_submenu, text="DELETE", width=20, command = self.open_delete_supplier_window)
        btn_modify_supplier = tk.Button(supplier_submenu, text="MODIFY", width=20, command = self.open_modify_supplier_window)
        btn_display_supplier = tk.Button(supplier_submenu, text="DISPLAY", width=20, command=self.open_display_supplier_window)

        # Place buttons on the screen
        btn_add_supplier.pack(pady=10)
        btn_delete_supplier.pack(pady=10)
        btn_modify_supplier.pack(pady=10)
        btn_display_supplier.pack(pady=10)
        
    def open_add_supplier_window(self):
        # Create a new window for adding a supplier
        add_supplier_window = tk.Toplevel(self.master)
        add_supplier_window.title("Add Supplier")
        add_supplier_window.geometry("340x300")
        add_supplier_window.configure(bg="Dark Green")

        # Supplier details input fields
        lbl_supplier_id = tk.Label(add_supplier_window, text="Supplier ID:", width=15)
        lbl_supplier_id.grid(row=0, column=0, pady=(20, 5), padx=10, sticky="e")
        entry_supplier_id = tk.Entry(add_supplier_window, width=30)
        entry_supplier_id.grid(row=0, column=1, pady=(20, 5), padx=10, sticky="w")

        lbl_name = tk.Label(add_supplier_window, text="Name:", width=15)
        lbl_name.grid(row=1, column=0, pady=5, padx=10, sticky="e")
        entry_name = tk.Entry(add_supplier_window, width=30)
        entry_name.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        lbl_address = tk.Label(add_supplier_window, text="Address:", width=15)
        lbl_address.grid(row=2, column=0, pady=5, padx=10, sticky="e")
        entry_address = tk.Entry(add_supplier_window, width=30)
        entry_address.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        lbl_contact_details = tk.Label(add_supplier_window, text="Contact Details:", width=15)
        lbl_contact_details.grid(row=3, column=0, pady=5, padx=10, sticky="e")
        entry_contact_details = tk.Entry(add_supplier_window, width=30)
        entry_contact_details.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        lbl_menu = tk.Label(add_supplier_window, text="Menu:", width=15)
        lbl_menu.grid(row=4, column=0, pady=5, padx=10, sticky="e")
        entry_menu = tk.Entry(add_supplier_window, width=30)
        entry_menu.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        lbl_min_guests = tk.Label(add_supplier_window, text="Min Guests:", width=15)
        lbl_min_guests.grid(row=5, column=0, pady=5, padx=10, sticky="e")
        entry_min_guests = tk.Entry(add_supplier_window, width=30)
        entry_min_guests.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        lbl_max_guests = tk.Label(add_supplier_window, text="Max Guests:", width=15)
        lbl_max_guests.grid(row=6, column=0, pady=5, padx=10, sticky="e")
        entry_max_guests = tk.Entry(add_supplier_window, width=30)
        entry_max_guests.grid(row=6, column=1, pady=5, padx=10, sticky="w")

        # Submit button
        btn_submit = tk.Button(add_supplier_window, text="Submit", width=20, command=lambda: self.submit_supplier(
            entry_supplier_id.get(), entry_name.get(), entry_address.get(), entry_contact_details.get(),
            entry_menu.get(), entry_min_guests.get(), entry_max_guests.get()
        ))
        btn_submit.grid(row=7, column=0, columnspan=2, pady=20)

    def submit_supplier(self, supplier_id, name, address, contact_details, menu, min_guests, max_guests):
        # Create a Supplier object with provided details
        new_supplier = Supplier(supplier_id, name, address, contact_details, menu, min_guests, max_guests)
        
        # Add supplier details
        new_supplier.add_supplier()
        
        # Show a message box indicating successful addition
        messagebox.showinfo("Success", "Supplier added successfully!")
        
    def open_display_supplier_window(self):
        # Create a new window for displaying supplier details
        display_supplier_window = tk.Toplevel(self.master)
        display_supplier_window.title("Supplier_Display")
        display_supplier_window.geometry("300x100")
        display_supplier_window.configure(bg="Dark Green")

        # Label and Entry for supplier ID
        lbl_supplier_id = tk.Label(display_supplier_window, text="Enter Supplier ID:", width=15)
        lbl_supplier_id.grid(row=0, column=0, padx=10, pady=10)
        entry_supplier_id = tk.Entry(display_supplier_window, width=20)
        entry_supplier_id.grid(row=0, column=1, padx=10, pady=10)

        # Submit button
        btn_submit = tk.Button(display_supplier_window, text="Submit", width=10, command=lambda: self.display_supplier(entry_supplier_id.get()))
        btn_submit.grid(row=1, column=0, columnspan=2, pady=10)

    def display_supplier(self, supplier_id):
        # Get the supplier details by ID
        supplier = Supplier.display_supplier_by_id(supplier_id)

        if supplier:
            # Create a new window for displaying supplier details
            display_window = tk.Toplevel(self.master)
            display_window.title("Supplier Details")
            display_window.geometry("400x200")
            display_window.configure(bg="Dark Green")

            # Display supplier details
            lbl_supplier_details = tk.Label(display_window, text=f"Supplier ID: {supplier['supplier_id']}\n"
                                                                   f"Name: {supplier['name']}\n"
                                                                   f"Contact Details: {supplier['contact_details']}\n"
                                                                   f"Address: {supplier['address']}\n"
                                                                   f"Menu: {supplier['menu']}\n"
                                                                   f"Minimum Guests: {supplier['min_guests']}\n"
                                                                   f"Maximum Guests: {supplier['max_guests']}",
                                             width=40)
            lbl_supplier_details.pack(pady=10)
        else:
            messagebox.showerror("Error", "Supplier not found!")
            
    def open_delete_supplier_window(self):
        # Create a new window for deleting a client
        delete_supplier_window = tk.Toplevel(self.master)
        delete_supplier_window.title("Supplier_Delete")
        delete_supplier_window.geometry("300x100")
        delete_supplier_window.configure(bg="Dark Green")

        # Label and Entry for client ID
        lbl_supplier_id = tk.Label(delete_supplier_window, text="Enter Supplier ID:", width=15)
        lbl_supplier_id.grid(row=0, column=0, padx=10, pady=10)
        entry_supplier_id = tk.Entry(delete_supplier_window, width=20)
        entry_supplier_id.grid(row=0, column=1, padx=10, pady=10)

        # Submit button
        btn_submit = tk.Button(delete_supplier_window, text="Delete", width=10, command=lambda: self.supplier.delete_supplier(entry_supplier_id.get()))
        btn_submit.grid(row=1, column=0, columnspan=2, pady=10)
        
    def open_modify_supplier_window(self):
        def fetch_supplier_details():
            supplier_id = entry_supplier_id.get()
            supplier = Supplier.display_supplier_by_id(supplier_id)

            if supplier:
                # entry fields with supplier details
                entry_new_name.delete(0, tk.END)
                entry_new_name.insert(0, supplier['name'])
                entry_new_address.delete(0, tk.END)
                entry_new_address.insert(0, supplier['address'])
                entry_new_contact_details.delete(0, tk.END)
                entry_new_contact_details.insert(0, supplier['contact_details'])
                entry_new_menu.delete(0, tk.END)
                entry_new_menu.insert(0, supplier['menu'])
                entry_new_min_guests.delete(0, tk.END)
                entry_new_min_guests.insert(0, supplier['min_guests'])
                entry_new_max_guests.delete(0, tk.END)
                entry_new_max_guests.insert(0, supplier['max_guests'])
            else:
                messagebox.showerror("Error", "supplier not found!")

        def modify_supplier_details():
            modified_supplier_details = {
                "name": entry_new_name.get(),
                "address": entry_new_address.get(),
                "contact_details": entry_new_contact_details.get(),
                "menu": entry_new_menu.get(),
                "min_guests": entry_new_min_guests.get(),
                "max_guests":entry_new_max_guests.get()
            }
            supplier_id = entry_supplier_id.get()
            Supplier().modify_supplier(supplier_id, modified_supplier_details)

        modify_supplier_window = tk.Toplevel(self.master)
        modify_supplier_window.title("Supplier_Modify")
        modify_supplier_window.geometry("400x400")
        modify_supplier_window.configure(bg="Dark Green")

        lbl_supplier_id = tk.Label(modify_supplier_window, text="Supplier ID:", width=15)
        lbl_supplier_id.grid(row=0, column=0, pady=10, padx=10, sticky="e")
        entry_supplier_id = tk.Entry(modify_supplier_window, width=30)
        entry_supplier_id.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        lbl_new_name = tk.Label(modify_supplier_window, text="New Name:", width=15)
        lbl_new_name.grid(row=1, column=0, pady=10, padx=10, sticky="e")
        entry_new_name = tk.Entry(modify_supplier_window, width=30)
        entry_new_name.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        lbl_new_address = tk.Label(modify_supplier_window, text="New Address:", width=15)
        lbl_new_address.grid(row=2, column=0, pady=10, padx=10, sticky="e")
        entry_new_address = tk.Entry(modify_supplier_window, width=30)
        entry_new_address.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        lbl_new_contact_details = tk.Label(modify_supplier_window, text="New Contact Details:", width=15)
        lbl_new_contact_details.grid(row=3, column=0, pady=10, padx=10, sticky="e")
        entry_new_contact_details = tk.Entry(modify_supplier_window, width=30)
        entry_new_contact_details.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        lbl_new_menu = tk.Label(modify_supplier_window, text="New Menu:", width=15)
        lbl_new_menu.grid(row=4, column=0, pady=10, padx=10, sticky="e")
        entry_new_menu = tk.Entry(modify_supplier_window, width=30)
        entry_new_menu.grid(row=4, column=1, pady=10, padx=10, sticky="w")

        lbl_new_min_guests = tk.Label(modify_supplier_window, text="New Min Guests:", width=15)
        lbl_new_min_guests.grid(row=5, column=0, pady=10, padx=10, sticky="e")
        entry_new_min_guests = tk.Entry(modify_supplier_window, width=30)
        entry_new_min_guests.grid(row=5, column=1, pady=10, padx=10, sticky="w")

        lbl_new_max_guests = tk.Label(modify_supplier_window, text="New Max Guests:", width=15)
        lbl_new_max_guests.grid(row=6, column=0, pady=10, padx=10, sticky="e")
        entry_new_max_guests = tk.Entry(modify_supplier_window, width=30)
        entry_new_max_guests.grid(row=6, column=1, pady=10, padx=10, sticky="w")

        btn_fetch_details = tk.Button(modify_supplier_window, text="Fetch Details", width=20, command=fetch_supplier_details)
        btn_fetch_details.grid(row=7, column=0, columnspan=2, pady=20)

        btn_modify = tk.Button(modify_supplier_window, text="Modify", width=20, command=modify_supplier_details)
        btn_modify.grid(row=8, column=0, columnspan=2, pady=20)

#*******************************Venue Section*****************************************

    def open_venue_submenu(self):
        # Create a new window for the venue submenu
        venue_submenu = tk.Toplevel(self.master)
        venue_submenu.title("Venue Submenu")
        venue_submenu.geometry("400x300")
        venue_submenu.configure(bg="Dark Green")

        # Create buttons for venue submenu
        btn_add_venue = tk.Button(venue_submenu, text="ADD", width=20, command=self.open_add_venue_window)
        btn_delete_venue = tk.Button(venue_submenu, text="DELETE", width=20, command = self.open_delete_venue_window)
        btn_modify_venue = tk.Button(venue_submenu, text="MODIFY", width=20, command = self.open_modify_venue_window)
        btn_display_venue = tk.Button(venue_submenu, text="DISPLAY", width=20, command=self.open_display_venue_window)

        # Place button on the screen
        btn_add_venue.pack(pady=10)
        btn_delete_venue.pack(pady=10)
        btn_modify_venue.pack(pady=10)
        btn_display_venue.pack(pady=10)

    def open_add_venue_window(self):
        # Create a new window for adding a venue
        add_venue_window = tk.Toplevel(self.master)
        add_venue_window.title("Add Venue")
        add_venue_window.geometry("340x300")
        add_venue_window.configure(bg="Dark Green")

        # Venue details input fields
        lbl_venue_id = tk.Label(add_venue_window, text="Venue ID:", width=15)
        lbl_venue_id.grid(row=0, column=0, pady=(20, 5), padx=10, sticky="e")
        entry_venue_id = tk.Entry(add_venue_window, width=30)
        entry_venue_id.grid(row=0, column=1, pady=(20, 5), padx=10, sticky="w")

        lbl_name = tk.Label(add_venue_window, text="Name:", width=15)
        lbl_name.grid(row=1, column=0, pady=5, padx=10, sticky="e")
        entry_name = tk.Entry(add_venue_window, width=30)
        entry_name.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        lbl_address = tk.Label(add_venue_window, text="Address:", width=15)
        lbl_address.grid(row=2, column=0, pady=5, padx=10, sticky="e")
        entry_address = tk.Entry(add_venue_window, width=30)
        entry_address.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        lbl_contact_details = tk.Label(add_venue_window, text="Contact Details:", width=15)
        lbl_contact_details.grid(row=3, column=0, pady=5, padx=10, sticky="e")
        entry_contact_details = tk.Entry(add_venue_window, width=30)
        entry_contact_details.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        lbl_min_guests = tk.Label(add_venue_window, text="Min Guests:", width=15)
        lbl_min_guests.grid(row=4, column=0, pady=5, padx=10, sticky="e")
        entry_min_guests = tk.Entry(add_venue_window, width=30)
        entry_min_guests.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        lbl_max_guests = tk.Label(add_venue_window, text="Max Guests:", width=15)
        lbl_max_guests.grid(row=5, column=0, pady=5, padx=10, sticky="e")
        entry_max_guests = tk.Entry(add_venue_window, width=30)
        entry_max_guests.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        # Submit button
        btn_submit = tk.Button(add_venue_window, text="Submit", width=20, command=lambda: self.submit_venue(
            entry_venue_id.get(), entry_name.get(), entry_address.get(), entry_contact_details.get(),
            entry_min_guests.get(), entry_max_guests.get()
        ))
        btn_submit.grid(row=6, column=0, columnspan=2, pady=20)

    def submit_venue(self, venue_id, name, address, contact_details, min_guests, max_guests):
        # Create a Venue object with provided details
        new_venue = Venue(venue_id, name, address, contact_details, min_guests, max_guests)
        
        # Add venue details
        new_venue.add_venue()
        
        # Show a message box indicating successful addition
        messagebox.showinfo("Success", "Venue added successfully!")
        
    def open_display_venue_window(self):
        # Create a new window for displaying venue details
        display_venue_window = tk.Toplevel(self.master)
        display_venue_window.title("Display Venue")
        display_venue_window.geometry("300x100")
        display_venue_window.configure(bg="Dark Green")

        # Label and Entry for venue ID
        lbl_venue_id = tk.Label(display_venue_window, text="Enter Venue ID:", width=15)
        lbl_venue_id.grid(row=0, column=0, padx=10, pady=10)
        entry_venue_id = tk.Entry(display_venue_window, width=20)
        entry_venue_id.grid(row=0, column=1, padx=10, pady=10)

        # Submit button
        btn_submit = tk.Button(display_venue_window, text="Submit", width=10, command=lambda: self.display_venue(entry_venue_id.get()))
        btn_submit.grid(row=1, column=0, columnspan=2, pady=10)

    def display_venue(self, venue_id):
        # Get the venue details by ID
        venue = Venue.display_venue_by_id(venue_id)

        if venue:
            # Create a new window for displaying venue details
            display_window = tk.Toplevel(self.master)
            display_window.title("Venue Details")
            display_window.geometry("400x250")
            display_window.configure(bg="Dark Green")

            # Display venue details
            lbl_venue_details = tk.Label(display_window, text=f"Venue ID: {venue['venue_id']}\n"
                                                               f"Name: {venue['name']}\n"
                                                               f"Address: {venue['address']}\n"
                                                               f"Minimum Guests: {venue['min_guests']}\n"
                                                               f"Maximum Guests: {venue['max_guests']}\n"
                                                               f"Contact Details: {venue['contact_details']}",
                                         width=40)
            lbl_venue_details.pack(pady=10)
        else:
            messagebox.showerror("Error", "Venue not found!")
            
    def open_delete_venue_window(self):
        # Create a new window for deleting a client
        delete_venue_window = tk.Toplevel(self.master)
        delete_venue_window.title("Delete Venue")
        delete_venue_window.geometry("300x100")
        delete_venue_window.configure(bg="Dark Green")

        # Label and Entry for client ID
        lbl_venue_id = tk.Label(delete_venue_window, text="Enter Venue ID:", width=15)
        lbl_venue_id.grid(row=0, column=0, padx=10, pady=10)
        entry_venue_id = tk.Entry(delete_venue_window, width=20)
        entry_venue_id.grid(row=0, column=1, padx=10, pady=10)

        # Submit button
        btn_submit = tk.Button(delete_venue_window, text="Delete", width=10, command=lambda: self.venue.delete_venue(entry_venue_id.get()))
        btn_submit.grid(row=1, column=0, columnspan=2, pady=10)

    def open_modify_venue_window(self):
        def fetch_venue_details():
            venue_id = entry_venue_id.get()
            venue = Venue.display_venue_by_id(venue_id)

            if venue:
                # entry fields with venue details
                entry_new_name.delete(0, tk.END)
                entry_new_name.insert(0, venue['name'])
                entry_new_address.delete(0, tk.END)
                entry_new_address.insert(0, venue['address'])
                entry_new_contact_details.delete(0, tk.END)
                entry_new_contact_details.insert(0, venue['contact_details'])
                entry_new_min_guests.delete(0, tk.END)
                entry_new_min_guests.insert(0, venue['min_guests'])
                entry_new_max_guests.delete(0, tk.END)
                entry_new_max_guests.insert(0, venue['max_guests'])
            else:
                messagebox.showerror("Error", "venue not found!")

        def modify_venue_details():
            modified_venue_details = {
                "name": entry_new_name.get(),
                "address": entry_new_address.get(),
                "contact_details": entry_new_contact_details.get(),
                "min_guests": entry_new_min_guests.get(),
                "max_guests":entry_new_max_guests.get()
            }
            venue_id = entry_venue_id.get()
            Venue().modify_venue(venue_id, modified_venue_details)

        modify_venue_window = tk.Toplevel(self.master)
        modify_venue_window.title("Modify venue")
        modify_venue_window.geometry("400x400")
        modify_venue_window.configure(bg="Dark Green")

        lbl_venue_id = tk.Label(modify_venue_window, text="Venue ID:", width=15)
        lbl_venue_id.grid(row=0, column=0, pady=10, padx=10, sticky="e")
        entry_venue_id = tk.Entry(modify_venue_window, width=30)
        entry_venue_id.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        lbl_new_name = tk.Label(modify_venue_window, text="New Name:", width=15)
        lbl_new_name.grid(row=1, column=0, pady=10, padx=10, sticky="e")
        entry_new_name = tk.Entry(modify_venue_window, width=30)
        entry_new_name.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        lbl_new_address = tk.Label(modify_venue_window, text="New Address:", width=15)
        lbl_new_address.grid(row=2, column=0, pady=10, padx=10, sticky="e")
        entry_new_address = tk.Entry(modify_venue_window, width=30)
        entry_new_address.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        lbl_new_contact_details = tk.Label(modify_venue_window, text="New Contact Details:", width=15)
        lbl_new_contact_details.grid(row=3, column=0, pady=10, padx=10, sticky="e")
        entry_new_contact_details = tk.Entry(modify_venue_window, width=30)
        entry_new_contact_details.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        lbl_new_min_guests = tk.Label(modify_venue_window, text="New Min Guests:", width=15)
        lbl_new_min_guests.grid(row=4, column=0, pady=10, padx=10, sticky="e")
        entry_new_min_guests = tk.Entry(modify_venue_window, width=30)
        entry_new_min_guests.grid(row=4, column=1, pady=10, padx=10, sticky="w")

        lbl_new_max_guests = tk.Label(modify_venue_window, text="New Max Guests:", width=15)
        lbl_new_max_guests.grid(row=5, column=0, pady=10, padx=10, sticky="e")
        entry_new_max_guests = tk.Entry(modify_venue_window, width=30)
        entry_new_max_guests.grid(row=5, column=1, pady=10, padx=10, sticky="w")

        btn_fetch_details = tk.Button(modify_venue_window, text="Fetch Details", width=20, command=fetch_venue_details)
        btn_fetch_details.grid(row=6, column=0, columnspan=2, pady=20)

        btn_modify = tk.Button(modify_venue_window, text="Modify", width=20, command=modify_venue_details)
        btn_modify.grid(row=7, column=0, columnspan=2, pady=20)
