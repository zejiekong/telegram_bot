# Telegram Bot Server-Client Program

## Requirement
In same folder, create a file called tele_config.py with the macros below set:
```
TOKEN =  "<telegram api token>"

UPDATE_URL = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

CHAT_ID = "<telegram bot chat id>"

LISTEN_PORT = <port for server to listen> e.g. 12345

CLIENT_NUM = <num of clients> e.g 1

TIMEOUT = <server timeout in seconds> e.g. 60
```