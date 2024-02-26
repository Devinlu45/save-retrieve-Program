import socket

client_socket = socket.socket()
host = socket.gethostname()
port = 7245
client_socket.connect((host, port))

def retrieveData():
    num1 = "retrieve/TifaandCloud.png,TifaandCloud.png,retrieve"
    client_socket.send(num1.encode())

def saveData():
    name = "save,ff7_rebirth_party.jpg,save"
    client_socket.send(name.encode())

retrieveData()

client_socket.close()

