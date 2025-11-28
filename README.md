📘 Library Management System – README
📄 Overview

This project is a simple Library Management System developed using Python.
It allows librarians or users to manage:

Books

Members

Borrowing and returning of books

Basic analytics report

The system runs entirely in the console and uses JSON files to store data so that it remains saved between runs.

📁 Project Structure
LibraryManagementSystem/
│
├── book.py
├── member.py
├── library.py
├── main.py
└── README.md

📦 Files Description
1️⃣ book.py

Defines the Book class.
Each book stores:

Title

Author

ISBN/Code

Availability status

Number of times borrowed

It also includes methods for marking books as issued or returned.

2️⃣ member.py

Contains the Member class. Members can:

Borrow books

Return books

View the list of books they currently hold

Each member is tracked using a unique Member ID.

3️⃣ library.py

Acts as the main controller for the whole system.
It manages:

Adding books

Registering members

Issuing and receiving books

Analytics (most used book, total members, issued books count)

Saving & loading data using JSON files

4️⃣ main.py

A console-based menu interface that interacts with the Library System.
Users can choose options like:

Add book

Register member

Borrow book

Return book

View statistics

View all books

View all members

💾 Data Persistence

The system automatically creates and updates two files:

library_books.json

library_members.json

These store all information about books and members.
You can delete them anytime to reset the library.

▶️ How to Run the Program

Install Python (version 3.7 or above recommended).

Place all .py files in the same folder.

Open terminal/command prompt in that folder.

Run the program using:

python main.py


Follow the on-screen menu.

📊 Features Summary
Feature	Description
Add Books	Store book info with unique code
Register Members	Create member profiles with unique ID
Issue Book	Issue book to a member if available
Return Book	Accept returned book from a member
Auto-Save	JSON-based persistent storage
Analytics	Shows most borrowed book, active members, issued books count
Menu UI	Easy text-based interface
👨‍💻 Future Enhancements (Optional)

You can extend the project by adding:

Due dates & penalties

Advanced search option

Sorting books

GUI with Tkinter or PyQt

Admin login system
