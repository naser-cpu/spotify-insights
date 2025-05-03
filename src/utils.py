import os
import sys

def clear_screen():
    """Clears terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_program(conn):
    """Helper function to exit program, from exit option in every menu"""
    
    # Prints an exit message, closes connection if there is one, and exits program
    print("\nExiting program. Goodbye!")
    if conn:
        conn.close()
    sys.exit(0)