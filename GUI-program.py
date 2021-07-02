import socket
import time
import threading
from tkinter import *

root=Tk()
root.geometry("300x500")
root.config(bg="white")

def func():
    t=threading.Thread(target=recv)
    t.start()

def recv():
    listensocket=socket.socket()
    port=3050
    maxconnection=99
    ip=socket.gethostname()
    print(ip)
    
    listensocket.bind(('', port))
    listensocket.listen(maxconnection)
    (clientsocket, address) = listensocket.accept()
    
    while True:
          sendermessage = clientsocket.recv(1024).decode()
          if not sendermessage == "":
              time.sleep(5)
              listbx.insert(0,"CLient: ", +sendermessage)

def threadsedmessagec():
    

startchatimage = PhotoImage(file='start.png')

buttons=Button(root, image = startchatimage, command=func, borderwidth=0)
buttons.place(x=90,y=10)

message = StringVar()
messagebox = Entry(root, textvariable = message, font = ('arial', 10, 'normal'), border = 2, width = 30)
messgebox.place(x=15, y=400)

sendmessaging=PhotoImage(file='send.png')

sendmessagebutton = Button(root, image=sendmessaging, command = threadsendmessage, borderwidth = 0)
sendmessahebutton.place(x=300,y=400)

lstbx = ListBox(root, height=30, width=50)
lstbx.place(x=20,y=60)

root.mainloop()












