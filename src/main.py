import tkinter as tk
from tkinter import Label, Button, Canvas, PhotoImage
from define import * 

def create_attendant_page(root):
    page = tk.Frame(root, bg='white')
    page.pack(fill='both', expand=True)
    
    # Canvas để tạo khung viền xanh
    canvas = Canvas(page, bg='white', highlightthickness=0)
    canvas.place(relx=0.02, rely=0.05, relwidth=0.6, relheight=0.9)
    
    # Tiêu đề
    title = Label(canvas, text="Attendant Standards Checking System", fg="#0077C8", font=("Arial", 14, "bold"), bg='white')
    title.pack(pady=(20, 10), anchor='w', padx=20)
    
    # Nội dung mô tả
    desc = Label(canvas, text=("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
                               "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s."),
                 wraplength=350, justify='left', bg='white')
    desc.pack(anchor='w', padx=20)
    
    # Yêu cầu compliance
    compliance_label = Label(canvas, text="Before using the application please comply with the following regulations.",
                             font=("Arial", 10, "bold"), bg='white')
    compliance_label.pack(pady=(15, 5), anchor='w', padx=20)
    
    # Hiển thị hình ảnh vật dụng (giả lập bằng Label, có thể thay bằng PhotoImage)
    item_canvas = Canvas(canvas, width=350, height=100, bg='white', highlightthickness=1, highlightbackground='blue')
    item_canvas.pack(anchor='w', padx=20, pady=10)
    
    # Nút Start Identifying
    start_btn = Button(canvas, text="Start Identifying", bg='#F4A100', fg='white', font=("Arial", 10, "bold"),
                       padx=10, pady=5, border=0)
    start_btn.pack(pady=20)
    
    # Hình tiếp viên (có thể thay bằng hình thật với PhotoImage)
    img_label = Label(page, bg='white')
    img_label.place(relx=0.65, rely=0.05, relwidth=0.33, relheight=0.9)
    
    return page



class App():

    def __init__(self, window) -> None:
        self.window = window
        window.geometry("{}x{}+{}+{}".format(WINDOWN_WIDTH, WINDOWN_HEIGHT, WINDOWN_POSITION_RIGHT, WINDOWN_POSITION_DOWN))

        # Initialize saved images list
        self.saved_images = []

        # Title
        window.title("Project Name")
        # Background
        window['background'] = COLOR_BACKGROUND



def create_main_window():
    window = tk.Tk()
    app = App(window)
    window.mainloop()

if __name__ == "__main__":
    create_main_window()

