from .ClientDialog import ClientDialog
from .ClientNavigator import ClientNavigator


class ClientPage:
    def __init__(
        self,
        title: str,
        short_introduction: str = "",
        action_options: list = [],
        dialog: ClientDialog = ClientDialog(['Go to sleep']),
    ):
        self.title = title
        self.short_introduction = short_introduction
        self.action_options = action_options
        self.sections = []
        self.dialog = dialog
        self.display_content()
        self.dialog.loop()

    def add_section(self, section):
        self.sections.append(section)

    def display_content(self):
        print(self.title)
        print("-" * len(self.title))
        if self.short_introduction:
            print(self.short_introduction)
        for action_option in self.action_options:
            print(f"{nav_option.index}. {nav_option.title}")

    def display_section(self, section):
        pass

    def display_sections(self):
        pass
