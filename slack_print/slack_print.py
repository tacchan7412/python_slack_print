from slacker import Slacker
import os


class SlackPrint():
    
    def __init__(self, access_token, channel):
        self.access_token = access_token
        self.channel = channel
        self.slacker = Slacker(access_token)

    def print(self, text):
        print(text)
        try:
            self.slacker.chat.post_message(
                channel = self.channel,
                text = text
            )
        except:
            pass

    def upload(self, path):
        try:
            self.slacker.files.upload(
                file_=path, 
                filename=os.path.basename(path),
                channels=self.channel
            )
        except:
            pass
