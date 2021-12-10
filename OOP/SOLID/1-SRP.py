# 1. SRP 단일 책임 원칙
from enum import Enum

class UserRole(Enum):
	User  = 1
	Admin = 2

class User:
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name    = name
        self.role    = role
    
    def is_admin(self):
        return self.role == UserRole.Admin.name
    
    def greet(self):
        print(f"Hello, {self.name}")
    
    def create_order(self):
        pass

# create_order 함수는 SRP 규칙에 따라 다른 클래스에 속해 있어야 한다.

class User:
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name    = name
        self.role    = role
    
    def is_admin(self):
        return self.role == UserRole.Admin.name
    
    def greet(self):
        print(f"Hello, {self.name}")

class Order:
    def __init__(self):
        pass
    
    def create_order(self):
        pass

# create_order 메소드는 Order 클래스로 옴겨지므로서 User 클래스가 주문을 생성하는 책임까지 지지 않도록 되었다.