from tkinter import messagebox
import pickle

class Event:
    def __init__(self, event_id=None, event_type=None, theme=None, date=None, time=None, duration=None, venue_address=None, client_id=None, guest_list=None, catering_company=None, cleaning_company=None, decorations_company=None, entertainment_company=None, furniture_company=None, invoice=None):
        """Initialize Event object with specified attributes."""
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.catering_company = catering_company
        self.cleaning_company = cleaning_company
        self.decorations_company = decorations_company
        self.entertainment_company = entertainment_company
        self.furniture_company = furniture_company
        self.invoice = invoice

    def add_event(self):
        """Add a new event to the event data file."""
        event_data = {
            "event_id": self.event_id,
            "event_type": self.event_type,
            "theme": self.theme,
            "date": self.date,
            "time": self.time,
            "duration": self.duration,
            "venue_address": self.venue_address,
            "client_id": self.client_id,
            "guest_list": self.guest_list,
            "catering_company": self.catering_company,
            "cleaning_company": self.cleaning_company,
            "decorations_company": self.decorations_company,
            "entertainment_company": self.entertainment_company,
            "furniture_company": self.furniture_company,
            "invoice": self.invoice
        }
        
        with open("events.pickle", "ab") as file:
            pickle.dump(event_data, file)  # Append event data to file

    def delete_event(self, event_id):
        """Delete an event based on the event_id."""
        try:
            with open("events.pickle", "rb") as file:
                events = pickle.load(file)  # Load existing events from file

            if isinstance(events, dict):
                events = [events]

            for event in events:
                if str(event["event_id"]) == str(event_id):
                    events.remove(event)  # Remove the specified event
                    break
            else:
                messagebox.showerror("Error", "Event not found!")
                return

            with open("events.pickle", "wb") as file:
                pickle.dump(events, file)  # Save updated event list

            messagebox.showinfo("Success", "Event deleted successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No events found!")
        
    def modify_event(self, event_id, modified_event_details):
        """Modify event details identified by event_id."""
        try:
            with open("events.pickle", "rb") as file:
                events = pickle.load(file)  # Load existing events from file

            if isinstance(events, dict):
                events = [events]

            for event in events:
                if str(event["event_id"]) == str(event_id):
                    event.update(modified_event_details)  # Update event details
                    break

            with open("events.pickle", "wb") as file:
                pickle.dump(events, file)  # Save updated event list

            messagebox.showinfo("Success", "Event details modified successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No events found!")

    @staticmethod
    def display_event_by_id(event_id):
        """Retrieve event details by event_id."""
        try:
            with open("events.pickle", "rb") as file:
                events = pickle.load(file)  # Load existing events from file

            if isinstance(events, dict):
                events = [events]

            for event in events:
                if str(event["event_id"]) == str(event_id):
                    return event  # Return event details if found

            return None
        except FileNotFoundError:
            messagebox.showerror("Error", "No events found!")
            return None
