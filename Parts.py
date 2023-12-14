import tkinter as tk
import time
from tkinter import messagebox, font
from graf import algorithm, algorithm2


class Parts():
    def __init__(self, window):
        self.window = window
        self.frame_for_canvas = tk.Frame(master=self.window, bg='#4E5754')
        self.canvas = tk.Canvas(master=self.frame_for_canvas, bg='#F5FFFA', width=800, height=550, highlightthickness=2,
                                highlightbackground='black')
        self.frame_for_parts = tk.Frame(master=self.window, bg='#4E5754')
        self.var = tk.BooleanVar()
        self.var.set(False)
        self.check = tk.Checkbutton(master=self.frame_for_parts, text="ориентированный граф", variable=self.var,
                                    onvalue=True,
                                    offvalue=False, bg='#4E5754')

        self.var1 = tk.BooleanVar()
        self.var1.set(False)
        self.check_other = tk.Checkbutton(master=self.frame_for_parts, text="взвешенный граф", variable=self.var1,
                                          onvalue=True,
                                          offvalue=False, bg='#4E5754', command=lambda: self.weight())

        self.label_rebra = tk.Label(master=self.frame_for_parts, text='установите вершины, соединяющиеся ребром',
                                    bg='#4E5754')
        self.frame_for_rebro = tk.Frame(master=self.frame_for_parts, bg='#4E5754')
        self.label_begin_r = tk.Label(master=self.frame_for_rebro, text='вершина начала ребра', bg='#4E5754',
                                      justify='left')
        self.label_end_r = tk.Label(master=self.frame_for_rebro, text='вершина конца ребра', bg='#4E5754',
                                    justify='left')
        self.label_weight = tk.Label(master=self.frame_for_rebro, text='вес ребра', bg='#4E5754', justify='left')
        self.entry_begin_rebro = tk.Entry(master=self.frame_for_rebro, width=5)
        self.entry_end_rebro = tk.Entry(master=self.frame_for_rebro, width=5)
        self.entry_weight = tk.Entry(master=self.frame_for_rebro, width=5)
        self.label_rebra_empty = tk.Label(master=self.frame_for_rebro,
                                      text=' ',
                                      bg='#4E5754')

        self.frame_for_button_graph = tk.Frame(master=self.frame_for_parts, bg='#4E5754')
        self.button_rebro = tk.Button(master=self.frame_for_button_graph, text='нарисовать ребро', bg='#B5B8B1',
                                      fg='black',
                                      command=lambda: self.botton_get_be())

        self.button_clear = tk.Button(master=self.frame_for_button_graph, text='очистить полотно', bg='#B5B8B1',
                                      fg='black',
                                      command=lambda: self.button_clean())

        self.count = 0
        self.top = '  '
        self.dict_of_grah = {}
        self.count1 = 1
        self.list_matrix = []
        self.list_circle = []
        self.path = []
        self.id = []
        self.list_weight = {}
        self.flag = 0
        self.set1 = []

        self.button_matrix = tk.Button(master=self.frame_for_parts, text='показать матрицу смежности', bg='#B5B8B1',
                                       fg='black',
                                       command=lambda: self.botton_show_matrix())

        self.label_rebra1 = tk.Label(master=self.frame_for_parts,
                                    text='установите вершину начала и вершину конца работы алгоритма',
                                    bg='#4E5754')
        self.frame_for_algorithm = tk.Frame(master=self.frame_for_parts, bg='#4E5754')
        self.entry_begin = tk.Entry(master=self.frame_for_algorithm, width=5)
        self.entry_end = tk.Entry(master=self.frame_for_algorithm, width=5)

        self.label_begin_a = tk.Label(master=self.frame_for_algorithm, text='вершина начала', bg='#4E5754',
                                      justify='left')
        self.label_end_a = tk.Label(master=self.frame_for_algorithm, text='вершина конца', bg='#4E5754', justify='left')

        self.frame_for_button_alg = tk.Frame(master=self.frame_for_parts, bg='#4E5754')
        self.button_algoritm = tk.Button(master=self.frame_for_button_alg, text='показать работу волнового алгоритма',
                                         bg='#B5B8B1',
                                         fg='black', command=lambda: self.botton_algorithm())
        self.button_clear_alg = tk.Button(master=self.frame_for_button_alg, text='отмена работы алгоритма',
                                          bg='#B5B8B1',
                                          fg='black',
                                          command=lambda: self.button_clean_alg())



        self.canvas.bind('<ButtonPress>', self.mouse_motion_circle)
        self.actions = []
        self.button_otmena = tk.Button(master=self.frame_for_button_graph, text='отмена',
                                          bg='#B5B8B1',
                                          fg='black',
                                          command=lambda: self.otmena())
        self.frame_for_result = tk.Frame(master=self.frame_for_parts, bg='#4E5754')

        self.label_result_empty1 = tk.Label(master=self.frame_for_button_alg,
                                           text=' ',
                                           bg='#4E5754')
        self.label_result_empty2 = tk.Label(master=self.frame_for_button_alg,
                                           text=' ',
                                           bg='#4E5754')

        self.label_rebra_result = tk.Label(master=self.frame_for_result,
                                     text='результат работы алгоритма: ',
                                     bg='#4E5754')

        self.label_rebra_r = tk.Label(master=self.frame_for_result,
                                     text=' ',
                                     bg='#4E5754', font=("Arial", 14))
        self.font1 = font.Font(family= "Arial", size=11, weight="normal", slant="roman", underline=True, overstrike=True)



    def to_text(self, path):
        path_text = ''
        for i in range(len(path)):
            if i != len(path) - 1:
                path_text += str(path[i]) + " - "
            else:
                path_text += str(path[i])
        return path_text

    def weight(self):
        if self.var1.get() == True:
            self.label_rebra_empty.grid_remove()
            self.entry_weight.grid(row=2, column=0, pady=5, padx=5, sticky="w")
            self.label_weight.grid(row=2, column=1, pady=10, padx=2, sticky="w")
        else:
            self.label_rebra_empty.grid(row=2, column=0, pady=10, padx=5, sticky="w")
            self.entry_weight.grid_forget()
            self.label_weight.grid_forget()

    def result(self, f):
        if f == True:
            self.label_result_empty1.grid_forget()
            self.label_result_empty2.grid_forget()
            self.label_rebra_result.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        else:
            self.label_result_empty1.grid()
            self.label_result_empty2.grid()
            self.label_rebra_result.grid_forget()
            self.label_rebra_r.grid_forget()

    def button_clean(self):
        self.canvas.delete("all")
        self.count = 0
        self.top = '  '
        self.dict_of_grah = {}

    def mouse_motion_circle(self, event):
        x, y = event.x, event.y
        self.count += 1
        self.set1.append(self.count)
        self.top += str(self.count) + ' '
        self.dict_of_grah[str(self.count)] = (x, y, self.count)
        self.flag += 1
        self.canvas.create_oval(x, y, x + 20, y + 20, fill='blue', outline='black', width=2, tags=f"line{self.flag}")
        self.canvas.create_text(x + 10, y + 10, text=self.count, tags=f"line{self.flag}")
        self.actions.append((f"line{self.flag}", 'o'))

    def botton_get_be(self):
        uinput = self.entry_begin_rebro.get()
        uinput2 = self.entry_end_rebro.get()
        if int(uinput) <= 0 or int(uinput2) <= 0 or uinput2 not in self.dict_of_grah or uinput not in self.dict_of_grah:
            messagebox.showerror(title="ошибка", message="неверный ввод данных")
            return
        p1 = self.dict_of_grah[uinput]
        p2 = self.dict_of_grah[uinput2]
        self.list_matrix.append([int(uinput), int(uinput2)])
        if self.var.get() == True and uinput == uinput2:
            x = p1[0]
            y = p1[1]
            self.canvas.create_oval(x - 4, y - 4, x + 40, y + 40, outline='grey', tags=f"line{self.flag}")
            return
        self.flag += 1
        if self.var.get() == True:
            if [int(uinput2), int(uinput)] in self.list_matrix:
                self.canvas.create_line(p2[0] , p2[1], p1[0], p1[1], width=1.5, arrow='both',
                                        fill="grey", stipple="gray50",tags=f"line{self.flag}")
                self.canvas.create_oval(p1[0], p1[1], p1[0] + 20, p1[1] + 20, fill='blue', outline='black', width=2,
                                        tags=f"line{self.flag}")
                self.canvas.create_text(p1[0] + 10, p1[1] + 10, text=p1[2], tags=f"line{self.flag}")
                self.canvas.create_oval(p2[0], p2[1], p2[0] + 20, p2[1] + 20, fill='blue', outline='black', width=2,
                                        tags=f"line{self.flag}")
                self.canvas.create_text(p2[0] + 10, p2[1] + 10, text=p2[2], tags=f"line{self.flag}")
            else:
                self.canvas.create_line(p1[0] + 11, p1[1] + 11, p2[0], p2[1] , width=1.5, arrow='last',
                                        fill="grey", stipple="gray50", tags=f"line{self.flag}")
                self.canvas.create_oval(p1[0], p1[1], p1[0] + 20, p1[1] + 20, fill='blue', outline='black', width=2,
                                        tags=f"line{self.flag}")
                self.canvas.create_text(p1[0] + 10, p1[1] + 10, text=p1[2], tags=f"line{self.flag}")
                self.canvas.create_oval(p2[0], p2[1], p2[0] + 20, p2[1] + 20, fill='blue', outline='black', width=2,
                                        tags=f"line{self.flag}")
                self.canvas.create_text(p2[0] + 10, p2[1] + 10, text=p2[2], tags=f"line{self.flag}")
        elif self.var.get() == False and self.var1.get() == False:
            self.canvas.create_line(p1[0] + 11, p1[1] + 11, p2[0] + 11, p2[1] + 11, width=1.5, fill="grey",
                                    stipple="gray50", tags=f"line{self.flag}")
            self.canvas.create_oval(p1[0], p1[1], p1[0] + 20, p1[1] + 20, fill='blue', outline='black', width=2,
                                    tags=f"line{self.flag}")
            self.canvas.create_text(p1[0] + 10, p1[1] + 10, text=p1[2], tags=f"line{self.flag}")
            self.canvas.create_oval(p2[0], p2[1], p2[0] + 20, p2[1] + 20, fill='blue', outline='black', width=2,
                                    tags=f"line{self.flag}")
            self.canvas.create_text(p2[0] + 10, p2[1] + 10, text=p2[2], tags=f"line{self.flag}")
        elif self.var1.get() == True:
            w = self.entry_weight.get()
            if int(w) <= 0 or w == "":
                messagebox.showerror(title="ошибка", message="неверный ввод данных")
                return
            self.list_weight[uinput + uinput2] = int(w)
            x = max(p1[0], p2[0]) - abs(p1[0] - p2[0] + 10) / 2
            y = max(p1[1], p2[1]) - abs(p1[1] - p2[1] + 10) / 2
            self.canvas.create_line(p1[0] + 15, p1[1] + 15, p2[0] + 5, p2[1] + 5, width=1.5, fill="grey",
                                    stipple="gray50", tags=f"line{self.flag}")
            self.canvas.create_oval(p1[0], p1[1], p1[0] + 20, p1[1] + 20, fill='blue', outline='black', width=2,
                                    tags=f"line{self.flag}")
            self.canvas.create_text(p1[0] + 10, p1[1] + 10, text=p1[2], tags=f"line{self.flag}")
            self.canvas.create_oval(p2[0], p2[1], p2[0] + 20, p2[1] + 20, fill='blue', outline='black', width=2,
                                    tags=f"line{self.flag}")
            self.canvas.create_text(p2[0] + 10, p2[1] + 10, text=p2[2], tags=f"line{self.flag}")
            self.canvas.create_oval(x - 8, y - 8, x + 12, y + 12, fill='#F5FFFA', outline='#F5FFFA', tags=f"line{self.flag}")
            self.canvas.create_text(x, y, text=w, font="Verdana 13", tags=f"line{self.flag}")
        self.actions.append((f"line{self.flag}", 'l'))

    def otmena(self):
        if self.set1 == []:
            messagebox.showerror(title="ошибка", message="нет данных для отмены")
            return
        n = len(self.actions)
        str1 = self.actions[n - 1][0]
        metka = self.actions[n - 1][1]
        if metka == 'o':
            self.canvas.delete(str1)
            n1 = len(str(self.count))
            self.count-=1
            self.set1.pop()
            self.top = self.top[:len(self.top)-n1-1]
            self.dict_of_grah.pop(str(self.count +1))
            self.actions.pop()
        if metka == 'l':
            self.canvas.delete(str1)
            self.list_matrix.pop()
            self.actions.pop()



    def matr(self):
        if self.set1 == []:
            return
        max_top = max(self.set1)
        global matrix
        matrix = [[0 for i in range(max_top)] for j in range(max_top)]
        matrix_text = '\n'
        if self.var.get() == True:
            for i in self.list_matrix:
                matrix[i[0] - 1][i[1] - 1] = 1
        else:
            for i in self.list_matrix:
                matrix[i[0] - 1][i[1] - 1] = 1
                matrix[i[1] - 1][i[0] - 1] = 1
        for k in range(max_top):
            matrix_text += str(k + 1) + ' '
            for j in range(max_top):
                matrix_text += str(matrix[k][j]) + ' '
            matrix_text += '\n'
        return matrix_text

    def botton_show_matrix(self):
        window2 = tk.Toplevel(width=200, height=200)
        window2.title("Матрица смежности")
        global matrix_text
        if len(self.dict_of_grah) != 0:
            matrix_text = self.matr()
            t = tk.Text(master=window2)
            t.pack(fill='both', expand=True)
            t.insert("1.0", self.top)
            t.insert("2.0", matrix_text)

    def botton_algorithm(self):
        start = self.entry_begin.get()
        end = self.entry_end.get()
        if int(start) <= 0 or int(end) <= 0 or start not in self.dict_of_grah or end not in self.dict_of_grah:
            messagebox.showerror(title="ошибка", message="неверный ввод данных")
            return
        set1 = self.matr()
        if self.var1.get() == False:
            path = algorithm(matrix, start_node=int(start), end_node=int(end))
        else:
            path = algorithm2(graph=matrix, start_node=int(start), end_node=int(end), list_weight=self.list_weight)
        if path == None:
            return
        for i in path:
            coord = self.dict_of_grah[str(i)]
            id1 = self.canvas.create_oval(coord[0], coord[1], coord[0] + 20, coord[1] + 20, fill='red')
            id2 = self.canvas.create_text(coord[0] + 10, coord[1] + 10, text=i)
            self.window.update()
            time.sleep(0.5)
            self.id.append([id1, id2])
        text = self.to_text(path)
        #self.result(f=True)
        self.label_rebra_r.config(text=text)
        self.label_rebra_r.config(background='#B5B8B1')
        self.label_rebra_r.grid(row=1, column=0, pady=5, padx=5,sticky='w')

    def button_clean_alg(self):
        for i in self.id:
            self.canvas.delete(i[0])
            self.canvas.delete(i[1])
            self.label_rebra_r.destroy()

    def draw_widgets(self):
        self.frame_for_parts.pack(side='left', expand=True, fill='both')
        self.frame_for_canvas.pack(side='right', expand=True, fill='both')
        self.canvas.pack(expand=True, padx=5, pady=5)

        self.check.pack(expand=True, pady=5, padx=10, anchor="nw")
        self.check_other.pack(expand=True, pady=5, padx=10, anchor="nw")

        self.label_rebra.pack(expand=True, fill="both", pady=5, padx=2)
        self.frame_for_rebro.pack(expand=True, pady=5, padx=10, anchor="w")
        self.label_begin_r.grid(row=0, column=1, pady=10, padx=2, sticky="w")
        self.label_end_r.grid(row=1, column=1, pady=10, padx=2, sticky="w")
        self.label_rebra_empty.grid(row=2, column=0, pady=10, padx=5, sticky="w")
        self.label_weight.grid_remove()
        self.entry_begin_rebro.grid(row=0, column=0, pady=5, padx=5, sticky="w")
        self.entry_end_rebro.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.entry_weight.grid_remove()
        self.frame_for_button_graph.pack(expand=True, pady=5, padx=5, anchor="w")
        self.button_rebro.grid(row=0, column=0, pady=10, padx=10, sticky='w')
        self.button_clear.grid(row=0, column=1, pady=10, padx=10, sticky='w')
        self.button_otmena.grid(row=0, column=2, pady=10, padx=10, sticky='w')

        self.button_matrix.pack(expand=True, pady=5, padx=15, anchor="nw")

        self.label_rebra1.pack(expand=True, fill="both", pady=5, padx=2)
        self.frame_for_algorithm.pack(expand=True, pady=5, padx=10, anchor="nw")
        self.entry_begin.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        self.entry_end.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        self.label_begin_a.grid(row=0, column=1, pady=10, padx=5, sticky='w')
        self.label_end_a.grid(row=1, column=1, pady=10, padx=5, sticky='w')
        self.frame_for_button_alg.pack(expand=True, pady=5, padx=10, anchor="nw")
        self.button_algoritm.grid(row=0, column=0, pady=10, padx=5, sticky='w')
        self.button_clear_alg.grid(row=0, column=1, pady=10, padx=5, sticky='w')
        self.frame_for_result.pack(expand=True, pady=5, padx=10, anchor="nw")
        self.label_rebra_result.grid(row=0, column=0, pady=5, padx=5)
        self.label_rebra_r.grid(row=1, column=0, pady=5, padx=5, sticky='w')

