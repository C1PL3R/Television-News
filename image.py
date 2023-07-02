from PIL import Image
from customtkinter import CTkImage

image_menu_burger = CTkImage(light_image=Image.open("Image/menu_icon.png"),
                                  dark_image=Image.open("Image/menu_icon.png"),
                                  size=(20, 20))

image_close_menu = CTkImage(light_image=Image.open("Image/close.png"),
                                  dark_image=Image.open("Image/close.png"),
                                  size=(20, 20))

header_news1_img = CTkImage(light_image=Image.open("Image/header_news1.png"),
                                  dark_image=Image.open("Image/header_news1.png"),
                                  size=(320, 200))

news1_img = CTkImage(light_image=Image.open("Image/news1.png"),
                                  dark_image=Image.open("Image/news1.png"),
                                  size=(220, 140))

news2_img = CTkImage(light_image=Image.open("Image/news2.png"),
                                  dark_image=Image.open("Image/news2.png"),
                                  size=(220, 140))