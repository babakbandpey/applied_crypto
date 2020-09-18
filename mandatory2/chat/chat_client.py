#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import dh_utils
import json

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Chatter")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = input('Enter port: ')

if not HOST:
    HOST = "127.0.0.1"

if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 2048
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()

"""
Implementing secret key handshake
Generate g as base number
Generate private key
Get p as a Safe Prime modulu
Generate public key
send the g, p and public key to the server
expect a response
calculate a secret key with the server's sessions public key
"""

# g = dh_utils.get_random_base()
g = 2
private_key = dh_utils.generate_private_key()
p = dh_utils.get_random_safe_prime()["p"]

public_key = dh_utils.calc_public_key(private_key, g, p)

print(public_key)

handshake = {
    "data": {
        "type": "INIT_HANDSHAKE",
        "g": g,
        "p": p,
        "public_key": public_key
    }
}
print(private_key)
print(handshake)
client_socket.send(bytes(json.dumps(handshake), "utf8"))

"""
Expecting to receive the handshake response
"""
msg = client_socket.recv(BUFSIZ).decode("utf8")
msg = json.loads(msg)

if "data" in msg and "type" in msg["data"] and msg["data"]["type"] == "HANDSHAKE_RESPONSE" and "server_public_key" in msg["data"]:
    handshake_response = msg["data"]
    msg = ""
    secret_key = dh_utils.calc_secret_key(handshake_response["server_public_key"], private_key, p)
    print(handshake_response)
    print("Secret key:", secret_key)

    print(dh_utils.encrypt_msg(secret_key, "DO YOU READ ME?"))

    client_socket.send(bytes(dh_utils.encrypt_msg(secret_key, "DO YOU READ ME?"), "utf8"))

tkinter.mainloop()  # Starts GUI execution.