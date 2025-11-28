# book.py - Revised Implementation
# Author: Gaurav Kumar (2501940033)
# Date: 28-11-2025
# Assignment: Library Inventory System - Library logic with persistence

class Book:
    def __init__(self, name, writer, code, is_free=True, times_used=0):
        self.name = name
        self.writer = writer
        self.code = code
        self.is_free = is_free
        self.times_used = times_used

    def mark_taken(self):
        if not self.is_free:
            return False
        self.is_free = False
        self.times_used += 1
        return True

    def mark_returned(self):
        self.is_free = True

    def export(self):
        return {
            "name": self.name,
            "writer": self.writer,
            "code": self.code,
            "is_free": self.is_free,
            "times_used": self.times_used
        }

    @staticmethod
    def build(data):
        return Book(
            data["name"],
            data["writer"],
            data["code"],
            data.get("is_free", True),
            data.get("times_used", 0)
        )

    def __repr__(self):
        s = "Available" if self.is_free else "Issued"
        return f"{self.name} ({self.writer}) | {self.code} | {s} | Used {self.times_used} times"

