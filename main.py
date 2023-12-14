import tkinter as tk
from graf import algorithm, algorithm2
import time
from tkinter import messagebox
########################
#global +
set1 = []
top = '  '
dict_of_grah = {}

count = 0
count1 = 1
list_matrix = []
list_circle = []
path = []
id= []
list_weight = {}
flag = 0

######################### +
window = tk.Tk()
window.title("Волновой алгоритм")
window.geometry("800x580")
window.resizable(False, False)

########################## +
# главные рамки
frame_for_parts = tk.Frame(master=window, bg='#4E5754')
frame_for_parts.pack(side='left', expand=True, fill='both')
frame_for_canvas = tk.Frame(master=window, bg='#4E5754')
frame_for_canvas.pack(side='right', expand=True, fill='both')

##########################+
#флаг
var = tk.BooleanVar()
var.set(False)

check = tk.Checkbutton(master=frame_for_parts, text="ориентированный граф", variable=var, onvalue=True, offvalue=False,bg='#4E5754' )
check.pack(expand=True, pady=5, padx=10, anchor="nw")

var1 = tk.BooleanVar()
var1.set(False)

check_other = tk.Checkbutton(master=frame_for_parts, text="взвешенный граф", variable=var1, onvalue=True, offvalue=False, bg='#4E5754', command=lambda: weight())
check_other.pack(expand=True, pady=5, padx=10, anchor="nw")

########################## +
# установление ребер
label_rebra = tk.Label(master=frame_for_parts, text='установите вершины, соединяющиеся ребром', bg='#4E5754')
label_rebra.pack(expand=True, fill="both", pady=5, padx=2)

frame_for_rebro = tk.Frame(master=frame_for_parts, bg='#4E5754')
frame_for_rebro.pack(expand=True, pady=5, padx=10,anchor="w")


def label():
    label_begin = tk.Label(master=frame_for_rebro, text='вершина начала ребра', bg='#4E5754', justify='left')
    label_begin.grid(row=0, column=1, pady=10, padx=2, sticky="w")
    label_end = tk.Label(master=frame_for_rebro, text='вершина конца ребра', bg='#4E5754', justify='left')
    label_end.grid(row=1, column=1, pady=10, padx=2, sticky="w")
    label_weight = tk.Label(master=frame_for_rebro, text='вес ребра', bg='#4E5754', justify='left')
    label_weight.grid(row=2, column=1, pady=10, padx=2, sticky="w")


label()

entry_begin_rebro = tk.Entry(master=frame_for_rebro, width=5)
entry_begin_rebro.grid(row=0, column=0, pady=5, padx=5, sticky="w")

entry_end_rebro = tk.Entry(master=frame_for_rebro, width=5)
entry_end_rebro.grid(row=1, column=0, pady=5, padx=5, sticky="w")

entry_weight = tk.Entry(master=frame_for_rebro, width=5, state="disabled")
entry_weight.grid(row=2, column=0, pady=5, padx=5, sticky="w")

def weight():
    if var1.get() == True:
        entry_weight.config(state="normal")
    else:
        entry_weight.config(state="disabled")

frame_for_button_graph = tk.Frame(master=frame_for_parts, bg='#4E5754')
frame_for_button_graph.pack(expand=True, pady=5, padx=5,anchor="w")

button_rebro = tk.Button(master=frame_for_button_graph, text='нарисовать ребро', bg='#B5B8B1', fg='black',
                         command=lambda: botton_get_be())
button_rebro.grid(row=0, column=0, pady=10, padx=10, sticky='w')

##########################
#кнопка очистки
button_clear = tk.Button(master=frame_for_button_graph, text='очистить полотно', bg='#B5B8B1', fg='black',
                         command=lambda: button_clean())
button_clear.grid(row=0, column=1, pady=10, padx=10, sticky='w')
def button_clean():
    canvas.delete("all")
    global count
    global top
    global dict_of_grah
    count = 0
    top = '  '
    dict_of_grah = {}

########################## +
# кнопка матрицы
button_matrix = tk.Button(master=frame_for_parts, text='показать матрицу смежности', bg='#B5B8B1', fg='black',
                          command=lambda: botton_show_matrix())
