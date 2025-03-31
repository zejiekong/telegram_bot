import socket

s = socket.socket()
s.settimeout(1)
timeout_count = 0
while timeout_count < 60:
    try:
        s.connect(("127.0.0.1",12345))
        break
        
    except TimeoutError:
        print("Timeout count: ",timeout_count)

while True:
    try:
        user_input = input("input word")
        s.send(user_input.encode())
    except KeyboardInterrupt:
        break

s.close()