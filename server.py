import socket
import threading
#a way of allowing multiple pieces of codes to run, so one block doesn't have to wait for the other to finish
# so clients don't have to wait for each other before communicating with server

HEADER= 64
#defining byte size. no matter the size of the message, the header size is 64. the message will contain the size of the bytes

PORT= 5050
# one of the blank ports of your PC. 8080 is used for hhtp, etc. Read on it
#type ipconfig in cmd to get your computer's IP address (IP4 address). its fconfig for mac or something like that
SERVER= socket.gethostbyname(socket.gethostname())
#use this device's IP address. the above code is a way of getting this pc's IP address.
#if you want to run the server on a different P you may have to manually get itor request it.
# try print(SERVER)
ADDR= (SERVER, PORT)
#has to be in a tuple
FORMAT= 'utf-8'
DISCONNET_MESSAGE= "!DISCONNECTED" 

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#what type of address will we be looking for for this connection?, data is being streamed through the socket
server.bind(ADDR)
#we've bound this socket to this address. anything that tries to request this server will use the socket


#the functions will run concurrently for each client

def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')

    connected= True
    while connected: 
        msg_length= conn.recv(HEADER).decode(FORMAT)
            #how many bytes to rcv, message needs to be encode it into byte format so we decode it using utf format
        if msg_length: 
             msg_length= int(msg_length)
             msg= conn.recv(msg_length).decode(FORMAT)
             if msg== DISCONNET_MESSAGE:
                  connected= False

             print(f"[{addr}] {msg}")
             conn.send("Msg received".encode(FORMAT))
            
        conn.close()
        #close current connection   
#this thread handles individual connections and distributes them where they need to go
#f strings allow you to print variables in print lines

def start():
    server.listen()
    print("f[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr= server.accept()
        thread= threading.Thread(target= handle_client, args= (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
#this thread waits for and handles NEW connections to the server, stores the IP address and socket for communication with thing that connected


print("[STARTING] server is starting....")
start()






