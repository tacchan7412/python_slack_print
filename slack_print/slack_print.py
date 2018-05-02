from slacker import Slacker
import os, sys


class SlackPrint():
    
    def __init__(self, access_token, channel):
        self.access_token = access_token
        self.channel = channel
        self.slacker = Slacker(access_token)

    def print(self, *objects, sep=' ', end='\n', file=sys.stdout, flush=False):
        print(*objects, sep=sep, end=end, file=file, flush=flush)
        text = sep.join([str(x) for x in objects])
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
