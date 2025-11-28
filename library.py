# library.py - Entirely Rewritten
# Author: <Your Name>

import json
from book import Book
from member import Member

class LibrarySystem:
    def __init__(self, books_file="library_books.json", members_file="library_members.json"):
        self.books_file = books_file
        self.members_file = members_file
        self.books = {}
        self.members = {}
        self._load()

    # ------------------------------ Data control
    def _load(self):
        # load books
        try:
            with open(self.books_file, "r") as f:
                for item in json.load(f):
                    obj = Book.build(item)
                    self.books[obj.code] = obj
        except:
            self.books = {}

        # load members
        try:
            with open(self.members_file, "r") as f:
                for item in json.load(f):
                    mem = Member.unpack(item)
                    self.members[mem.uid] = mem
        except:
            self.members = {}

    def _save_all(self):
        with open(self.books_file, "w") as f:
            json.dump([b.export() for b in self.books.values()], f, indent=3)

        with open(self.members_file, "w") as f:
            json.dump([m.export() for m in self.members.values()], f, indent=3)

    # ------------------------------ Book operations
    def insert_book(self, obj):
        if obj.code in self.books:
            return False
        self.books[obj.code] = obj
        self._save_all()
        return True

    # ------------------------------ Member operations
    def add_member(self, mem):
        if mem.uid in self.members:
            return False
        self.members[mem.uid] = mem
        self._save_all()
        return True

    # ------------------------------ Borrowing
    def issue(self, uid, code):
        m = self.members.get(uid)
        b = self.books.get(code)
        if not m: return (False, "No such member.")
        if not b: return (False, "Book missing.")
        if not b.is_free: return (False, "Book already issued.")
        if m.take(b):
            self._save_all()
            return (True, "Issued successfully.")
        return (False, "Unable to issue.")

    def receive(self, uid, code):
        m = self.members.get(uid)
        b = self.books.get(code)
        if not m or not b:
            return (False, "Invalid details.")
        if m.give_back(b):
            self._save_all()
            return (True, "Returned.")
        return (False, "Member does not hold this book.")

    # ------------------------------ Analytics
    def summary(self):
        if not self.books:
            return "No books available."

        highest = max(self.books.values(), key=lambda x: x.times_used, default=None)
        s = []
        s.append(f"Total Members: {len(self.members)}")
        s.append(f"Books currently issued: " +
                 f"{len([x for x in self.books.values() if not x.is_free])}")
        s.append("Most used book: ")
        if highest:
            s.append(f"  -> {highest}")
        return "\n".join(s)

    def list_all_books(self):
        return list(self.books.values())

    def list_all_members(self):
        return list(self.members.values())
