from sys import platform
import matplotlib
from tkinter import Tk, StringVar, Label, messagebox

# Globals variables

BLACK = "#101419"
WHITE = "#FFF"
BLUE = "#476C9B"
RED = "#984447"

expression = ""
history = []

def push(button: int):
    """ Add value to equation
    """

    if button == "=":
        compute()
        return

    global expression
    if button == "+" or button == "-" or button == "*" or button == "/":
        if expression == "":
            return
    
    expression += str(button)
    equation.set(expression)

def compute():
    """ Compute the equation 
    """

    global expression
    try:
        total = str(eval(expression))
        add_to_history(expression, total)
        equation.set(total)
        expression = total
    except Exception as err:
        print(err)
        equation.set("Erreur")
        expression = ""

def erase():
    """ Erase the current equation
    """
    
    global expression
    expression = ""
    equation.set("")


def add_to_history(expression, result):
    """ Add recent equation to history
    """
    
    global history
    history.append(f"{expression} = {result}")


def show_history():
    """ Display the history
    """
    
    global history
    if not history:
        messagebox.showinfo('Historique', 'L\'historique est vide.')
    else:
        history_str = '\n'.join(history)
        messagebox.showinfo('Historique', history_str)


if __name__ == "__main__":

    print("Starting up...")
    interface = Tk()

    # Background color
    interface.configure(background=BLACK)

    # Title
    interface.title("Calculatrice")

    # Size
    print(f"Version : {platform}")
    if platform == "linux" or platform == "linux2":
        # Linux
        interface.geometry("575x725")
    elif platform == "win32":
        # Windows
        interface.geometry("325x475")

    # Store content
    equation = StringVar()

    # Result box
    result = Label(interface, bg=BLACK, fg=WHITE, textvariable=equation, height="2", font="Arial")
    result.grid(columnspan=4)

    # Buttons
    buttons = [7, 8, 9, "*", 4, 5, 6, "-", 1, 2, 3, "+", 0, ".", "/", "="]

    line = 1
    column = 0
    isHistoricSet = False

    for button in buttons:
        # Create a button
        b = Label(interface, text=str(button), bg=BLUE, fg=WHITE, height=5, width=8)
        # Make text clickable
        b.bind("<Button-1>", lambda e, button=button: push(button))

        b.grid(row=line, column=column)

        column += 1
        if column == 4:
            # Place button History before the first return at the line
            if not isHistoricSet :
                b = Label(interface, text="Historique", bg=BLUE, fg=WHITE, height=5, width=8)
                b.bind("<Button-1>", lambda e: show_history())
                b.grid(row=line, column=column)
                isHistoricSet = True
            column = 0
            line += 1

    # Place button erase at the end
    b = Label(interface, text="Effacer", bg=RED, fg=WHITE, height=4, width=34)
    b.bind("<Button-1>", lambda e: erase())
    b.grid(columnspan=4)

    # Run application
    interface.mainloop()
    print("Exiting...")
