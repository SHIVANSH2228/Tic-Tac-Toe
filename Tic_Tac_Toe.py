from tkinter import *
from tkinter import messagebox, Button

# creating main screen
root = Tk()
root.title("Tic-Tac-Toe")
root.resizable(width=False, height=False)

# defining important variable
chance = True
counting = 0
winner = False
sent = "Winner is "


# making functions

def disable():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def win():
    global winner
    global entry, sent, entry2
    # checking for x
    if b1["text"] == 'X' and b2["text"] == 'X' and b3["text"] == 'X':
        b1.config(bg='#FA8072')
        b2.config(bg='#FA8072')
        b3.config(bg='#FA8072')
        winner = True
        messagebox.showinfo("Tic Tac Toe", sent+ entry.get())
        disable()

    elif b4["text"] == 'X' and b5["text"] == 'X' and b6["text"] == 'X':
        b4.config(bg='#FA8072')
        b5.config(bg='#FA8072')
        b6.config(bg='#FA8072')
        winner = True
        messagebox.showinfo("Tic-tac-Toe", sent+ entry.get())
        disable()

    elif b7["text"] == 'X' and b8["text"] == 'X' and b9["text"] == 'X':
        b7.config(bg='#FA8072')
        b8.config(bg='#FA8072')
        b9.config(bg='#FA8072')
        winner = True
        messagebox.showinfo("Tic-tac-Toe", sent+ entry.get())
        disable()

    elif b1["text"] == 'X' and b4["text"] == 'X' and b7["text"] == 'X':
        b1.config(bg='#FA8072')
        b4.config(bg='#FA8072')
        b7.config(bg='#FA8072')
        winner = True
        messagebox.showinfo("Tic-tac-Toe", sent+ entry.get())
        disable()

    elif b2["text"] == 'X' and b5["text"] == 'X' and b8["text"] == 'X':
        b2.config(bg='#FA8072')
        b5.config(bg='#FA8072')
        b8.config(bg='#FA8072')
        winner = True
        messagebox.showinfo("Tic-tac-Toe", sent+ entry.get())
        disable()

    elif b3["text"] == 'X' and b6["text"] == 'X' and b9["text"] == 'X':
        b3.config(bg='#FA8072')
        b6.config(bg='#FA8072')
        b9.config(bg='#FA8072')
        winner = True
        messagebox.showinfo("Tic-tac-Toe", sent+ entry.get())
        disable()

    elif b1["text"] == 'X' and b5["text"] == 'X' and b9["text"] == 'X':
        b1.config(bg='#FA8072')
        b5.config(bg='#FA8072')
        b9.config(bg='#FA8072')
        winner = True
        messagebox.showinfo("Tic-tac-Toe", sent+ entry.get())
        disable()

    elif b3["text"] == 'X' and b5["text"] == 'X' and b7["text"] == 'X':
        b3.config(bg='#FA8072')
        b5.config(bg='#FA8072')
        b7.config(bg='#FA8072')
        winner = True
        messagebox.showinfo("Tic-tac-Toe", sent+ entry.get())
        disable()

    # checking for o
    elif b1["text"] == 'O' and b2["text"] == 'O' and b3["text"] == 'O':
        b1.config(bg='#FA8072')
        b2.config(bg='#FA8072')
        b3.config(bg='#FA8072')
        winner = True
        messagebox.showinfo("Tic-tac-Toe", sent+ entry2.get())
        disable()

    elif b4["text"] == 'O' and b5["text"] == 'O' and b6["text"] == 'O':
        b4.config(bg='#FA8072')
        b5.config(bg='#FA8072')
        b6.config(bg='#FA8072')
        winner = True
        messagebox.showinfo("Tic-tac-Toe", sent+ entry2.get())
        disable()

    elif b7["text"] == 'O' and b8["text"] == 'O' and b9["text"] == 'O':
        b7.config(bg='#FA8072')
        b8.config(bg='#FA8072')
        b9.config(bg='#FA8072')
        winner = True
        messagebox.showinfo("Tic-tac-Toe", sent+ entry2.get())
        disable()

    elif b1["text"] == 'O' and b4["text"] == 'O' and b7["text"] == 'O':
        b1.config(bg='#FA8072')
        b4.config(bg='#FA8072')
        b7.config(bg='#FA8072')
        winner = True
        messagebox.showinfo("Tic-tac-Toe", sent+ entry2.get())
        disable()

    elif b2["text"] == 'O' and b5["text"] == 'O' and b8["text"] == 'O':
        b2.config(bg='#FA8072')
        b5.config(bg='#FA8072')
        b8.config(bg='#FA8072')
        winner = True
        messagebox.showinfo("Tic-tac-Toe", sent+entry2.get())
        disable()

    elif b3["text"] == 'O' and b6["text"] == 'O' and b9["text"] == 'O':
        b3.config(bg='#FA8072')
        b6.config(bg='#FA8072')
        b9.config(bg='#FA8072')
        winner = True
        messagebox.showinfo("Tic-tac-Toe", sent+ entry2.get())
        disable()

    elif b1["text"] == 'O' and b5["text"] == 'O' and b9["text"] == 'O':
        b1.config(bg='#FA8072')
        b5.config(bg='#FA8072')
        b9.config(bg='#FA8072')
        winner = True
        messagebox.showinfo("Tic-tac-Toe", sent+ entry2.get())
        disable()

    elif b3["text"] == 'O' and b5["text"] == 'O' and b7["text"] == 'O':
        b3.config(bg='#FA8072')
        b5.config(bg='#FA8072')
        b7.config(bg='#FA8072')
        winner = True
        messagebox.showinfo("Tic-tac-Toe", sent+ entry2.get())
        disable()
    # checking for tie
    elif counting == 9 and winner == False:
        messagebox.showinfo("Tic-tac-Toe", "It is a TIE!!")
        disable()


