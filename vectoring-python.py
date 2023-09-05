from customtkinter import *
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from CTkMessagebox import CTkMessagebox

m = CTk()
m.attributes("-fullscreen", True)
set_appearance_mode("dark")

switch_var = StringVar(value="Dark")

def toggle():
    current = switch_var.get()
    if current == "Dark":
        lbl_answer.place_forget()
        set_appearance_mode("dark")
        toggle_switch.configure(text=get_appearance_mode())
        plt.close()

        fig = plt.figure(facecolor="#434343")
        ax = fig.add_subplot(111, projection="3d")
        ax.set_facecolor("#434343")

        canvas = FigureCanvasTkAgg(fig, master=m)
        canvas.get_tk_widget().place(x=20, y=140)

    else:
        lbl_answer.place_forget()
        set_appearance_mode("light")
        toggle_switch.configure(text=get_appearance_mode())
        plt.close()

        fig = plt.figure(facecolor="#FAF9F6")
        ax = fig.add_subplot(111, projection="3d")
        ax.set_facecolor("#FAF9F6")

        canvas = FigureCanvasTkAgg(fig, master=m)
        canvas.get_tk_widget().place(x=20, y=140)

def dot_product():
    plt.close()
    lbl_answer.place_forget()
    curr = get_appearance_mode()
    try:
        a = int(x1.get())
        b = int(y1.get())
        c = int(z1.get())
        d = int(x2.get())
        e = int(y2.get())
        f = int(z2.get())
        v1 = np.array([a, b, c])
        v2 = np.array([d, e, f])
        dot = np.dot(v1, v2)
        lbl_answer.configure(text=dot, text_color="white")

        width = answer.winfo_width()
        height = answer.winfo_height()
        center_x = width // 2
        center_y = height // 2

        lbl_answer.place(x=center_x, y=center_y, anchor=CENTER)

        if curr == "Light":
            fig = plt.figure(facecolor="#FAF9F6")
            ax = fig.add_subplot(111, projection="3d")
            ax.set_facecolor("#FAF9F6")
        else:
            fig = plt.figure(facecolor="#434343")
            ax = fig.add_subplot(111, projection="3d")
            ax.set_facecolor("#434343")

        ax.set_xlim([-dot, dot])
        ax.set_ylim([-dot, dot])
        ax.set_zlim([-dot, dot])

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        ax.quiver(0, 0, 0, a, b, c)
        ax.quiver(0, 0, 0, d, e, f, color="r")
        ax.scatter(dot, 0, 0, s=50, c='green') 

        canvas = FigureCanvasTkAgg(fig, master=m)
        canvas.draw()
        canvas.get_tk_widget().place(x=20, y=140)

    except ValueError:
        CTkMessagebox(master=m, title="Error!", message="Enter an integer!", icon="warning")
        lbl_answer.place_forget()

def cross_product():
    plt.close()
    curr = get_appearance_mode()
    lbl_answer.place_forget()
    try:
        a = int(x1.get())
        b = int(y1.get())
        c = int(z1.get())
        d = int(x2.get())
        e = int(y2.get())
        f = int(z2.get())
        v1 = np.array([a, b, c])
        v2 = np.array([d, e, f])
        cross = np.cross(v1, v2)
        i = cross[0]
        j = cross[1]
        k = cross[2]
        real_cross = f"({i}i) + ({j}j) + ({k}k)"
        lbl_answer.configure(text=real_cross, text_color="white")

        width = answer.winfo_width()
        height = answer.winfo_height()
        center_x = width // 2
        center_y = height // 2

        lbl_answer.place(x=center_x, y=center_y, anchor=CENTER)

        if curr == "Light":
            fig = plt.figure(facecolor="#FAF9F6")
            ax = fig.add_subplot(111, projection="3d")
            ax.set_facecolor("#FAF9F6")
        else:
            fig = plt.figure(facecolor="#434343")
            ax = fig.add_subplot(111, projection="3d")
            ax.set_facecolor("#434343")

        max_val = max(abs(cross))
        ax.set_xlim([-max_val, max_val])
        ax.set_ylim([-max_val, max_val])
        ax.set_zlim([-max_val, max_val])

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        ax.quiver(0, 0, 0, i, j, k, arrow_length_ratio=0.2, length=1, linewidth=2, color='r', pivot="tip")

        canvas = FigureCanvasTkAgg(fig, master=m)
        canvas.draw()
        canvas.get_tk_widget().place(x=20, y=140)

    except ValueError:
        CTkMessagebox(master=m, title="Error!", message="Enter an integer!", icon="warning")
        lbl_answer.place_forget()

