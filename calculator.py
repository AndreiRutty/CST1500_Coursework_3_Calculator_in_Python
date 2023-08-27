import customtkinter as ctk
import ui_config as ui
from widget import *
from functions import MathFunction

# class calculator which inherits from the customtkinter class
class Calculator(ctk.CTk):
	def __init__(self):
		super().__init__(fg_color=(LIGHT_GREY, GREY))

		# Boolean variable that dictates the state of the app
		self.is_dark = True  # Determines if the app is in dark mode or not

		# Setting an icon
		self.iconbitmap("") # This will remove the default icon

		# Calculator window default size
		self.geometry("450x800")

		self.title("Calculator")

		# Setting minimum and maximum size
		self.minsize(400, 600)
		self.maxsize(500, 900)

		# Calculator Layout 
		# row = 9 & column = 4(normal mode)
		# list(range(<num>)) - creates a list of a number within the range specified by <num>
		self.rowconfigure(list(range(ui.row_num)), weight = 1, uniform ='a')
		self.columnconfigure(list(range(ui.column_num)), weight = 1, uniform = 'a')

		# Calling calculator window
		self.window()

		# Looping the window
		self.mainloop()

	# Function that will display the calculator layout
	# Which includes the title, the formula and result textand the button grid
	# It separates the calculator into 2 halves
	# First half - title and formula and result text
	# Second half - button grid
	def window(self):

		# Data
		self.formula_text = ctk.StringVar(value="0")
		self.result_text = ctk.StringVar(value="0")

		# Calling MathFunction class to access the mathematical operations for the buttons
		self.function = MathFunction(self.result_text, self.formula_text)

		# Fonts Styles
		self.title_font = ctk.CTkFont(family=ui.font_family, size=ui.title_font_size, weight='bold')
		self.formula_font = ctk.CTkFont(family=ui.font_family, size=ui.formula_font_size)
		self.result_font = ctk.CTkFont(family=ui.font_family, size=ui.result_font_size, weight='bold')

		# Images
		self.theme_mode_image = ctk.CTkImage(light_image=ui.images["dark-mode"],dark_image=ui.images["light-mode"], size=ui.toggle_button_size)
		self.equal_sign_image = ctk.CTkImage(ui.images["equal-sign"], size= ui.button_size)
		self.plus_image = ctk.CTkImage(ui.images["plus"], size= ui.button_size)
		self.minus_image = ctk.CTkImage(ui.images["minus"], size= ui.button_size)
		self.multiply_image = ctk.CTkImage(ui.images["multiply"], size= ui.button_size)
		self.divide_image = ctk.CTkImage(ui.images["divide"], size= ui.button_size)
		self.back_image = ctk.CTkImage(ui.images["back"], size=ui.button_size_2)
		self.pi_image = ctk.CTkImage(light_image=ui.images["pi"], dark_image=ui.images["pi-light"], size=ui.button_size_3)
		self.square_root_image = ctk.CTkImage(light_image=ui.images["square-root"], dark_image=ui.images["square-root-light"], size=ui.button_size_3)
		self.clear_image = ctk.CTkImage(ui.images["clear"], size=ui.button_size_4)
		self.round_image = ctk.CTkImage(ui.images["round"], size=ui.button_size_4)

		# Header Start -------------------------------------------------------------------------------------------------------------------------

		# Adding the title to the left of the header
		self.title = Label(self, "Calculator", (ui.BLACK, ui.WHITE), self.title_font, pady=ui.height_padding)

		# Putting the title to the left of the header
		self.title.grid(row=0, column=0, columnspan=2)

		# Theme toggle mode Button
		# This button will change the theme of the app
		self.toggle_buttoon = ImageButton(self, 0, 3, self.theme_mode_image, self.toggle_theme, width=30)

		# Header End --------------------------------------------------------------------------------------------------------------------------


		# Output Window Start -----------------------------------------------------------------------------------------------------------------

		#Labels
		self.formula_label = OutputLabel(self, self.formula_text, (ui.BLACK, ui.WHITE), self.formula_font, 1, 0)
		self.result_label = OutputLabel(self, self.result_text, (ui.BLACK, ui.WHITE), self.result_font, 2, 0)

		# Line breaker - to give space between the output windows and the buttons grid
		self.line_breaker = Space(self, 10)
		self.line_breaker.grid(row=3, column=0, columnspan=4)

		# Output Window End --------------------------------------------------------------------------------------------------------------------


		# Button Grid Start --------------------------------------------------------------------------------------------------------------------

		self.button_grid = ctk.CTkFrame(self, fg_color=(LIGHTER_GREY, BLACK))

		# Configurating the grid layout (5x4)
		self.button_grid.rowconfigure(list(range(button_grid_row_num)), weight=1, uniform='a')
		self.button_grid.columnconfigure(list(range(button_grid_column_num)), weight=1, uniform='a')

		# Placing the 
		self.button_grid.grid(row=4, column=0, rowspan=ui.button_grid_row_num, columnspan=ui.column_num)


		# First Row
		Button(self.button_grid, "x", 0, 0, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("x"))
		Button(self.button_grid, "(-)", 0, 1, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("(-"))
		Button(self.button_grid, "%", 0, 2, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.operator_press("%"))
		ImageButton(self.button_grid, 0, 3, self.pi_image, lambda: self.function.number_press("PI"))
		Button(self.button_grid, "e", 0, 4, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("e"))

		# Second Row
		Button(self.button_grid, "sin", 1, 0, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("sin("))
		Button(self.button_grid, "cos", 1, 1, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("cos("))
		Button(self.button_grid, "tan", 1, 2, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("tan("))
		Button(self.button_grid, "ln", 1, 3, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("ln("))
		Button(self.button_grid, "log", 1, 4, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("log("))

		# # Third Row
		Button(self.button_grid, "X^2", 2, 0, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("^2"))
		ImageButton(self.button_grid, 2, 1, self.square_root_image, lambda: self.function.number_press("sqrt("))
		Button(self.button_grid, "X^y", 2, 2, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("^"))
		Button(self.button_grid, "(", 2, 3, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("("))
		Button(self.button_grid, ")", 2, 4, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press(")"))
		

		# Numbers
		# Fourth Row
		Button(self.button_grid, "7", 3, 0, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("7"))
		Button(self.button_grid, "8", 3, 1, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("8"))
		Button(self.button_grid, "9", 3, 2, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("9"))
		ImageButton(self.button_grid, 3, 3,self.round_image, lambda: self.function.round_number())
		ImageButton(self.button_grid, 3, 4, self.clear_image,lambda: self.function.clear())

		# Fifth Row
		Button(self.button_grid, "4", 4, 0, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("4"))
		Button(self.button_grid, "5", 4, 1, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("5"))
		Button(self.button_grid, "6", 4, 2, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("6"))

		# Sixth Row
		Button(self.button_grid, "1", 5, 0, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("1"))
		Button(self.button_grid, "2", 5, 1, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("2"))
		Button(self.button_grid, "3", 5, 2, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("3"))

		# Seventh Row
		LargeButton(self.button_grid, "0", 6, 0, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("0"))
		Button(self.button_grid, ".", 6, 2, (ui.LIGHTER_GREY, ui.BLACK), (ui.BLACK, ui.WHITE), lambda: self.function.number_press("."))

		# Math Operation Button
		ImageButton(self.button_grid, 4, 3, self.divide_image, lambda: self.function.operator_press("/"))
		ImageButton(self.button_grid, 5, 3, self.multiply_image, lambda: self.function.operator_press("*"))
		ImageButton(self.button_grid, 4, 4, self.minus_image, lambda: self.function.operator_press("-"))
		ImageButton(self.button_grid, 5, 4, self.plus_image, lambda: self.function.operator_press("+"))
		ImageButton(self.button_grid, 6, 4, self.equal_sign_image, lambda: self.function.operator_press("="))
		# Button Grid Ends ---------------------------------------------------------------------------------------------------------------------


	# Function that will change the state of the is_dark variable and change the theme of the app accordingly
	def toggle_theme(self):
		# Changing the state of is_dark
		self.is_dark = not self.is_dark

		# Setting the theme of the app accordingly
		ctk.set_appearance_mode("dark" if self.is_dark else "light")

if __name__ == '__main__':
	# Running the calculator program
	Calculator()