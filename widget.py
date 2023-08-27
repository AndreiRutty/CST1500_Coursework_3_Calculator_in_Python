import customtkinter as ctk
from ui_config import *

# This file is responsible to hold all the customtkinter widget needed for the calculator
# The custom widget are implemented as Classes

# Class Label - all text labels except for the formula and result text labels
class Label(ctk.CTkLabel):
	def __init__(self, master, text, text_color, font, **kwargs):
		super().__init__(master, text=text, text_color=text_color, font=font, **kwargs)

# Class OutputLabel - text label for only the formula and result text labels
class OutputLabel(ctk.CTkLabel):
	def __init__(self, master,output_text, text_color, font, row, column, **kwargs):
		super().__init__(master, text="", text_color=text_color, font=font, textvariable = output_text, **kwargs)

		self.grid(row=row, column=column, columnspan=column_num, sticky="E", padx=output_label_padding)

# Class Button - templates for all the button with text
class Button(ctk.CTkButton):
	def __init__(self, master, text, row, column, fg_color, text_color, command, **kwargs):
		super().__init__(master, 
			command=command,
			text=text,
			corner_radius=0,
			fg_color=fg_color,
			text_color=text_color,
			hover_color=(HOVER_COLOR_LIGHT, HOVER_COLOR),
			font=ctk.CTkFont(family=font_family, size=button_font_size),
			**kwargs)
		self.grid(row=row, column=column, sticky="NSEW", padx=button_grid_spacing)

# Class LargeButton - same as class MathButton but wider 
class LargeButton(ctk.CTkButton):
	def __init__(self, master, text, row, column, fg_color, text_color, command, **kwargs):
		super().__init__(master, 
			command=command,
			text=text,
			corner_radius=0,
			fg_color=fg_color,
			text_color=text_color,
			hover_color=(HOVER_COLOR_LIGHT, HOVER_COLOR),
			font=ctk.CTkFont(family=font_family, size=button_font_size),
			**kwargs)
		self.grid(row=row, column=column,columnspan=2, sticky="NSEW", padx=button_grid_spacing)

# Class ImageButton - Button with an Image and no text
class ImageButton(ctk.CTkButton):
	def __init__(self, master, row, column, image, command, **kwargs):
		super().__init__(master,
			command=command,
			text="",
			fg_color="transparent",
			hover_color=(HOVER_COLOR_LIGHT, HOVER_COLOR),
			image=image,
			**kwargs
			)

		self.grid(row=row, column=column, padx=button_grid_spacing, sticky="NSEW")

# Class Space - use as a separator between widgets
class Space(ctk.CTkLabel):
	def __init__(self, master, pady, **kwargs):
		super().__init__(master,text="", pady=pady, **kwargs)

