# Main.py
# Author: Gaurav Kumar (2501940033)
# Date: 28-11-2025
# Assignment: Library Inventory System - Library logic with persistence
from library import LibrarySystem
from book import Book
from member import Member

def banner():
    print("\n======== LIBRARY CONTROL PANEL ========\n")

def run():
    system = LibrarySystem()
    while True:
        print("\nOptions:")
        print("1) Add new book")
        print("2) Register new member")
        print("3) Issue a book")
        print("4) Accept returned book")
        print("5) Show statistics")
        print("6) Display all books")
        print("7) Display all members")
        print("0) Exit")

        ch = input("Select: ").strip()

        if ch == "1":
            title = input("Book title: ")
            writer = input("Writer name: ")
            code = input("Book code: ")
            if system.insert_book(Book(title, writer, code)):
                print("Book added.")
            else:
                print("Book already exists.")

        elif ch == "2":
            nm = input("Member name: ")
            mid = input("Member ID: ")
            if system.add_member(Member(nm, mid)):
                print("Member registered.")
            else:
                print("ID already present.")

        elif ch == "3":
            mid = input("Member ID: ")
            bc = input("Book code: ")
            ok, msg = system.issue(mid, bc)
            print(msg)

        elif ch == "4":
            mid = input("Member ID: ")
            bc = input("Book code: ")
            ok, msg = system.receive(mid, bc)
            print(msg)

        elif ch == "5":
            print("\n---- LIBRARY STATUS ----")
            print(system.summary())

        elif ch == "6":
            print("\n--- Books ---")
            for b in system.list_all_books():
                print(b)

        elif ch == "7":
            print("\n--- Members ---")
            for m in system.list_all_members():
                print(m)

        elif ch == "0":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    banner()
    run()

