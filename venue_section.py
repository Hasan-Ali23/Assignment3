import tkinter as tk
from tkinter import messagebox
import pickle

class Venue:
    def __init__(self, venue_id=None, name=None, address=None, contact_details=None, min_guests=None, max_guests=None):
        """Initialize Venue object with specified attributes."""
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.min_guests = min_guests
        self.max_guests = max_guests

    def _load_venues(self):
        """Load existing venue data from file or return an empty list if file doesn't exist."""
        try:
            with open("venues.pickle", "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    def add_venue(self):
        """Add a new venue to the venue data file."""
        venue_data = {
            "venue_id": self.venue_id,
            "name": self.name,
            "address": self.address,
            "contact_details": self.contact_details,
            "min_guests": self.min_guests,
            "max_guests": self.max_guests
        }
        venues = self._load_venues()
        venues.append(venue_data)
        with open("venues.pickle", "wb") as file:
            pickle.dump(venues, file)
        messagebox.showinfo("Success", "Venue added successfully!")

    def delete_venue(self, venue_id):
        """Delete a venue based on the venue_id."""
        venues = self._load_venues()
        updated_venues = [venue for venue in venues if str(venue["venue_id"]) != str(venue_id)]
        with open("venues.pickle", "wb") as file:
            pickle.dump(updated_venues, file)
        messagebox.showinfo("Success", "Venue deleted successfully!")

    def modify_venue(self, venue_id, modified_venue_details):
        """Modify venue details identified by venue_id."""
        venues = self._load_venues()
        for venue in venues:
            if str(venue["venue_id"]) == str(venue_id):
                venue.update(modified_venue_details)
                break
        with open("venues.pickle", "wb") as file:
            pickle.dump(venues, file)
        messagebox.showinfo("Success", "Venue details modified successfully!")

    @staticmethod
    def display_venue_by_id(venue_id):
        """Retrieve venue details by venue_id."""
        try:
            with open("venues.pickle", "rb") as file:
                venues = pickle.load(file)
            for venue in venues:
                if str(venue["venue_id"]) == str(venue_id):
                    return venue
            messagebox.showinfo("Error", "Venue not found!")
            return None
        except (FileNotFoundError, EOFError):
            messagebox.showerror("Error", "No venues found!")
            return None
