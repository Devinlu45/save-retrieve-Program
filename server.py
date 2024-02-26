import socket
from pymongo import MongoClient
from gridfs import GridFS

cluster = MongoClient("mongodb+srv://Devinlu1:Persona4golden@cluster0.7qs6qve.mongodb.net/")

db = cluster["FileStorage"]

collection = db["Backup"]

created_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 7245
created_socket.bind((host, port))
created_socket.listen(1)

client_socket, addr = created_socket.accept()

num1 = client_socket.recv(1024).decode()
split1, split2, split3 = num1.split(',')
fs = GridFS(db)
def retrieveFile(location, fileName):
    data_retrieve = db.fs.files.find_one({'filename': fileName})
    download_location = location + fileName
    data_output = fs.get(data_retrieve['_id']).read()
    the_output = open(download_location, "wb")
    the_output.write(data_output)

def saveFile(fileName):
    file_data = open(fileName, "rb")
    data_chunks = file_data.read()
    fs.put(data_chunks, filename = fileName)

if split3.upper() == "SAVE":
    saveFile(split2)
else:
    retrieveFile(split1, split2)
client_socket.close()