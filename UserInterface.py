from abc import ABC, abstractmethod


class UserInterface(ABC):
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def get_input(self):
        pass


class ConsoleUI(UserInterface):
    def display(self, message):
        print(message)

    def get_input(self, prompt):
        return input(prompt)
