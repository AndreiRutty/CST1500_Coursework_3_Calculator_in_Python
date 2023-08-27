from PIL import Image, ImageTk

#This file is responsible to store all style related settings and images for the Calculator UI

# Colors
BLACK = '#18202a'
WHITE = '#EEEEEE'
GREY = '#36474f'
LIGHT_GREY = '#EAEAEA'
LIGHTER_GREY = '#F5F5F5'
ORANGE = '#F86334'
HOVER_COLOR="#121820"
HOVER_COLOR_LIGHT = "#DDDDDD"

# Font styles for different labels
font_family="Lato"
title_font_size = 25
formula_font_size = 22
result_font_size = 30
button_font_size = 22
number_font_size = 25

# Grid Layout
# Setting the total number of rows and column in the grid
column_num = 4
row_num = 11

# Button Grid
button_grid_row_num = 7
button_grid_column_num = 5

# Padding
button_grid_spacing = 0.5
height_padding = 20
edge_padding = 20
output_label_padding = 30

# Images Path
images_path = {
	"equal-sign": "./Images/equal.png",
	"plus": "./Images/plus.png",
	"minus": "./Images/minus.png",
	"multiply": "./Images/times.png",
	"divide": "./Images/division.png",
	"light-mode": "./Images/light_mode.png",
	"dark-mode": "./Images/dark_mode.png",
	"back": "./Images/back.png",
	"pi": "./Images/pi.png",
	"pi-light": "./Images/pi_light.png",
	"square-root": "./Images/square_root.png",
	"square-root-light": "./Images/square_root_light.png",
	"clear": "./Images/c.png",
	"round": "./Images/round.png"
}

# Images reference
images = {
	"equal-sign": Image.open(images_path["equal-sign"]),
	"plus": Image.open(images_path["plus"]),
	"minus": Image.open(images_path["minus"]),
	"multiply": Image.open(images_path["multiply"]),
	"divide": Image.open(images_path["divide"]),
	"light-mode": Image.open(images_path["light-mode"]),
	"dark-mode": Image.open(images_path["dark-mode"]),
	"back": Image.open(images_path["back"]),
	"pi": Image.open(images_path["pi"]),
	"pi-light": Image.open(images_path["pi-light"]),
	"square-root": Image.open(images_path["square-root"]),
	"square-root-light": Image.open(images_path["square-root-light"]),
	"clear": Image.open(images_path["clear"]),
	"round": Image.open(images_path["round"])
}

# Button size
button_size = (70,70)
button_size_2 = (60,60)
button_size_3 = (30, 30)
button_size_4 = (40, 40)
toggle_button_size = (40,40)
