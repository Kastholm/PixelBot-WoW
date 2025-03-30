class BotAgent:
    def __init__(self, toggle_bot_thread):
        self.toggle_bot_thread = toggle_bot_thread

    def start_bot(self):
        while True:
            if self.toggle_bot_thread.is_set():
                print('Play!')
            else:
                self.toggle_bot_thread.wait()