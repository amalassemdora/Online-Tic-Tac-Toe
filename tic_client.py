
from tkinter import *
from tkinter import messagebox

from socket import * 

# global variables
player = 0 # indicate which player has to play
turn=1 # indicate which turn used to show if we finish game or not 
# functions
# check
def check():
	global turn
	turn +=1
	
	if ((btn1["text"]== btn2["text"] and btn2["text"]== btn3["text"] and btn1["text"] =="O") or (btn1["text"]== btn2["text"] and btn2["text"]== btn3["text"] and btn1["text"] =="X")):
		win(btn1["text"])

	if ((btn4["text"]== btn5["text"] and btn5["text"]== btn6["text"] and btn4["text"] =="O") or (btn4["text"]== btn5["text"] and btn5["text"]== btn6["text"] and btn4["text"] =="X")):
		win(btn4["text"])

	if ((btn7["text"]== btn8["text"] and btn8["text"]== btn9["text"] and btn7["text"] =="O") or (btn7["text"]== btn8["text"] and btn8["text"]== btn9["text"] and btn7["text"] =="X")):
		win(btn7["text"])

	if ((btn1["text"]== btn4["text"] and btn4["text"]== btn7["text"] and btn1["text"] =="O") or (btn1["text"]== btn4["text"] and btn4["text"]== btn7["text"] and btn1["text"] =="X")):
		win(btn1["text"])

	if ((btn2["text"]== btn5["text"] and btn5["text"]== btn8["text"] and btn2["text"] =="O") or (btn2["text"]== btn5["text"] and btn5["text"]== btn8["text"] and btn2["text"] =="X")):
		win(btn2["text"])

	if ((btn3["text"]== btn6["text"] and btn6["text"]== btn9["text"] and btn3["text"] =="O") or (btn3["text"]== btn6["text"] and btn6["text"]== btn9["text"] and btn3["text"] =="X")):
		win(btn3["text"])

	if ((btn1["text"]== btn5["text"] and btn5["text"]== btn9["text"] and btn1["text"] =="O") or (btn1["text"]== btn5["text"] and btn5["text"]== btn9["text"] and btn1["text"] =="X")):
		win(btn1["text"])

	if ((btn3["text"] == btn5["text"] and btn5["text"]== btn7["text"] and btn3["text"] =="O") or (btn3["text"]== btn5["text"] and btn5["text"]== btn7["text"] and btn3["text"] =="X")):
		win(btn3["text"])
		

	
def win(player):
	messagebox.showinfo("win", player +" is win")
	wind.destroy()

#fun1
def clicked1():
	global player
	if(btn1["text"]==" "):
		if(player==1):
			player=2
			btn1["text"] = "X"
			sendPlay(1)	
		check()

#fun2
def clicked2():
	global player
	if(btn2["text"]==" "):
		if(player==1):
			player=2
			btn2["text"] = "X"
			sendPlay(2)	
		
		check()

#fun3
def clicked3():
	global player
	if(btn3["text"]==" "):
		if(player==1):
			player=2
			btn3["text"] = "X"
			sendPlay(3)	
		
		check()

#fun4
def clicked4():
	global player
	if(btn4["text"]==" "):
		if(player==1):
			player=2
			btn4["text"] = "X"
			sendPlay(4)	
		
		check()

#fun5
def clicked5():
	global player
	if(btn5["text"]==" "):
		if(player==1):
			player=2
			btn5["text"] = "X"
			sendPlay(5)	
		check()

#fun6
def clicked6():
	global player
	if(btn6["text"]==" "):
		if(player==1):
			player=2
			btn6["text"] = "X"
			sendPlay(6)	
	    
		check()

#fun7
def clicked7():
	global player
	if(btn7["text"]==" "):
		if(player==1):
			player=2
			btn7["text"] = "X"
			sendPlay(7)	
	    
		check()

#fun8
def clicked8():
	global player
	if(btn8["text"]==" "):
		if(player==1):
			player=2
			btn8["text"] = "X"
			sendPlay(8)
	    
		check()

#fun9
def clicked9():
	global player
	if(btn9["text"]==" "):
		if(player==1):
			player=2
			btn9["text"] = "X"
			sendPlay(9)	
		check()

def sendPlay(n):
    n = str(n)
    n = n.encode()
    soc.send(n)

def handlePlay(n):
    global player
    n = n - 1 
    butList[n]["text"] = "O"
    player = 1 


def applayPlay(p):
    p = p.decode()
    p = int(p)
    handlePlay(p)


#window
wind = Tk()
wind.title("tic tac toe") # title
wind.geometry("400x300")  # size

# labels one and two players
lb1 = Label(wind,text="player1:X   " ,font=('Helvetiica',15))
lb1.grid(row = 0,column=0)

# buttons
butList = list() 
#button1
btn1=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font='Helvetiica',command=clicked1)
btn1.grid(row=0,column=1)
#button2
btn2=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font='Helvetiica',command=clicked2)
btn2.grid(row=0,column=2)
#button3
btn3=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font='Helvetiica',command=clicked3)
btn3.grid(row=0,column=3)
#button4
btn4=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font='Helvetiica',command=clicked4)
btn4.grid(row=1,column=1)
#button5
btn5=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font='Helvetiica',command=clicked5)
btn5.grid(row=1,column=2)
#button6
btn6=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font='Helvetiica',command=clicked6)
btn6.grid(row=1,column=3)
#button7
btn7=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font='Helvetiica',command=clicked7)
btn7.grid(row=2,column=1)
#button8
btn8=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font='Helvetiica',command=clicked8)
btn8.grid(row=2,column=2)
#button9
btn9=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font='Helvetiica',command=clicked9)
btn9.grid(row=2,column=3)

butList.append(btn1)
butList.append(btn2)
butList.append(btn3)
butList.append(btn4)
butList.append(btn5)
butList.append(btn6)
butList.append(btn7)
butList.append(btn8)
butList.append(btn9)

# session with server 

soc = socket(AF_INET , SOCK_STREAM)

soc.connect(("127.0.0.1" , 6002) )
from threading import Thread

def rec():
    while True:
      p = soc.recv(10)
      applayPlay(p)


t = Thread(target = rec )
t.start()



#to run the window
wind.mainloop()



    