def proj_a_on_b():
    plt.close()
    curr = get_appearance_mode()
    lbl_answer.place_forget()
    try:
        a = int(x1.get())
        b = int(y1.get())
        c = int(z1.get())
        d = int(x2.get())
        e = int(y2.get())
        f = int(z2.get())
        v1 = np.array([a, b, c])
        v2 = np.array([d, e, f])
        mag_v2 = np.sqrt(sum(v2 ** 2))
        projection = (np.dot(v1, v2) / mag_v2 ** 2) * v2
        i = projection[0]
        j = projection[1]
        k = projection[2]
        real_projection = f"({i:.2f}i) + ({j:.2f}j) + ({k:.2f}k)"
        lbl_answer.configure(text=real_projection, text_color="white")

        width = answer.winfo_width()
        height = answer.winfo_height()
        center_x = width // 2
        center_y = height // 2

        lbl_answer.place(x=center_x, y=center_y, anchor=CENTER)

        if curr == "Light":
            fig = plt.figure(facecolor="#FAF9F6")
            ax = fig.add_subplot(111, projection="3d")
            ax.set_facecolor("#FAF9F6")
        else:
            fig = plt.figure(facecolor="#434343")
            ax = fig.add_subplot(111, projection="3d")
            ax.set_facecolor("#434343")

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        max_val = max(abs(projection))
        ax.set_xlim([-max_val, max_val])
        ax.set_ylim([-max_val, max_val])
        ax.set_zlim([-max_val, max_val])

        ax.quiver(0, 0, 0, i, j, k, arrow_length_ratio=0.2, color='r', length=1, linewidth=2)

        canvas = FigureCanvasTkAgg(fig, master=m)
        canvas.draw()
        canvas.get_tk_widget().place(x=20, y=140)

    except ValueError:
        CTkMessagebox(master=m, title="Error!", message="Enter an integer!", icon="warning")
        lbl_answer.place_forget()

def proj_b_on_a():
    plt.close()
    curr = get_appearance_mode()
    lbl_answer.place_forget()
    try:
        a = int(x1.get())
        b = int(y1.get())
        c = int(z1.get())
        d = int(x2.get())
        e = int(y2.get())
        f = int(z2.get())
        v1 = np.array([a, b, c])
        v2 = np.array([d, e, f])
        mag_v1 = np.sqrt(sum(v1 ** 2))
        projection = (np.dot(v1, v2) / mag_v1 ** 2) * v1
        i = projection[0]
        j = projection[1]
        k = projection[2]
        real_projection = f"({i:.2f}i) + ({j:.2f}j) + ({k:.2f}k)"
        lbl_answer.configure(text=real_projection, text_color="white")

        width = answer.winfo_width()
        height = answer.winfo_height()
        center_x = width // 2
        center_y = height // 2

        lbl_answer.place(x=center_x, y=center_y, anchor=CENTER)

        if curr == "Light":
            fig = plt.figure(facecolor="#FAF9F6")
            ax = fig.add_subplot(111, projection="3d")
            ax.set_facecolor("#FAF9F6")
        else:
            fig = plt.figure(facecolor="#434343")
            ax = fig.add_subplot(111, projection="3d")
            ax.set_facecolor("#434343")

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        max_val = max(abs(projection))
        ax.set_xlim([-max_val, max_val])
        ax.set_ylim([-max_val, max_val])
        ax.set_zlim([-max_val, max_val])

        ax.quiver(0, 0, 0, i, j, k, arrow_length_ratio=0.2, length=1, linewidth=2, color='r', pivot="tip")

        canvas = FigureCanvasTkAgg(fig, master=m)
        canvas.draw()
        canvas.get_tk_widget().place(x=20, y=140)

    except ValueError:
        CTkMessagebox(master=m, title="Error!", message="Enter an integer!", icon="warning")
        lbl_answer.place_forget()

def plot():
    plt.close()
    lbl_answer.place_forget()
    curr = get_appearance_mode()
    try:
        a = int(x1.get())
        b = int(y1.get())
        c = int(z1.get())
        d = int(x2.get())
        e = int(y2.get())
        f = int(z2.get())
        v1 = np.array([a, b, c])
        v2 = np.array([d, e, f])
        if curr == "Light":
            fig = plt.figure(facecolor="#FAF9F6")
            ax = fig.add_subplot(111, projection="3d")
            ax.set_facecolor("#FAF9F6")

        else:
            fig = plt.figure(facecolor="#434343")
            ax = fig.add_subplot(111, projection="3d")
            ax.set_facecolor("#434343")

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        max_val = max(max(v1), max(v2))
        ax.set_xlim([-max_val, max_val])
        ax.set_ylim([-max_val, max_val])
        ax.set_zlim([-max_val, max_val])

        ax.quiver(0, 0, 0, a, b, c)
        ax.quiver(0, 0, 0, d, e, f, color="r")

        if curr == "Light":
            plt.legend(labels=["Vector A", "Vector B"], framealpha=1, loc="upper left", fontsize=8, facecolor="#FAF9F6")
        else:
            plt.legend(labels=["Vector A", "Vector B"], framealpha=1, loc="upper left", fontsize=8, facecolor="#434343", labelcolor="#FAF9F6")


        canvas = FigureCanvasTkAgg(fig, master=m)
        canvas.draw()
        canvas.get_tk_widget().place(x=20, y=140)

    except:
        CTkMessagebox(master=m, title="Error!", message="Enter an integer!", icon="warning")
        lbl_answer.place_forget()

