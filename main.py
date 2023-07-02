import tkinter
from customtkinter import CTk, CTkFrame, CTkImage, CTkButton, set_appearance_mode, CTkLabel, CTkScrollableFrame, CTkOptionMenu
from PIL import Image
from utils import toggle_menu, open_url
from image import news1_img, image_close_menu, image_menu_burger, header_news1_img, news2_img

app = CTk()
app.title("Television News")
app.geometry("1000x600")
app.iconbitmap("Image/tn.ico")

app.resizable(False, False)
set_appearance_mode("light")

scrollable_frame = CTkScrollableFrame(app, width=1000, height=600, fg_color="transparent", corner_radius=0)
scrollable_frame.pack()

if "menu_not_burger" == "menu_not_burger":
    frame = CTkFrame(master=scrollable_frame, width=1000, height=50, fg_color="darkred", corner_radius=0)
    frame.pack()

    header_text = CTkLabel(master=frame, text="Television News", font=("Roboto", 27), text_color="white")
    header_text.place(x=400, y=8)

    button_menu = CTkButton(frame, fg_color="transparent", text="", command=lambda: toggle_menu(menu_frame, scrollable_frame), image=image_menu_burger, width=20, height=20)
    button_menu.place(x=50, y=10)


if "menu" == "menu":
    menu_frame = CTkFrame(app, corner_radius=0, fg_color="red", width=200, height=600)
    menu_frame.place(x=-200)

    def change_appearance_mode_event(new_appearance_mode: str):
        if new_appearance_mode == "Чорна":
            new_appearance_mode = "Dark"
            global color
            color = "black"
            print(color)
        elif new_appearance_mode == "Світла":
            new_appearance_mode = "Light"
            
            color = "#E6E6E6"
        else:
            pass
        set_appearance_mode(new_appearance_mode)

    appearance_mode_optionmenu = CTkOptionMenu(menu_frame, values=["Світла", "Чорна"], command=change_appearance_mode_event, anchor="center")
    appearance_mode_optionmenu.place(x=0, y=0)

    menu_text_1 = CTkButton(menu_frame, text="Про нас", fg_color="transparent", font=("", 20), width=50)
    menu_text_1.place(x=15, y=70)

    menu_text_2 = CTkButton(menu_frame, text="Контакти", fg_color="transparent", font=("", 20), width=60)
    menu_text_2.place(x=15, y=110)

    menu_text_3 = CTkButton(menu_frame, text="Служба підтримки", fg_color="transparent", font=("", 20), width=70, command=open_url)
    menu_text_3.place(x=15, y=150)

    menu_text_4 = CTkButton(menu_frame, text="Спорт", fg_color="transparent", font=("", 20), width=60)
    menu_text_4.place(x=15, y=190)

    button_menu = CTkButton(menu_frame, text="", fg_color="transparent", command=lambda: toggle_menu(menu_frame, scrollable_frame), image=image_close_menu, width=20, height=20)
    button_menu.place(x=150, y=10)


header_text2 = CTkLabel(scrollable_frame, text="Головні Новини станом на 10.12.2022", font=("", 27, "bold"), corner_radius=0)
header_text2.pack(pady=(20,0))


if "Header News Block 1" == "Header News Block 1":
    header_news1 = CTkFrame(scrollable_frame, width=950, height=510, fg_color="black", corner_radius=0)
    header_news1.pack(pady=(20,0), padx=(10,10))

    news1_image_label = CTkLabel(header_news1, image=header_news1_img, text="", corner_radius=0)
    news1_image_label.place(x=225)

    header_text_news1 = CTkLabel(header_news1, text="Інформація про вибухи в Львівській області: голова ОВА відреагував", font=("", 20, "bold"), text_color="white")
    header_text_news1.place(x=10, y=210)

    text_news1_a = CTkLabel(header_news1, text='У Львівській області 5 грудня під час масштабної повітряної тривоги не було вибухів.\n\nПро це повідомив голова Львівської ОВА Максим Козицький.\n\nДеякі телеграм-канали поширили неправдиву інформацію,\n\nначебто у Бориславі чули вибух. Офіційно заявляю: станом на 15:00 це не\n\nпідтвердилося', font=("", 18), text_color="white", justify="left")
    text_news1_a.place(x=10, y=260)


frame_2 = CTkFrame(scrollable_frame, width=800, height=70, fg_color="transparent", corner_radius=0)
frame_2.pack(pady=(0,0), padx=(0,0))

text_frame_2 = CTkLabel(frame_2, text="Стрічка Новин", font=("", 25, "bold"))
text_frame_2.place(x=300, y=20)

if "News Frame" == "News Frame":
    news_1_frame = CTkScrollableFrame(scrollable_frame, width=370, height=350, fg_color=color)
    news_1_frame.pack(side="left")

    news1_image = CTkLabel(news_1_frame, image=news1_img, text="")
    news1_image.pack()

    news1_header_text = CTkLabel(news_1_frame, text="Виведення російських військ \nта вступ України в НАТО", font=("", 20, "bold"))
    news1_header_text.pack(pady=10)

    text_news1 = "Він зазначив, що всі розмови \nз Росією треба розпочинати з \nвимог вивести війська \nз українських територій, а після \nзакінчення війни Україну потрібно \nприйняти в НАТО."

    news1_text = CTkLabel(news_1_frame, text=text_news1, font=("", 20), justify="left")
    news1_text.pack(side="left", pady=20)

    news_2_frame = CTkScrollableFrame(scrollable_frame, width=370, height=350, fg_color=color)
    news_2_frame.pack(side="right", padx=30, pady=0)

    news2_image = CTkLabel(news_2_frame, image=news2_img, text="")
    news2_image.pack(pady=(15,0), padx=10)

    news2_header_text = CTkLabel(news_2_frame, text="В Україні інфляція \nзменшила оберти", font=("", 20, "bold"))
    news2_header_text.pack(pady=10)

    text_news2 = "Базова інфляція, яка не \nвраховує короткострокові \nшокові зміни цін, в листопаді \nстановила 1,3% \nпорівняно із жовтнем, а від початку \nроку – 21,6%.\n\nВ Україні вперше від початку війни \nрівень споживчої \nінфляції сповільнився. \nПоказник зменшився від 26,6% \nу жовтні до 26,5% \nу листопаді у річному вимірі."

    news2_text = CTkLabel(news_2_frame, text=text_news2, font=("New Times", 20), justify="left")
    news2_text.pack(side="right", padx=10)

app.mainloop()
