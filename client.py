import socket
import threading

HOST = "127.0.0.1"
PORT = 5000
ENC = "utf-8"

def receiver(sock):
    while True:
        try:
            data = sock.recv(4096)
            if not data:
                print("Disconnected from server.")
                break
            print(data.decode(ENC), end="")
        except:
            break

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    print("Conectado ao servidor!\n")

    threading.Thread(target=receiver, args=(sock,), daemon=True).start()

    while True:
        msg = input()
        if msg.upper() == "QUIT":
            sock.sendall(b"QUIT\n")
            break
        sock.sendall((msg + "\n").encode(ENC))

if __name__ == "__main__":
    main()
