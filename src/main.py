import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
import os
from define import *
import cv2

class LoadingScreen(tk.Toplevel):
    def __init__(self, parent, on_finish):
        super().__init__(parent)
        self.title("Attendant Standards Checking System - ASCS")
        self.geometry("{}x{}+{}+{}".format(WINDOWN_WIDTH, WINDOWN_HEIGHT, WINDOWN_POSITION_RIGHT, WINDOWN_POSITION_DOWN))

        image_path = "public/VNairlinesBrand.png"  
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((WINDOWN_WIDTH, WINDOWN_HEIGHT), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        self.canvas = tk.Canvas(self, width=WINDOWN_WIDTH, height=WINDOWN_HEIGHT)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)

        self.canvas.create_text(430, 570, text="Attendant Standards Checking System - ASCS", 
                                font=("Arial", 16, "bold"), fill="white")

        style = ttk.Style()
        style.theme_use('clam')

        style.configure("Custom.Horizontal.TProgressbar",
                        troughcolor='#005BAC',
                        bordercolor="transparent",
                        background='#FFC44E',
                        thickness=5)

        # === Thanh Loading Bar ===
        self.progress = ttk.Progressbar(self, orient="horizontal", length=600, mode="determinate",
                                        style="Custom.Horizontal.TProgressbar")
        self.progress.place(x=200, y=610)

        #"Now Loading"
        self.loading_text = tk.Label(self, text="Now Loading", font=("Arial", 10), bg="#006884", fg="white")
        self.loading_text.place(x=200, y=635)

        self.on_finish = on_finish  

        # Chạy loading sau khi mở app
        self.after(1000, self.load_main_interface)

    def load_main_interface(self):
        for i in range(101):
            self.progress["value"] = i
            self.update_idletasks()
            time.sleep(0.03)  

        self.on_finish() 
        self.destroy() 


# === Giao diện Attendant Standards Checking System ===
def create_attendant_page(root):
    for widget in root.winfo_children():
        widget.destroy()

    page = tk.Frame(root, bg='white')
    page.pack(fill='both', expand=True)
    
    canvas = tk.Canvas(page, bg='white', highlightthickness=0)
    canvas.place(relx=0.1, rely=0.08, relwidth=0.55, relheight=0.9)
    
    # Title
    title = tk.Label(canvas, text="Attendant Standards Checking System", justify='left', 
                    wraplength=700, fg="#006884", font=("Arial", 30, "bold"), bg='white')
    title.pack(pady=20, anchor='w')
    
    # Description
    desc = tk.Label(canvas, text=("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
                                    "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
                                    "when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
                                    "It has survived not only five centuries, but also the leap into electronic typesetting, "
                                    "remaining essentially unchanged."),
                    wraplength=550, justify='left', font=("Arial", 13),
                    bg='white')
    desc.pack(anchor='w', pady=20)
    
    # Compliance
    compliance_label = tk.Label(canvas, text="Before using the application please comply with the following regulations.",
                                wraplength=500, justify='left', font=("Arial", 14), bg='white')
    compliance_label.pack(pady=(20, 5), anchor='w')
    
    # Item img
    item_canvas = tk.Canvas(canvas, width=600, height=150, bg='white', highlightthickness=0)
    item_canvas.pack(anchor='w', pady=40)
    
    image_folder = "public/"

    image1 = Image.open(os.path.join(image_folder, "IdCard.png")).resize((150, 150))
    image2 = Image.open(os.path.join(image_folder, "WhiteMask.png")).resize((150, 150))
    image3 = Image.open(os.path.join(image_folder, "SunGlasses.png")).resize((150, 150))

    photo1 = ImageTk.PhotoImage(image1)
    photo2 = ImageTk.PhotoImage(image2)
    photo3 = ImageTk.PhotoImage(image3)

    item_canvas.create_image(100, 70, image=photo1)  
    item_canvas.create_image(300, 70, image=photo2) 
    item_canvas.create_image(500, 70, image=photo3) 

    item_canvas.image1 = photo1
    item_canvas.image2 = photo2
    item_canvas.image3 = photo3
    
    # Button Start Identifying
    start_btn = tk.Button(canvas, bg='#DC9D1F', fg='white', font=("Arial", 10, "bold"),
                        padx=10, pady=5, border=0, text="Start Identifying",
                        command=root.show_identification_page)  # Thêm command để chuyển trang
    start_btn.pack(pady=20, anchor='nw')

    def update_image(event=None):
        width, height = canvas2.winfo_width(), canvas2.winfo_height()
        if width > 0 and height > 0:
            image = Image.open(image_attendant).resize((width, height))  
            photo = ImageTk.PhotoImage(image)
        
            canvas2.image = photo  
            canvas2.create_image(0, 0, anchor='nw', image=photo)  
    
    # frame right
    image_attendant = os.path.join(image_folder, "TiepVien.png") 

    canvas2 = tk.Canvas(root, bg='white')
    canvas2.place(relx=0.60, relwidth=0.4, relheight=1)

    root.bind("<Configure>", update_image) 
    
    return page


