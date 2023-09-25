import os


class Directory:
    def __init__(self, path):
        self.path = path
    
    def __str__(self) -> str:
        return f"Directory: {self.path}"

    def exists(self):
        return os.path.exists(self.path)