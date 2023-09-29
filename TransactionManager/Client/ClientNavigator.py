class ClientNavigator:
    def __init__(self):
        self.current_page = None

    def add_page(self, page):
        self.current_page = page

    def get_current_page(self):
        return self.current_page

    def go_to_page(self, page):
        self.current_page = page

    def get_nav_tree(self):
        pass