button_matrix.pack(expand=True, pady=5, padx=15, anchor="nw")

########################## +
# установление начала и конца работы алгоритма и веса ребра

label_rebra = tk.Label(master=frame_for_parts, text='установите вершину начала и вершину конца работы алгоритма',
                       bg='#4E5754')
label_rebra.pack(expand=True, fill="both", pady=5, padx=2)

frame_for_algorithm = tk.Frame(master=frame_for_parts, bg='#4E5754')
frame_for_algorithm.pack(expand=True, pady=5, padx=10, anchor="nw")

entry_begin = tk.Entry(master=frame_for_algorithm, width=5)
entry_begin.grid(row=0, column=0, pady=5, padx=5, sticky='w')
entry_end = tk.Entry(master=frame_for_algorithm, width=5)
entry_end.grid(row=1, column=0, pady=5, padx=5, sticky='w')

def label2():
    label_begin = tk.Label(master=frame_for_algorithm, text='вершина начала', bg='#4E5754', justify='left')
    label_begin.grid(row=0, column=1, pady=10, padx=5, sticky='w')
    label_end = tk.Label(master=frame_for_algorithm, text='вершина конца', bg='#4E5754', justify='left')
    label_end.grid(row=1, column=1, pady=10, padx=5, sticky='w')

label2()

########################## +
# работа волнового алгоритма

frame_for_button_alg = tk.Frame(master=frame_for_parts, bg='#4E5754')
frame_for_button_alg.pack(expand=True, pady=0, padx=10, anchor="nw")

def button():
    button_algoritm = tk.Button(master=frame_for_button_alg, text='показать работу волнового алгоритма', bg='#B5B8B1',
                                fg='black', command=lambda: botton_algorithm())
    button_algoritm.grid(row=0,column=0, pady=10, padx=5, sticky='w')

button()

########################## +
#отмена работы волнового алгоритма

button_clear_alg = tk.Button(master=frame_for_button_alg, text='отмена работы алгоритма', bg='#B5B8B1', fg='black',
                         command=lambda: button_clean_alg())

button_clear_alg.grid(row=0,column=1, pady=10, padx=5, sticky='w')

############################ +
canvas = tk.Canvas(master=frame_for_canvas, bg='#F5FFFA', width=800, height=550, highlightthickness=2,
                   highlightbackground='black')

########################## +
#результат работы
frame_for_result = tk.Frame(master=frame_for_parts, bg='#4E5754')
frame_for_result.pack(expand=True, pady=5, padx=10, anchor="w")

label_rebra = tk.Label(master=frame_for_result, text='результат работы программы: ', bg='#4E5754')
label_rebra.grid(row=0,column=0, pady=7, padx=5, sticky='w')

def to_text():
    path_text = ""
    for i in range(len(path)):
        if i != len(path) - 1:
            path_text += str(path[i]) + " - "
        else:
            path_text += str(path[i])
    return path_text
path_text = to_text()
result = tk.Label(master=frame_for_result, text=path_text, bg = "#4E5754")
result.grid(row=1,column=0, pady=7, padx=5, sticky='w')


########################## +
def mouse_motion_circle(event):
    global dict_of_grah
    global flag
    x, y = event.x, event.y
    global count
    count += 1
    global top
    global list_circle
    set1.append(count)
    top += str(count) + ' '
    dict_of_grah[str(count)] = (x, y)
    flag += 1
    canvas.create_oval(x, y, x + 20, y + 20, fill='blue', outline='black', width=2, tags=f"line{flag}")
    canvas.create_text(x + 10, y + 10, text=count, tags=f"line{flag}")

canvas.bind('<ButtonPress>', mouse_motion_circle)

