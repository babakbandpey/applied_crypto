#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import dh_utils
import json

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    """
    Expecting the first message to be a json encoded handshake
    """
    msg = client.recv(BUFSIZ).decode("utf8")
    msg = json.loads(msg)

    if "data" in msg and "type" in msg["data"] and msg["data"]["type"] == "INIT_HANDSHAKE" and "public_key" in msg["data"] :
        handshake = msg["data"]
        msg = ""
        session_private_key = dh_utils.generate_private_key()
        session_public_key = dh_utils.calc_public_key(session_private_key, handshake["g"], handshake["p"])
        session_secret_key = dh_utils.calc_secret_key(handshake["public_key"], session_private_key, handshake["p"])

        handshake["session_secret_key"] = session_secret_key

        handshake_response = {
            "data": {
                "type": "HANDSHAKE_RESPONSE",
                "server_public_key": session_public_key
            }
        }

        """
        Sending the handshake response
        """
        client.send(bytes(json.dumps(handshake_response), "utf8"))


        """
        Waiting for the confirmation
        DO YOU READ ME?
        """

        msg = client.recv(BUFSIZ).decode("utf8")

        print(dh_utils.decrypt_msg(session_secret_key, msg))

        name = client.recv(BUFSIZ).decode("utf8")
        handshake["name"] = name

        welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
        client.send(bytes(welcome, "utf8"))
        msg = "%s has joined the chat!" % name
        broadcast(bytes(msg, "utf8"))
        clients[client] = handshake

        while True:
            msg = client.recv(BUFSIZ)
            print(msg)
            if msg != bytes("{quit}", "utf8"):
                broadcast(msg, name+": ")
            else:
                client.send(bytes("{quit}", "utf8"))
                client.close()
                del clients[client]
                broadcast(bytes("%s has left the chat." % name, "utf8"))
                break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 2048
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()