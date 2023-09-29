class ClientDialog:
    def __init__(self, options, message: str = "Choose an option:"):
        self.options = options
        self.message = message
        self.user_input = None

    def display_message(self):
        print(self.message)

    def loop(self):
        while self.user_input is None:
            self.handle_dialog()

    def handle_dialog(self):
        self.display_options()
        if self.get_valid_input():
            self.user_input = self.get_valid_input()

    def display_options(self):
        for i, option in enumerate(self.options):
            print(i + 1, ": ", option)

    def get_valid_input(self):
        user_input = self.get_input()
        if self.is_input_valid(user_input):
            return user_input
        else:
            return False


    def get_input(self, prompt="Choice: "):
        return input(prompt)

    def handle_input(self, prompt="Choice: ") -> str:
        self.get_input()
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
