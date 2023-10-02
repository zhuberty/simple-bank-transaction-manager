import tkinter as tk
from TransactionManager.Client import Client


class TestClientFrameMain:
    test_main_dir = "test_user_data_TestClientFrameMain"
    client = Client.Client(test_main_dir)
    client.update_idletasks()

    def test_check_main_dir(self):
        assert self.client.main_dir is not None

    def test_geometry_correct(self):
        assert self.client.geometry() == "800x600+100+100"

    def test_title_set(self):
        assert self.client.title() == "Transaction Manager"

    def test_frames_created(self):
        assert self.client.frames != {}

    def test_frames_correct(self):
        assert self.client.frames.keys() == {"admin", "main"}

    def test_show_frame(self):
        self.client.show_frame("admin")
        assert self.client.get_showing_frame() == self.client.frames["admin"]
        self.client.show_frame("main")
        assert self.client.get_showing_frame() == self.client.frames["main"]