class Dialog:
    def __init__(self, options, message:str = "Choose an option:"):
        self.message = message

    def display_message(self):
        print(self.message)

    def display_options(self):
        for option in self.options:
            print(option)

    def loop(self):
        while self.dialog_active:
            self.display_options()
            user_input = self.get_input()
            is_input_valid = self.handle_input(user_input)
            if is_input_valid:
                return user_input
        

    def get_input(self, prompt="Choice: "):
        return input(prompt)

    def handle_input(self, prompt="Choice: ") -> str: 
        user_input = input(prompt)
        if self.is_input_valid(user_input):
            return user_input
        else:
            self.handle_invalid_input(user_input)
            return False

    def is_input_valid(self, input) -> bool:
        pass

    def handle_invalid_input(self, user_input):
        print(f"Invalid input: {user_input}")
        print("Please try again.")