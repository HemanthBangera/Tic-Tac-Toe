from tkinter import *
import random

def next_turn(row,column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text']=player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=players[0]+" wins")

            elif check_winner() == "Tie":
                label.config(text="Tie")

        else:

            buttons[row][column]['text'] = players[1]

            if check_winner() is False:
                player = players[0]
                label.config(text=players[0] + " turn")

            elif check_winner() is True:
                label.config(text=players[1] + " wins")

            elif check_winner() == "Tie":
                label.config(text="Tie")

def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False

    else:
        return True
def check_winner():
    global player
    for row in range(3):

            if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
                label.config(text=player+" wins")
                buttons[row][0].config(bg='green')
                buttons[row][1].config(bg='green')
                buttons[row][2].config(bg='green')

                return True


    for column in range(3):
            if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
                label.config(text=player+" wins")
                buttons[0][column].config(bg='green')
                buttons[1][column].config(bg='green')
                buttons[2][column].config(bg='green')
                return True



    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        label.config(text=player + " wins")
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        label.config(text=player + " wins")
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    return False




def new_game():
    global player

    label.config(text=player+" turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column]['text'] = ""
            buttons[row][column].config(bg="#522908")



window = Tk()


window.title("Tic-Tac-Toe Game")
players = ['x','o']
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label1 = Label(window, text="Tic-Tac-Toe",font=("Ink free",20),bg="yellow", width = 16)
label1.pack()
label = Label(window, text=player+" turn",font=('Ink free', 20),bg="yellow", width = 16)
label.pack(side="top")

reset_button = Button(window,text="Restart", font=('Ink free', 20), command=new_game, width=16, bg="light yellow")
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('Consolas', 20), width=5, height=2,bg="#522908",
                                     command=lambda row= row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row, column=column)



window.mainloop()

