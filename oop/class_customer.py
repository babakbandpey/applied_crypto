#!/usr/bin/python3
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Customer(User):
    def __init__(self, name, email, password, membership_type):
        self.name = name
        self.email = email
        self.password = password
        self.membership_type = membership_type

    def update_memebership(self, memebership_type):
        self.membership_type = memebership_type

    def __str__(self):
        return "Name: " + self.name + ", Email: " + self.email + ", Membership type: " + self.membership_type
    
    def __repr__(self):
        return self.__str__()


customers = [
    Customer("Babak", "babak.bandpey@gmail.com", "Password", "Gold"),
    Customer("Babaki", "babak.bandpey@gmail.com", "Password", "Gold")
]

print(customers[1])