def clear():
    plt.close()

    x1.delete(0, END)
    x2.delete(0, END)
    y1.delete(0, END)
    y2.delete(0, END)
    z1.delete(0, END)
    z2.delete(0, END)

    curr = get_appearance_mode()
    lbl_answer.place_forget()
    if curr == "Light":
        fig = plt.figure(facecolor="#FAF9F6")
        ax = fig.add_subplot(111, projection="3d")
        ax.set_facecolor("#FAF9F6")
    else:
        fig = plt.figure(facecolor="#434343")
        ax = fig.add_subplot(111, projection="3d")
        ax.set_facecolor("#434343")
    canvas = FigureCanvasTkAgg(fig, master=m)
    canvas.get_tk_widget().place(x=20, y=140)

def slogan_text(event):
    global slogan
    slogan = CTkLabel(master=title, text="Shayan, Hashir, Muneer", font=("Helvetica", 16))
    slogan.place(x=683, y=80, anchor=CENTER)

def slogan_text2(event):
    global slogan
    slogan.place_forget()

fig = plt.figure(facecolor="#434343")
ax = fig.add_subplot(111, projection="3d")
ax.set_facecolor("#434343")
canvas = FigureCanvasTkAgg(fig, master=m)
canvas.get_tk_widget().place(x=20, y=140)

ax.set_xlim([-15, 15])
ax.set_ylim([-15, 15])
ax.set_zlim([-15, 15])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# TITLE FRAME

title = CTkFrame(master=m, height=100, width=1366)
title.place(x=0, y=0)

title_lbl = CTkLabel(master=title, text="VECTORIN' BY SHM", font=("Helvetica", 30))
title_lbl.place(x=683, y=50, anchor=CENTER)
title_lbl.bind("<Enter>", slogan_text)
title_lbl.bind("<Leave>", slogan_text2)

# TOGGLE

toggle_switch = CTkSwitch(master=m, text=switch_var.get(), command=toggle, variable=switch_var, onvalue="Dark", offvalue="Light")
toggle_switch.place(x=1280, y=140)

# COPYRIGHT

copyrights = CTkLabel(master=m, text="Copyright 2023, SHM, All Rights Reserved.", anchor=E)
copyrights.place(x=1120, y=740)

# BUTTONS FRAME

button_frame = CTkFrame(master=m, width=642, height=50)
button_frame.place(x=20, y=700)

# OPERATIONS

dot_btn = CTkButton(master=button_frame, text="Dot Product", border_width=1, border_color="black", command=dot_product)
dot_btn.place(x=17, y=10)

cross_btn = CTkButton(master=button_frame, text="Cross Product", border_width=1, border_color="black", command=cross_product)
cross_btn.place(x=172, y=10)

Ab = CTkButton(master=button_frame, text="Proj of A onto B", border_width=1, border_color="black", command=proj_a_on_b)
Ab.place(x=327, y=10)

Ba = CTkButton(master=button_frame, text="Proj of B onto A", border_width=1, border_color="black", command=proj_b_on_a)
Ba.place(x=482, y=10)

# LABELS AND ENTRIES

lbl_x1 = CTkLabel(master=m, text="Enter x₁:")
lbl_x1.place(x=750, y=320)

x1 = CTkEntry(master=m, placeholder_text="Enter x₁", width=100)
x1.place(x=800, y=320)

lbl_y1 = CTkLabel(master=m, text="Enter y₁:")
lbl_y1.place(x=925, y=320)

y1 = CTkEntry(master=m, placeholder_text="Enter y₁", width=100)
y1.place(x=975, y=320)

lbl_z1 = CTkLabel(master=m, text="Enter z₁:")
lbl_z1.place(x=1100, y=320)

z1 = CTkEntry(master=m, placeholder_text="Enter z₁", width=100)
z1.place(x=1150, y=320)

plot_btn = CTkButton(m, text="Plot", border_width=1, border_color="black", command=plot, width=60)
plot_btn.place(x=1260, y=320)

lbl_x2 = CTkLabel(master=m, text="Enter x₂:")
lbl_x2.place(x=750, y=420)

x2 = CTkEntry(master=m, placeholder_text="Enter x₂", width=100)
x2.place(x=800, y=420)

lbl_y2 = CTkLabel(master=m, text="Enter y₂:")
lbl_y2.place(x=925, y=420)

y2 = CTkEntry(master=m, placeholder_text="Enter y₂", width=100)
y2.place(x=975, y=420)

lbl_z2 = CTkLabel(master=m, text="Enter z₂:")
lbl_z2.place(x=1100, y=420)

z2 = CTkEntry(master=m, placeholder_text="Enter z₂", width=100)
z2.place(x=1150, y=420)

answer = CTkFrame(master=m, fg_color="black", width=510, height=100)
answer.place(x=750, y=520)

lbl_answer = CTkLabel(master=answer, text="", font=("Helvetica", 30))
lbl_answer.place(x=255, y=120)

clear_btn = CTkButton(master=m, text="Clear Graph", border_width=1, border_color="black", command=clear)
clear_btn.place(x=905, y=705)

exit_btn = CTkButton(master=m, text="Exit", border_width=1, border_color="black", command=m.quit, width=60)
exit_btn.place(x=1050, y=705)

m.mainloop()