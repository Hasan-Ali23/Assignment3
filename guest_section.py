from tkinter import messagebox
import pickle

class Guest:
    def __init__(self, guest_id=None, name=None, address=None, contact_details=None):
        """Initialize Guest object with specified attributes."""
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    def add_guest(self):
        """Add a new guest to the guest data file."""
        guest_data = {
            "guest_id": self.guest_id,
            "name": self.name,
            "address": self.address,
            "contact_details": self.contact_details
        }
        
        with open("guests.pickle", "ab") as file:
            pickle.dump(guest_data, file)  # Append guest data to file

    def delete_guest(self, guest_id):
        """Delete a guest based on the guest_id."""
        try:
            with open("guests.pickle", "rb") as file:
                guests = pickle.load(file)  # Load existing guests from file

            if isinstance(guests, dict):
                guests = [guests]

            for guest in guests:
                if str(guest["guest_id"]) == str(guest_id):
                    guests.remove(guest)  # Remove the specified guest
                    break
            else:
                messagebox.showerror("Error", "Guest not found!")
                return

            with open("guests.pickle", "wb") as file:
                pickle.dump(guests, file)  # Save updated guest list

            messagebox.showinfo("Success", "Guest deleted successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No guests found!")

    def modify_guest(self, guest_id, modified_guest_details):
        """Modify guest details identified by guest_id."""
        try:
            with open("guests.pickle", "rb") as file:
                guests = pickle.load(file)  # Load existing guests from file

            if isinstance(guests, dict):
                guests = [guests]

            for guest in guests:
                if str(guest["guest_id"]) == str(guest_id):
                    guest.update(modified_guest_details)  # Update guest details
                    break

            with open("guests.pickle", "wb") as file:
                pickle.dump(guests, file)  # Save updated guest list

            messagebox.showinfo("Success", "Guest details modified successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No guests found!")

    @staticmethod
    def display_guest_by_id(guest_id):
        """Retrieve guest details by guest_id."""
        try:
            with open("guests.pickle", "rb") as file:
                guests = pickle.load(file)  # Load existing guests from file

            if isinstance(guests, dict):
                guests = [guests]

            for guest in guests:
                if str(guest["guest_id"]) == str(guest_id):
                    return guest  # Return guest details if found

            return None
        except FileNotFoundError:
            messagebox.showerror("Error", "No guests found!")
            return None
