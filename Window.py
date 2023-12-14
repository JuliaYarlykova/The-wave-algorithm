import tkinter as tk

from Parts import Parts

class Window():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Волновой алгоритм")
        self.window.geometry("800x580")
        self.window.resizable(False, False)
        self.parts = Parts(self.window)
        self.mainmenu = tk.Menu(master=self.window)
        self.mainmenu.add_cascade(label="описание", command=lambda: self.description())
        self.mainmenu.add_cascade(label="инструкция", command=lambda : self.instr())
        self.bg = tk.PhotoImage(file="описание2.png")
        self.bg2 = tk.PhotoImage(file="инструкция.png")

    def description(self):
        window3 = tk.Toplevel(width=524, height=445)
        window3.title("описание")
        label = tk.Label(master=window3, image=self.bg, background="#4E5754")
        label.place(x=0, y=0)

    def instr(self):
        window4 = tk.Toplevel(width=542, height=469)
        window4.title("инструкция")
        label = tk.Label(master=window4, image=self.bg2, background="#4E5754")
        label.place(x=0, y=0)

    def run(self):
        self.draw_widgets()
        self.window.config(menu=self.mainmenu)
        self.window.mainloop()

    def draw_widgets(self):
        self.parts.draw_widgets()


if __name__ == "__main__":
    window = Window()
    window.run()
