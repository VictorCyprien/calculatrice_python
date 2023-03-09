from tkinter import StringVar

def push(button, expression, equation: str):
    """ Add value to equation
    """
    
    if button == "=":
        expression, equation = compute(expression, equation)
        return expression, equation
    
    expression += str(button)
    equation += str(button)
    return expression, equation


def compute(expression, equation):
    """ Compute the equation 
    """

    try:
        total = str(eval(expression))
        equation = total
        expression = total
    except Exception as err:
        print(err)
        equation = "Erreur"
        expression = ""

    return expression, equation


def erase(expression, equation):
    """ Erase the current equation
    """
    
    expression = ""
    equation = ""
    return expression, equation


def add_to_history(expression, result, history):
    """ Add recent equation to history
    """
    
    history.append(f"{expression} = {result}")
    return history


def show_history(history):
    """ Display the history
    """
    if not history:
        return "L'historique est vide."
    else:
        history_str = '\n'.join(history)
        return history_str