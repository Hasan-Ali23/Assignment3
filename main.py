import tkinter as tk
from gui import MainMenu  # Assuming MainMenu is defined in GUI module

def create_main_window():
    """Create and configure the main Tkinter window."""
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("400x400")
    root.configure(bg="orange")
    return root

def setup_main_menu(root):
    """Create and configure the main menu widget."""
    main_menu = MainMenu(root)
    return main_menu

def run_application():
    """Run the main application."""
    root = create_main_window()
    main_menu = setup_main_menu(root)
    root.mainloop()

if __name__ == "__main__":
    run_application()
