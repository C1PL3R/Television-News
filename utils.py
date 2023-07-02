def toggle_menu(menu_frame, scrollable_frame):
    if menu_frame.winfo_x() < 0:
        move_menu(menu_frame, scrollable_frame, 0)
    else:
        move_menu(menu_frame, scrollable_frame, -200)

def move_menu(menu_frame, scrollable_frame, target_x):
    current_x = menu_frame.winfo_x()
    if current_x != target_x:
        if current_x < target_x:
            menu_frame.place(x=current_x + 10, y=0)
        else:
            menu_frame.place(x=current_x - 10, y=0)
        scrollable_frame.after(10, lambda: move_menu(menu_frame, scrollable_frame, target_x))


import webbrowser

def open_url():
    url = "https://www.t.me/tn_supportBot"  # Ваш URL-адреса тут
    webbrowser.open(url)