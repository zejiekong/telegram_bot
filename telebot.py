"""
Telegram bot to send message to ownself
"""
import requests
import socket
from tele_config import *

class TeleBot():
    def get_updates(self): 
        """
        Get chat id. Note to disable telegram bot privacy before using this method. 
        """
        response = requests.get(UPDATE_URL)
        return response

    def send_message(self,msg):
        msg_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={msg}"
        response = requests.get(msg_url)
        return response

class TeleBotServer(TeleBot):
    def __init__(self):
        super().__init__()
        self.s = None

    def start(self):
        #Initialise
        self.s = socket.socket()
        self.s.settimeout(1)
        self.s.bind(('127.0.0.1',LISTEN_PORT))
        self.s.listen(CLIENT_NUM)

        timeout_count = 0
        #check for connected client for 1 min
        while timeout_count < TIMEOUT:
            try:
                c, addr = self.s.accept()
                print(f"{addr} client connected")
                break
            except TimeoutError:
                print("Connection Timeout: ",timeout_count)
                timeout_count += 1
        
        if timeout_count < TIMEOUT:
            #check for messages
            while True:
                try:
                    msg = c.recv(1024).decode()
                    if not msg: #check for closed client
                        print("client disconnected")
                        break
                    if msg != "":
                        print(msg)
                        print(self.send_message(msg))
                except KeyboardInterrupt:
                    break

        c.close()

if __name__ == "__main__":
    server = TeleBotServer()
    server.start()
    


    



