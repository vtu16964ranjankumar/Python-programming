class Person:
    def __init__(self, name, address, telephone_number):
        self.name = name
        self.address = address
        self.telephone_number = telephone_number

class Customer(Person):
    def __init__(self, name, address, telephone_number, customer_number, on_mailing_list):
        # Call the constructor of the parent class (Person)
        super().__init__(name, address, telephone_number)
        
        # Additional attributes specific to the Customer class
        self.customer_number = customer_number
        self.on_mailing_list = on_mailing_list

# Demonstrate an instance of the Customer class
if __name__ == "__main__":
    # Creating a Customer instance with on_mailing_list set to True
    customer1 = Customer(
        name="John Doe",
        address="123 Main St",
        telephone_number="555-1234",
        customer_number="C123456",
        on_mailing_list=True
    )

    # Accessing attributes of the Customer instance
    print("Customer Name:", customer1.name)
    print("Customer Address:", customer1.address)
    print("Customer Telephone Number:", customer1.telephone_number)
    print("Customer Number:", customer1.customer_number)
    print("On Mailing List:", customer1.on_mailing_list)
print()

# Creating another Customer instance with on_mailing_list set to False
customer2 = Customer(
    name="Jane Smith",
    address="456 Oak St",
    telephone_number="555-5678",
    customer_number="C789012",
    on_mailing_list=False
)

# Accessing and printing attributes of the Customer instance
print("Customer Name:", customer2.name)
print("Customer Address:", customer2.address)
print("Customer Telephone Number:", customer2.telephone_number)
print("Customer Number:", customer2.customer_number)
print("On Mailing List:", customer2.on_mailing_list)
