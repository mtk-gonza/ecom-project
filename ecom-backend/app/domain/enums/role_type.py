from enum import Enum

class RoleType(Enum):
    ROOT = 'root'
    ADMIN = 'admin'
    EDITOR = 'editor'
    USER = 'user'
    GUEST = 'guest'