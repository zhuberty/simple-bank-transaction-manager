from time import sleep
from TransactionManager.Client import Client


class TestClient:
    client = Client.Client()
    client.update_idletasks()

    def test_geometry_correct(self):
        assert self.client.geometry() == "800x600+100+100"

    def test_title_set(self):
        assert self.client.title() == "Transaction Manager"

    def test_frames_created(self):
        assert self.client.frames != {}

    def test_frames_correct(self):
        assert self.client.frames.keys() == {Client.PageAdmin, Client.MainPage}


    def test_show_frame(self):
        self.client.show_frame(Client.PageAdmin)

        # set page to PageAdmin
        assert self.client.frames[Client.PageAdmin].is_active
        # loop over other frames and make sure they are not active
        for frame in self.client.frames.values():
            if frame is not self.client.frames[Client.PageAdmin]:
                assert not frame.is_active

        self.client.show_frame(Client.MainPage)
        # loop over other frames and make sure they are not active
        for frame in self.client.frames.values():
            if frame is not self.client.frames[Client.MainPage]:
                assert not frame.is_active
        
