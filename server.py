import socket
import threading

HOST = '0.0.0.0'
PORT = 5000
ENC = 'utf-8'

lock = threading.Lock()
clients = {}

def send_system(conn, msg):
    try:
        conn.sendall((f"SYSTEM: {msg}\n").encode(ENC))
    except:
        pass

def broadcast(sender_nick, msg):
    to_remove = []
    with lock:
        for nick, (conn, _) in clients.items():
            try:
                conn.sendall((f"FROM {sender_nick} [all]: {msg}\n").encode(ENC))
            except:
                to_remove.append(nick)

        for nick in to_remove:
            if nick in clients:
                conn, _ = clients.pop(nick)
                try: conn.close()
                except: pass

def send_direct(sender_nick, target_nick, msg):
    with lock:
        if target_nick not in clients:
            return False
        conn, _ = clients[target_nick]
        try:
            conn.sendall((f"FROM {sender_nick} [dm]: {msg}\n").encode(ENC))
            return True
        except:
            if target_nick in clients:
                conn, _ = clients.pop(target_nick)
                try: conn.close()
                except: pass
            return False

def _remove_client(nick):
    with lock:
        if nick in clients:
            conn, _ = clients.pop(nick)
            try: conn.close()
            except: pass
            for other, (c, _) in clients.items():
                try:
                    c.sendall((f"SYSTEM: User {nick} left.\n").encode(ENC))
                except:
                    pass

def handle_client(conn, addr):
    conn.sendall(b"SYSTEM: Welcome! Please register your nick with: NICK your_nick\n")
    nick = None
    buf = conn.makefile("r", encoding=ENC)

    try:
        while True:
            line = buf.readline()
            if not line:
                break
            line = line.strip()

            if not nick:
                if line.startswith("NICK "):
                    requested = line[5:].strip()
                    if not requested:
                        send_system(conn, "Invalid nick. Use: NICK your_nick")
                        continue

                    with lock:
                        if requested in clients:
                            send_system(conn, "ERROR: nick already in use. Choose another.")
                        else:
                            nick = requested
                            clients[nick] = (conn, addr)
                            send_system(conn, f"New User. Welcome, {nick}!")
                            for other, (c, _) in clients.items():
                                if other != nick:
                                    try:
                                        c.sendall((f"SYSTEM: User {nick} joined.\n").encode(ENC))
                                    except:
                                        pass
                else:
                    send_system(conn, "Please register first with: NICK your_nick")
                continue

            if line.upper() == "WHO":
                with lock:
                    names = ", ".join(clients.keys())
                send_system(conn, f"Connected users: {names}")
                continue

            if line.upper() == "QUIT":
                send_system(conn, "Goodbye!")
                break

            if line.startswith("MSG "):
                body = line[4:].strip()
                if body.startswith("@"):
                    parts = body.split(" ", 1)
                    target = parts[0][1:]
                    text = parts[1] if len(parts) > 1 else ""
                    ok = send_direct(nick, target, text)
                    if not ok:
                        send_system(conn, f"ERROR: user {target} not found.")
                    continue

                broadcast(nick, body)
                continue

            send_system(conn, "Unknown command. Use: MSG, WHO, QUIT")

    finally:
        if nick:
            _remove_client(nick)
        try:
            conn.close()
        except:
            pass

def start():
    print(f"Starting server on {HOST}:{PORT}...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)

    try:
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        s.close()

if __name__ == "__main__":
    start()
