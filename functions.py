import math
import threading
import graph
from tkinter import messagebox

# class MathFunction defines all the mathematical operations of the calculator
class MathFunction:
    def __init__(self, result_string, formula_string):
        # List containing the digits for the number the user inputs
        self.displayed_number = []
        # List containing the full mathematical operation
        self.full_operation = []
        # Reference to the result_string string variable of the calculator ui
        self.result_string = result_string
        # Reference to the formula_string string variable of the calculator ui
        self.formula_string = formula_string

    # Function that will display the value ,passed by the parameter value , on the calculator screen when numbered buttons are pressed
    def number_press(self, value):
        # Appending the value to the list of digit
        self.displayed_number.append(str(value))
        # Joining the digits together to the full number
        full_number = ''.join(self.displayed_number)
        # Setting the full number to the result_string string variable
        self.result_string.set(full_number)

    # Function that will display the mathematical operator, provided by value, on the calculator screen when operator button is pressed
    # And will also evaluate the expression given
    def operator_press(self, value):
        # Getting the value of result_string string varibale
        current_number = self.result_string.get()

        # Checking if current_number is not an empty string
        if current_number:
            # If it is not, 
            # Add the number to the full operation list
            self.full_operation.append(current_number)

            # Checking if the value provided is not the equal sign
            if value != '=':
                # If it is not, 
                # Append the value to the full operation list
                self.full_operation.append(value)
                # Clearing the digit list to form the next number
                self.displayed_number.clear()
                # Clearing the result_string string variable
                self.result_string.set('')
                # Joining the content of the full operation list and setting to the formula_string string variable
                self.formula_string.set(' '.join(self.full_operation))
            else:
                # It is the equal sign
                # Joining the element of the full operation list together
                expression = ''.join(self.full_operation)

                # Create a thread for evaluating the expression provided by the expression variable
                thread = threading.Thread(target=self.evaluate_expression, args=(expression,))
                # Setting Daemon mode to true
                thread.setDaemon(True)
                # Starting the thread
                thread.start()

                # Clearing the full operation list, for the next expression
                self.full_operation.clear()
                # Setting the formula_string String variable to the expression
                self.formula_string.set(expression)

    # Function that will clear the expression and result
    def clear(self):
        # Setting the result_string string variable to 0
        self.result_string.set("0")
        # Setting the formula_string string variable to an empty string
        self.formula_string.set("")
        # Clearing the digit list 
        self.displayed_number.clear()
        # Cearing the full operation list
        self.full_operation.clear()

    # Function that will rounded off the answer to the expression to 3 decimal places
    def round_number(self):
        # Getting the value of the result_string string variable
        current_number = self.result_string.get()

        # Checking if current is not an empty string
        if current_number:
            # It is not, round the number to 3 decimal places
            rounded_number = round(float(current_number), 3)
            # Setting this number to the digit list
            self.displayed_number = [str(rounded_number)]
            # Setting this number to the result_string string variable
            self.result_string.set(rounded_number)

    # Function that will evaluate the expression provided by the parameter expression
    def evaluate_expression(self, expression):
        # Replacing math operation syntax with the Python mathematical syntax

        # Replacing sin with math.sin 
        expression = expression.replace("sin", "math.sin")
        # Replacing cos with math.cos 
        expression = expression.replace("cos", "math.cos")
        # Replacing tan with math.tan 
        expression = expression.replace("tan", "math.tan")
        # Replacing ^ with ** 
        expression = expression.replace("^", "**")
        # Replacing sqrt with math.sqrt 
        expression = expression.replace("sqrt", "math.sqrt")
        # Replacing PI with math.pi 
        expression = expression.replace("PI", "math.pi")
        # Replacing e with math.e 
        expression = expression.replace("e", "math.e")

        # Checking for ln and log
        # If the expression contains ln 
        if "ln" in expression:
            # Replacing ln with math.log
            expression = expression.replace("ln", "math.log")
        else:
            # If the expression contains log, replace log with log10
            expression = expression.replace("log", "math.log10")

        # This prevents that the function replaces ln with math.math.log10

        # Graph
        # Checking if the expression contains "x"
        if "x" in expression:
            try:
                # If it does, draw the graph of the expression
                graph.draw_graph(expression)
            except SyntaxError:
                messagebox.showerror(title="Error", message="There is a Syntax Error in your graph formula")

        else:
            # Error Handling - catching Syntax Error
            try:
                # Else we evaluate the answer of the expression
                result = eval(expression)
            except SyntaxError:
                messagebox.showerror(title="Error", message="There is a Syntax Error in your formula")
            else:
                 # Checking if the result is of type float
                if isinstance(result, float):
                    # Checks if the result has no fractional part, that is it is an integer
                    if result.is_integer():
                        # Converts the float number to an integer
                        result = int(result)
                    else:
                        # Letting the answer as it is
                        result = result

                # Setting the answer to the digit list
                self.displayed_number = [str(result)]
                # Setting the answer to the result_string string varible to be displayed on the ui
                self.result_string.set(result)
