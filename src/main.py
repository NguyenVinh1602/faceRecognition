import tkinter as tk
from tkinter import Label, Button, Canvas, PhotoImage
from define import *
from PIL import Image, ImageTk
import os

def create_attendant_page(root):
    """Tạo giao diện trang Attendant Standards Checking System"""
    page = tk.Frame(root, bg='white')
    page.pack(fill='both', expand=True)
    
    canvas = Canvas(page, bg='white', highlightthickness=0)
    canvas.place(relx=0.1, rely=0.08, relwidth=0.55, relheight=0.9)
    
    # Tiêu đề
    title = Label(canvas, text="Attendant Standards Checking System",justify='left' ,wraplength=700, fg="#006884", font=(FONT, 30, "bold"), bg='white')
    title.pack(pady=20, anchor='w',)
    
    # Nội dung mô tả
    desc = Label(canvas, text=("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
                           "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
                           "when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
                           "It has survived not only five centuries, but also the leap into electronic typesetting, "
                           "remaining essentially unchanged."),
             wraplength=550, justify='left', font=(FONT, 13, "normal"),
             bg='white')
    desc.pack(anchor='w', pady=20)
    
    # Yêu cầu compliance
    compliance_label = Label(canvas, text="Before using the application please comply with the following regulations.",
                              wraplength=500,justify='left',font=(FONT, 14), bg='white')
    compliance_label.pack(pady=(20, 5), anchor='w')
    
    # Hiển thị hình ảnh vật 
    item_canvas = Canvas(canvas, width=600, height=150, bg='white', highlightthickness=0)
    item_canvas.pack(anchor='w', pady = 40)
    
    image_folder = "public"

    image1 = Image.open(os.path.join(image_folder, "IdCard.png")).resize((150, 150))
    image2 = Image.open(os.path.join(image_folder, "WhiteMask.png ")).resize((150, 150))
    image3 = Image.open(os.path.join(image_folder, "SunGlasses.png")).resize((150, 150))

    photo1 = ImageTk.PhotoImage(image1)
    photo2 = ImageTk.PhotoImage(image2)
    photo3 = ImageTk.PhotoImage(image3)

    # Thêm ảnh vào Canvas
    item_canvas.create_image(100, 70, image=photo1)  
    item_canvas.create_image(300, 70, image=photo2) 
    item_canvas.create_image(500, 70, image=photo3) 

    # Giữ tham chiếu để tránh bị xóa bởi Garbage Collector
    item_canvas.image1 = photo1
    item_canvas.image2 = photo2
    item_canvas.image3 = photo3
    
    # Nút Start Identifying
    start_btn = Button(canvas, bg='#DC9D1F', fg='white', font=(FONT, 10, "bold"),
                       padx=10, pady=5, border=0, text="Start Identifying")
    start_btn.pack(pady=20,anchor='nw')

    def update_image(event=None):
        # Lấy kích thước thực của Canvas
        width, height = canvas2.winfo_width(), canvas2.winfo_height()
        if width > 0 and height > 0:
            image = Image.open(image_attendant).resize((width, height))  # Resize ảnh
            photo = ImageTk.PhotoImage(image)
        
            canvas2.image = photo  # Giữ tham chiếu
            canvas2.create_image(0, 0, anchor='nw', image=photo)  # Hiển thị ảnh
    
    # Hình tiếp viên (giả lập bằng Label, có thể thay bằng hình thật với PhotoImage)
    image_attendant = os.path.join(image_folder, "TiepVien.png") 

    # Thêm ảnh vào Label
    canvas2 = tk.Canvas(root, bg='white')
    canvas2.place(relx=0.60, relwidth=0.4, relheight=1)

    # Gọi hàm update_image sau khi giao diện load xong
    root.bind("<Configure>", update_image) 

    
    return page


class App:
    def __init__(self, window):
        self.window = window
        window.geometry("{}x{}+{}+{}".format(WINDOWN_WIDTH, WINDOWN_HEIGHT, WINDOWN_POSITION_RIGHT, WINDOWN_POSITION_DOWN))
        
        # Lưu trang hiện tại để quản lý
        self.current_page = None

        # Tiêu đề
        window.title("Project Name")

        # Background
        window['background'] = COLOR_BACKGROUND

        # Hiển thị trang Attendant mặc định
        self.show_attendant_page()

    def show_attendant_page(self):
        """Hiển thị trang Attendant Standards Checking"""
        # Xóa trang hiện tại nếu có
        if self.current_page:
            self.current_page.destroy()

        # Tạo trang mới
        self.current_page = create_attendant_page(self.window)


def create_main_window():
    window = tk.Tk()
    app = App(window)
    window.mainloop()

if __name__ == "__main__":
    create_main_window()