# === Main App ===
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        self.geometry("{}x{}+{}+{}".format(WINDOWN_WIDTH, WINDOWN_HEIGHT, WINDOWN_POSITION_RIGHT, WINDOWN_POSITION_DOWN))

        # Page Loading
        self.withdraw()
        self.loading_screen = LoadingScreen(self, self.show_attendant_page)

        # Page Attendant
    def show_attendant_page(self):
        self.deiconify() 
        create_attendant_page(self)

        # Main
    def show_identification_page(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.configure(bg=COLOR_CAMERA)

        self.cap = cv2.VideoCapture(0)
        self.load_icons() 
        self.create_widgets()
        self.update_camera()

    def load_icons(self):
        self.icon_camera = ImageTk.PhotoImage(Image.open("public/icon/camera.png").resize((30, 30)))
        self.icon_upload = ImageTk.PhotoImage(Image.open("public/icon/upload.png").resize((30, 30)))
        self.icon_load = ImageTk.PhotoImage(Image.open("public/icon/load.png").resize((30, 30)))
        self.icon_img = ImageTk.PhotoImage(Image.open("public/icon/img.png").resize((30, 30)))
        self.icon_menu = ImageTk.PhotoImage(Image.open("public/icon/menu.png").resize((30, 10)))

    def create_widgets(self):
        # Frame chính
        main_frame = tk.Frame(self, bg=COLOR_CAMERA)
        main_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Frame camera
        self.image_frame = tk.Label(main_frame, bg=COLOR_CAMERA)
        self.image_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Instruction
        instruction_label = tk.Label(
            main_frame,
            text="Please stay in the center of the frame. The identification process will take place automatically",
            fg="white",
            bg="#1a1a1a",
        )
        instruction_label.pack(pady=(0, 30))

        # navbar
        control_frame = tk.Frame(main_frame, bg=COLOR_BG_CAMERA)
        control_frame.pack(fill="x")
        control_frame.columnconfigure(0, weight=1)
        control_frame.columnconfigure(1, weight=3)
        control_frame.columnconfigure(2, weight=1)

        # Toggle button right
        toggle_container = tk.Frame(control_frame, bg=COLOR_BG_CAMERA)
        toggle_container.grid(row=0, column=0, sticky="w", padx=10, pady=15)

        toggle_label = tk.Label(
            toggle_container,
            text="Automatically Identification",
            fg="white",
            bg=COLOR_BG_CAMERA,
        )
        toggle_label.pack(side="left")

        toggle_button = ttk.Checkbutton(toggle_container)
        toggle_button.pack(side="left", padx=5)

        # button center
        button_frame = tk.Frame(control_frame, bg=COLOR_BG_CAMERA)
        button_frame.grid(row=0, column=1, sticky="ns", pady=5)
        
        capture_button = tk.Button(button_frame, image=self.icon_camera, bg="black", relief="flat")
        capture_button.pack(side="left", padx=10)
        
        upload_button = tk.Button(button_frame, image=self.icon_upload, bg="black", relief="flat")
        upload_button.pack(side="left", padx=10)
        
        settings_button = tk.Button(button_frame, image=self.icon_load, bg="black", relief="flat")
        settings_button.pack(side="left", padx=10)
        
        # button right
        right_button_frame = tk.Frame(control_frame, bg=COLOR_BG_CAMERA)
        right_button_frame.grid(row=0, column=2, sticky="e", padx=10, pady=5)
        
        # === Frame cho image_button ===
        self.frame_img = tk.Frame(self, bg=COLOR_BACKGROUND, bd=2, relief="ridge")
        self.frame_img_label = tk.Label(self.frame_img, text="📷 Image Options", fg="white", bg="#333333")
        self.frame_img_label.pack(pady=10)

        # === Frame cho menu_button ===
        self.frame_menu = tk.Frame(self, bg=COLOR_BACKGROUND, bd=2, relief="ridge")
        self.frame_menu_label = tk.Label(self.frame_menu, text="📋 Menu Options", fg="white", bg="#444444")
        self.frame_menu_label.pack(pady=10)

        # === Nút Image mở frame_img ===
        image_button = tk.Button(right_button_frame, image=self.icon_img, bg="black", relief="flat",
                         command=lambda: self.toggle_frame(self.frame_img, x_offset=0.85))
        image_button.pack(side="left", padx=5)

        # === Nút Menu mở frame_menu ===
        menu_button = tk.Button(right_button_frame, image=self.icon_menu, bg="black", relief="flat",
                        command=lambda: self.toggle_frame(self.frame_menu, x_offset=0.85))
        menu_button.pack(side="left", padx=5)



    def update_camera(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            frame = cv2.resize(frame, (CAMERA_WIDTH, CAMERA_HEIGHT))

            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.image_frame.imgtk = imgtk
            self.image_frame.configure(image=imgtk)
        self.after(10, self.update_camera)

    def toggle_frame(self, frame, x_offset):
        """Hiển thị hoặc ẩn Frame ở bên phải."""
        if frame.winfo_ismapped():
            frame.place_forget()
        else:
            frame.place(relx=0.85, rely=0.1, relwidth=0.14, relheight=0.3)

    def on_closing(self):
        self.cap.release()
        self.destroy()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()