
class UserDTO():
    
    def __init__(self, name, lastname, age) -> None:
        self.name = name
        self.lastname = lastname
        self.age = age
        
    def __str__(self) -> str:
        return f"UserDTO<({self.name}, {self.lastname}, {self.age})>"