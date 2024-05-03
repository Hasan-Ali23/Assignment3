from tkinter import messagebox
import pickle

class Client:
    def __init__(self, client_id=None, name=None, address=None, contact_details=None, budget=None):
        """Initialize Client object with specified attributes."""
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

    def add_client(self):
        """Add a new client by pickling client data to a file."""
        client_data = {
            "client_id": self.client_id,
            "name": self.name,
            "address": self.address,
            "contact_details": self.contact_details,
            "budget": self.budget
        }
        with open("client.pickle", "ab") as file:
            pickle.dump(client_data, file)

    def delete_client(self, client_id):
        """Delete a client by their client_id."""
        try:
            with open("client.pickle", "rb") as file:
                clients = pickle.load(file)

            if isinstance(clients, dict):
                clients = [clients]

            for client in clients:
                if str(client["client_id"]) == str(client_id):
                    clients.remove(client)
                    break
            else:
                messagebox.showerror("Error", "Client not found!")
                return

            with open("client.pickle", "wb") as file:
                pickle.dump(clients, file)

            messagebox.showinfo("Success", "Client deleted successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No clients found!")

    def modify_client(self, client_id, modified_client_details):
        """Modify client details identified by client_id."""
        try:
            with open("client.pickle", "rb") as file:
                clients = pickle.load(file)

            if isinstance(clients, dict):
                clients = [clients]

            for client in clients:
                if str(client["client_id"]) == str(client_id):
                    client.update(modified_client_details)
                    break

            with open("client.pickle", "wb") as file:
                pickle.dump(clients, file)

            messagebox.showinfo("Success", "Client details modified successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No clients found!")

    @staticmethod
    def display_client_by_id(client_id):
        """Retrieve client details by client_id."""
        try:
            with open("client.pickle", "rb") as file:
                clients = pickle.load(file)

            if isinstance(clients, dict):
                clients = [clients]

            for client in clients:
                if str(client["client_id"]) == str(client_id):
                    return client

            return None
        except FileNotFoundError:
            messagebox.showerror("Error", "No clients found!")
            return None
