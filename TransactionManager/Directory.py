import os
import logging


class Directory:
    def __init__(self, path):
        self.path = path
    
    def __str__(self) -> str:
        return f"Directory: {self.path}"

    def exists(self):
        logging.debug(f"Checking if directory exists: {self.path}")
        return os.path.exists(self.path)