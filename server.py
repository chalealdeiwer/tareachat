import socket   
import threading


host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen()
print(f"Server corriendo en {host}:{port}")


clients = []
usernames = []
#funcion de broadcast para enviar mensajes a los clientes
def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)

def disconnected_client(client):
    index = clients.index(client)
    username = usernames[index]
    broadcast(f"ChatBot: {username} se ha desconectado".encode('utf-8'), client)
    clients.remove(client)
    usernames.remove(username)
    client.close()
    print(f"{username} desconectado")

def handle_messages(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            disconnected_client(client)
            break


def receive_connections():
    while True:
        client, address = server.accept() 
        username = client.recv(1024).decode('utf-8')
        clients.append(client)
        usernames.append(username)
        print(f"{username} esta conectado desde {str(address)}")
        message = f"ChatBot: {username} ha entrado al chat!".encode("utf-8")
        broadcast(message, client)
        client.send("Se ha conectado al servidor".encode("utf-8"))
        thread = threading.Thread(target=handle_messages, args=(client,))
        thread.start()

receive_connections()