def click(b):
    global chance, counting

    if b["text"] == "" and chance == True:
        b["text"] = "X"
        chance = False
        counting += 1
        win()

    elif b["text"] == "" and chance == False:
        b["text"] = "O"
        chance = True
        counting += 1
        win()
    else:
        messagebox.showerror("Tic-Tac-Toe", "Box already selected.\nSelect a different box")


def reset():
    global counting, chance
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    counting = 0
    chance = True

    # creating buttons
    b1 = Button(root, text="", height=6, width=12, bg="SystemButtonFace", command=lambda: click(b1))
    b2 = Button(root, text="", height=6, width=12, bg="SystemButtonFace", command=lambda: click(b2))
    b3 = Button(root, text="", height=6, width=12, bg="SystemButtonFace", command=lambda: click(b3))

    b4 = Button(root, text="", height=6, width=12, bg="SystemButtonFace", command=lambda: click(b4))
    b5 = Button(root, text="", height=6, width=12, bg="SystemButtonFace", command=lambda: click(b5))
    b6 = Button(root, text="", height=6, width=12, bg="SystemButtonFace", command=lambda: click(b6))

    b7 = Button(root, text="", height=6, width=12, bg="SystemButtonFace", command=lambda: click(b7))
    b8 = Button(root, text="", height=6, width=12, bg="SystemButtonFace", command=lambda: click(b8))
    b9 = Button(root, text="", height=6, width=12, bg="SystemButtonFace", command=lambda: click(b9))

    # adding buttons to grid
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


# creating input for name
entry = Entry(root)
entry.grid(row=4, column=4)
entry2 = Entry(root)
entry2.grid(row=5, column=4)
# creating label for input
label = Label(root, text="Player 1")
label.grid(row=4, column=3)
label = Label(root, text="Player 2")
label.grid(row=5, column=3)

# creating menu
mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu, tearoff=False)
mymenu.add_cascade(label="Options", menu=submenu)
submenu.add_command(label="New Game", command=reset)
submenu.add_separator()
submenu.add_command(label="Exit", command=root.quit)

reset()
root.mainloop()
