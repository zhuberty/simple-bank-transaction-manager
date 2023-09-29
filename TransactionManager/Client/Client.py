from .ClientNavigator import ClientNavigator
from .ClientPage import ClientPage


pages = {
    'start': ClientPage('start', 'Start')
}

class Client:
    def __init__(self):
        self.navigator = ClientNavigator(pages)
        self.navigator.go_to_page('start')