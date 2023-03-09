from .functions_tests import push, erase, add_to_history, show_history

expression = ""
history = []

def test_compute_functions():
    global expression
    equation = ""

    expression, equation = push(button=5, expression=expression, equation=equation)
    print(expression)
    print(equation)

    expression, equation = push(button="+", expression=expression, equation=equation)
    print(expression)
    print(equation)

    expression, equation = push(button=5, expression=expression, equation=equation)
    print(expression)
    print(equation)

    expression, equation = push(button="=", expression=expression, equation=equation)
    print(expression)
    print(equation)

    assert equation == "10"
    assert expression == "10"


def test_compute_functions_wrong_compute():
    global expression
    equation = ""

    expression, equation = push(button="+", expression=expression, equation=equation)
    print(expression)
    print(equation)

    expression, equation = push(button="+", expression=expression, equation=equation)
    print(expression)
    print(equation)

    expression, equation = push(button="=", expression=expression, equation=equation)
    print(expression)
    print(equation)

    assert equation == "Erreur"
    assert expression == ""


def test_erase_functions():
    global expression
    expression = "10"
    equation = "10"

    expression, equation = erase(expression=expression, equation=equation)
    print(expression)
    print(equation)

    assert equation == ""
    assert expression == ""


def test_add_to_history_function():
    global expression
    global history
    expression = "10 + 5"
    totale = "15"

    history = add_to_history(expression, totale, history)
    print(history)

    assert history == ["10 + 5 = 15"]

    expression = "18 - 7"
    totale = "11"

    history = add_to_history(expression, totale, history)
    print(history)

    assert history == ['10 + 5 = 15', '18 - 7 = 11']

    expression = "15 * 2"
    totale = "30"

    history = add_to_history(expression, totale, history)
    print(history)

    assert history == ['10 + 5 = 15', '18 - 7 = 11', '15 * 2 = 30']

    expression = "10 / 5"
    totale = "2"

    history = add_to_history(expression, totale, history)
    print(history)

    assert history == ['10 + 5 = 15', '18 - 7 = 11', '15 * 2 = 30', '10 / 5 = 2']
    history = []


def test_show_history():
    global expression
    global history

    expression = "10 + 5"
    totale = "15"
    history = add_to_history(expression, totale, history)

    expression = "18 - 7"
    totale = "11"
    history = add_to_history(expression, totale, history)

    expression = "15 * 2"
    totale = "30"
    history = add_to_history(expression, totale, history)

    expression = "10 / 5"
    totale = "2"
    history = add_to_history(expression, totale, history)

    list_history = show_history(history)
    print(list_history)

    assert list_history == '10 + 5 = 15\n18 - 7 = 11\n15 * 2 = 30\n10 / 5 = 2'
