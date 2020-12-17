import tkinter as tk

top = tk.Tk()

C = tk.Canvas(top, bg='black', bd=0, height=300, width=300)
coord = 10, 50, 200, 210
arc = C.create_arc(coord, start=0, extent=150, fill='red')
C.pack()
top.mainloop()