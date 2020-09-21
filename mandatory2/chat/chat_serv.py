#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM, error as SocketError
from threading import Thread
import dh_utils
import json
from signal import signal, SIGINT
from sys import exit


def handler(signal_received, frame):
    # Handle any cleanup here
    SERVER.close()
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)        
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

        handshake["box"] = dh_utils.create_secret_box(session_secret_key)

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

        if dh_utils.decrypt_msg(handshake["box"], client.recv(BUFSIZ)) == "DO YOU READ ME?":

            """
            Replying
            ROGER, ROGER, ROGER
            """

            client.send(
                dh_utils.encrypt_msg(
                    handshake["box"], 
                    "ROGER, ROGER, ROGER"
                )
            )

            dh_utils.decrypt_msg(handshake["box"], client.recv(BUFSIZ))

            client.send(
                dh_utils.encrypt_msg(
                    handshake["box"], 
                    "Greetings from the cave! Now type your name and press enter!"
                )
            )

            name = dh_utils.decrypt_msg(handshake["box"], client.recv(BUFSIZ))
            handshake["name"] = name

            client.send(
                dh_utils.encrypt_msg(
                    handshake["box"], 
                    'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
                )
            )
            
            msg = "%s has joined the chat!" % name
            broadcast(msg)

            clients[client] = handshake

            while True:
                msg = dh_utils.decrypt_msg(handshake["box"], client.recv(BUFSIZ))
                print(msg)
                if msg != "{quit}":
                    broadcast(msg, name+": ")
                else:
                    client.send(
                        dh_utils.encrypt_msg(
                            handshake["box"], 
                            "{quit}"
                        )
                    )
                    client.close()
                    del clients[client]
                    broadcast("%s has left the chat." % name)
                    break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for client in clients:
        client.send(
            dh_utils.encrypt_msg(
                clients[client]["box"], 
                prefix + msg
            )
        )

try:
    clients = {}
    addresses = {}

    HOST = ''
    PORT = 33000
    BUFSIZ = 2048
    ADDR = (HOST, PORT)

    SERVER = socket(AF_INET, SOCK_STREAM)
    SERVER.bind(ADDR)

    if __name__ == "__main__":

        signal(SIGINT, handler)

        SERVER.listen(5)
        print("Waiting for connection...")
        ACCEPT_THREAD = Thread(target=accept_incoming_connections)
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
        SERVER.close()

except SocketError:
    print(SocketError)
    SERVER.close()    
    exit(0)
finally:
    SERVER.close()    