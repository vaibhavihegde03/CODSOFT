class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number, email, address):
        self.contacts[name] = {'number': number, 'email': email, 'address': address}
        print(f"Added {name} with number {number}, email {email}, and address {address} to contacts.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted {name} from contacts.")
        else:
            print(f"{name} not found in contacts.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Contact found - {name}: {self.contacts[name]}")
        else:
            print(f"{name} not found in contacts.")

    def update_contact(self, name, new_number):
        if name in self.contacts:
            self.contacts[name]['number'] = new_number
            print(f"Updated {name}'s number to {new_number}.")
        else:
            print(f"{name} not found in contacts.")

    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Number: {details['number']}, Email: {details['email']}, Address: {details['address']}")
        else:
            print("No contacts available.")

# Usage example with user input:
my_contacts = ContactBook()

while True:
    print("\nWhat would you like to do?")
    print("1. ADD CONTACT")
    print("2. VIEW CONTACT LIST")
    print("3. SEARCH CONTACT")
    print("4. UPDATE CONTACT")
    print("5. DELETE CONTACT")
    print("6. EXIT")

    choice = input("ENTER YOUR CHOICE  (1-6): ")

    if choice == '1':
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        email = input("Enter the email of the contact: ")
        address = input("Enter the address of the contact: ")
        my_contacts.add_contact(name, number, email, address)
    elif choice == '2':
        my_contacts.display_contacts()
    elif choice == '3':
        name = input("Enter contact name to search: ")
        my_contacts.search_contact(name)
    elif choice == '4':
        name = input("Enter contact name to update: ")
        new_number = input("Enter new number: ")
        my_contacts.update_contact(name, new_number)
    elif choice == '5':
        name = input("Enter contact name to delete: ")
        my_contacts.delete_contact(name)
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
