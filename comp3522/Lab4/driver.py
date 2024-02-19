"""
Main script for running the FAM (Family Asset Management) system.

This script initializes a FAM system, loads test users, and displays the main menu to the user.

Author: Yongeun Kwon (A01263922), Munyoung Cho (A01330048)
"""

from fam import FAM


def main():
    """
    Main function to run the FAM system.

    Initializes a new FAM system, loads test users, and displays the main menu to the user.
    """
    # Create a new FAM system
    fam_system = FAM()

    # Load test users
    fam_system.load_test_users()

    # Display the main menu to the user
    fam_system.display_main_menu()


if __name__ == "__main__":
    main()
