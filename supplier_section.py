import tkinter as tk
from tkinter import messagebox
import pickle

class Supplier:
    def __init__(self, supplier_id=None, name=None, address=None, contact_details=None, menu=None, min_guests=None, max_guests=None):
        """Initialize Supplier object with specified attributes."""
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.menu = menu
        self.min_guests = min_guests
        self.max_guests = max_guests

    def add_supplier(self):
        """Add a new supplier to the supplier data file."""
        data = {
            "supplier_id": self.supplier_id,
            "name": self.name,
            "address": self.address,
            "contact_details": self.contact_details,
            "menu": self.menu,
            "min_guests": self.min_guests,
            "max_guests": self.max_guests
        }
        with open("suppliers.pickle", "ab") as file:
            pickle.dump(data, file)  # Append supplier data to file

    def delete_supplier(self, supplier_id):
        """Delete a supplier based on the supplier_id."""
        try:
            with open("suppliers.pickle", "rb") as file:
                suppliers = pickle.load(file)  # Load existing suppliers from file

            if isinstance(suppliers, dict):
                suppliers = [suppliers]

            for supplier in suppliers:
                if str(supplier["supplier_id"]) == str(supplier_id):
                    suppliers.remove(supplier)  # Remove the specified supplier
                    break
            else:
                messagebox.showerror("Error", "Supplier not found!")
                return

            with open("suppliers.pickle", "wb") as file:
                pickle.dump(suppliers, file)  # Save updated supplier list

            messagebox.showinfo("Success", "Supplier deleted successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No Suppliers found!")

    def modify_supplier(self, supplier_id, modified_supplier_details):
        """Modify supplier details identified by supplier_id."""
        try:
            with open("suppliers.pickle", "rb") as file:
                suppliers = pickle.load(file)  # Load existing suppliers from file

            if isinstance(suppliers, dict):
                suppliers = [suppliers]

            for supplier in suppliers:
                if str(supplier["supplier_id"]) == str(supplier_id):
                    supplier.update(modified_supplier_details)  # Update supplier details
                    break

            with open("suppliers.pickle", "wb") as file:
                pickle.dump(suppliers, file)  # Save updated supplier list

            messagebox.showinfo("Success", "Supplier details modified successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No suppliers found!")

    @staticmethod
    def display_supplier_by_id(supplier_id):
        """Retrieve supplier details by supplier_id."""
        try:
            with open("suppliers.pickle", "rb") as file:
                suppliers = pickle.load(file)  # Load existing suppliers from file

            if isinstance(suppliers, dict):
                suppliers = [suppliers]

            for supplier in suppliers:
                if str(supplier["supplier_id"]) == str(supplier_id):
                    return supplier  # Return supplier details if found

            return None
        except FileNotFoundError:
            messagebox.showerror("Error", "No suppliers found!")
            return None