##########################
def botton_get_be():
    global list_of_lines
    global list_weight
    global flag
    uinput = entry_begin_rebro.get()
    uinput2 = entry_end_rebro.get()
    if int(uinput) <= 0 or int(uinput2) <= 0 or uinput2 not in dict_of_grah or uinput not in dict_of_grah:
        messagebox.showerror(title="ошибка", message="неверный ввод данных")
        return
    p1 = dict_of_grah[uinput]
    p2 = dict_of_grah[uinput2]
    list_matrix.append([int(uinput), int(uinput2)])
    if var.get() == True and uinput == uinput2:
        x = p1[0]
        y = p1[1]
        canvas.create_oval(x-4, y-4, x+40, y + 40, outline='grey')
        return
    flag += 1
    if var.get() == True:
        if [int(uinput2), int(uinput)] in list_matrix:
            canvas.create_line(p2[0]+11, p2[1]+11, p1[0]+11, p1[1]+11, width=1.5, arrow='both', fill="grey", tags=f"line{flag}", stipple="gray50")
        else:
            canvas.create_line(p1[0]+11, p1[1]+11, p2[0]+11 , p2[1]+11 , width=1.5, arrow='last', fill="grey", tags=f"line{flag}", stipple="gray50")
    elif var.get() == False:
        canvas.create_line(p1[0]+11, p1[1]+11, p2[0] +11, p2[1]+11 , width=1.5, fill="grey", tags=f"line{flag}", stipple="gray50")
    elif var1.get() == True:
        w = entry_weight.get()
        if int(w) <= 0 or w == "":
            messagebox.showerror(title="ошибка", message="неверный ввод данных")
            return
        list_weight[uinput + uinput2] = int(w)
        x = max(p1[0], p2[0])-abs(p1[0] - p2[0] + 10)/2
        y = max(p1[1], p2[1]) - abs(p1[1] - p2[1] + 10)/2
        canvas.create_line(p1[0] + 15, p1[1] + 15, p2[0] + 5, p2[1] + 5, width=1.5, fill="grey", tags=f"line{flag}")
        canvas.create_oval(x-8, y-8, x + 12, y + 12, fill='#F5FFFA', outline='#F5FFFA', tags=f"line{flag}")
        canvas.create_text(x, y, text=w, font="Verdana 13", tags=f"line{flag}")

##########################
def matr():
    if set1 == []:
        return
    max_top = max(set1)
    global matrix
    matrix = [[0 for i in range(max_top)] for j in range(max_top)]
    matrix_text = '\n'
    if var.get() == True:
        for i in list_matrix:
            matrix[i[0] - 1][i[1] - 1] = 1
    else:
        for i in list_matrix:
            matrix[i[0] - 1][i[1] - 1] = 1
            matrix[i[1] - 1][i[0] - 1] = 1
    for k in range(max_top):
        matrix_text += str(k + 1) + ' '
        for j in range(max_top):
            matrix_text += str(matrix[k][j]) + ' '
        matrix_text += '\n'
    return matrix_text

def botton_show_matrix():
    window2 = tk.Toplevel(width=200, height=200)
    window2.title("Матрица смежности")
    global matrix_text
    if len(dict_of_grah) != 0:
        matrix_text = matr()
        t = tk.Text(master=window2)
        t.pack(fill='both', expand=True)
        t.insert("1.0", top)
        t.insert("2.0", matrix_text)

def botton_algorithm():
    start = entry_begin.get()
    end = entry_end.get()
    if int(start) <= 0 or int(end) <= 0 or start not in dict_of_grah or end not in dict_of_grah:
        messagebox.showerror(title="ошибка", message="неверный ввод данных")
        return
    set1 = matr()
    global id
    global path
    if var1.get() == False:
        path = algorithm(matrix, start_node=int(start), end_node=int(end))
    else:
        path = algorithm2(graph=matrix, start_node=int(start), end_node=int(end), list_weight=list_weight)
    if path == None:
        return
    for i in path:
        coord = dict_of_grah[str(i)]
        id1 = canvas.create_oval(coord[0], coord[1], coord[0] + 20, coord[1] + 20, fill='red')
        id2 = canvas.create_text(coord[0] + 10, coord[1] + 10, text=i)
        window.update()
        time.sleep(0.5)
        id.append([id1, id2])
    path_text = to_text()
    result = tk.Label(master=frame_for_result, text=path_text, bg="#4E5754")
    result.grid(row=1, column=0, pady=7, padx=5, sticky='w')

def button_clean_alg():
    for i in id:
        canvas.delete(i[0])
        canvas.delete(i[1])

##########################
canvas.pack(expand=True, padx=5, pady=5)
window.mainloop()
