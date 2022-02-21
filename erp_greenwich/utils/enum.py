from enum import Enum


class Role(Enum):  # A subclass of Enum
    ADMIN = "Admin"
    STAFF = "Staff"
    SECURITY = "Security"
    STUDENT = "Student"
    MANAGER = "Manager"
