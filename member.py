# member.py - Updated Version
# Author: Gaurav Kumar (2501940033)
# Date: 28-11-2025
# Assignment: Library Inventory System - Library logic with persistence

class Member:
    def __init__(self, full_name, uid, holding=None):
        self.full_name = full_name
        self.uid = uid
        self.holding = holding if holding else []

    def take(self, book):
        if not book.is_free:
            return False
        if book.code in self.holding:
            return False
        book.mark_taken()
        self.holding.append(book.code)
        return True

    def give_back(self, book):
        if book.code not in self.holding:
            return False
        book.mark_returned()
        self.holding.remove(book.code)
        return True

    def export(self):
        return {
            "full_name": self.full_name,
            "uid": self.uid,
            "holding": self.holding
        }

    @staticmethod
    def unpack(data):
        return Member(data["full_name"], data["uid"], data.get("holding", []))

    def __repr__(self):
        return f"{self.full_name} [{self.uid}] | Books taken: {len(self.holding)}"

