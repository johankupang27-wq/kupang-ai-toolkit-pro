from rich import print
import os

def banner():
    print("[bold cyan]========================")
    print("[bold green] KUPANG AI TOOLKIT PRO")
    print("[bold cyan]========================\n")

def menu():
    banner()
    print("[1] Device Scanner")
    print("[2] AI Generator")
    print("[3] File Organizer")
    print("[4] Export Report")
    print("[0] Exit")
    return input("\nSelect > ")

while True:
    choice = menu()

    if choice == "1":
        print("Scanner running...")
    elif choice == "2":
        print("AI generating...")
    elif choice == "3":
        print("Organizing files...")
    elif choice == "4":
        print("Exporting PDF...")
    else:
        break

    input("\nEnter to continue...")
    os.system("clear")
