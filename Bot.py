from AddressBook import *
from UserInterface import *


class Bot:
    def __init__(self):
        self.book = AddressBook()
        self.ui = ConsoleUI()

    def handle(self, action):
        if action == 'add':
            name = Name(self.ui.get_input("Name: ")).value.strip()
            phones = Phone().value
            birth = Birthday().value
            email = Email().value.strip()
            status = Status().value.strip()
            note = Note(self.ui.get_input("Note: ")).value
            record = Record(name, phones, birth, email, status, note)
            return self.book.add(record)
        elif action == 'search':
            self.ui.display("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
            category = self.ui.get_input('Search category: ')
            pattern = self.ui.get_input('Search pattern: ')
            result = (self.book.search(pattern, category))
            for account in result:
                if account['birthday']:
                    birth = account['birthday'].strftime("%d/%m/%Y")
                    result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                    self.ui.display(result)
        elif action == 'edit':
            contact_name = self.ui.get_input('Contact name: ')
            parameter = self.ui.get_input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
            new_value = self.ui.get_input("New Value: ")
            return self.book.edit(contact_name, parameter, new_value)
        elif action == 'remove':
            pattern = self.ui.get_input("Remove (contact name or phone): ")
            return self.book.remove(pattern)
        elif action == 'save':
            file_name = self.ui.get_input("File name: ")
            return self.book.save(file_name)
        elif action == 'load':
            file_name = self.ui.get_input("File name: ")
            return self.book.load(file_name)
        elif action == 'congratulate':
            self.ui.display(self.book.congratulate())
        elif action == 'view':
            self.ui.display(self.book)
        elif action == 'exit':
            pass
        else:
            self.ui.display("There is no such command!")
