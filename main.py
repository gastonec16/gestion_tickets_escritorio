from tkinter import Tk
from tkinter.ttk import  Button, Entry, Frame, Label, Notebook, Style
from tkinter.font import Font

#region funciones

def posicionar_formulario(lista_label, lista_entry, column=0, row=1):
    row_label = row
    row_entry = row
    for i in lista_label:
        i.grid(column=column, row=row_label, padx=(24, 8), ipady=3, sticky='e')
        row_label += 1
    for i in lista_entry:
        i.grid(column=column+1, row=row_entry, padx=(8, 24), ipady=3, sticky='we')
        row_entry += 1

def registrarse():
    print('registrarse')

def agregar_area():
    print('agregar área')

#endregion

#region principal

colores = ('#251D3A', '#2A2550', '#E04D01', '#FF7700', 'black', 'white', '#C3C3C3')
tamaño_fuente = [1]

ventana = Tk()
ventana.geometry('960x540')
ventana.minsize(640, 480)
ventana.title('Gestión de Tickets')
ventana.config(bg=colores[0])
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

fuente_titulo = Font(family='Segoe UI', size=int(18*tamaño_fuente[0]), slant='italic')
fuente_pie = Font(family='Segoe UI', size=int(8*tamaño_fuente[0]))
fuente_button = Font(family='Segoe UI', size=int(12*tamaño_fuente[0]), weight='bold')
fuente_label = Font(family='Segoe UI', size=int(12*tamaño_fuente[0]))
fuente_notebook = Font(family='Segoe UI', size=int(14*tamaño_fuente[0]), weight='bold')

estilo = Style()
estilo.theme_use('alt')

estilo.configure("TCombobox", foreground=colores[4])
estilo.configure("TEntry", foreground=colores[4])
estilo.configure("TFrame", background=colores[0])
estilo.configure("TLabel", background=colores[0], foreground=colores[5], font=fuente_label)
estilo.configure("titulo.TLabel", background=colores[0], foreground=colores[6], font=fuente_titulo, justify='center')
estilo.configure("pie.TLabel", background=colores[0], foreground=colores[3], font=fuente_pie)
estilo.configure("TButton", background=colores[2], foreground=colores[5], focuscolor='none', font=fuente_button)
estilo.map('TButton', background=[('active', colores[3])])
estilo.configure("TNotebook", background=colores[1], borderwidth = 0)
estilo.configure("TNotebook.Tab", foreground=colores[1], focuscolor='none', font=fuente_button)
estilo.map('TNotebook.Tab', background=[('selected', colores[0]), ('active', colores[5])],
foreground=[('selected', colores[6])], font=[('selected', fuente_notebook)])

notebook_contenido = Notebook(ventana)
notebook_contenido.grid(column=0, row=0, sticky='nswe')

label_pie = Label(ventana, style='pie.TLabel', text='Municipalidad de Villa Carlos Paz')
label_pie.grid(column=0, row=1, columnspan=2, sticky='w')

#endregion

#region widgets registrarse

frame_registrarse = Frame(notebook_contenido)
frame_registrarse.grid(column=0, row=0, sticky='nswe')
frame_registrarse.columnconfigure(1, weight=1)
frame_registrarse.rowconfigure((0,1,2,3,4,5,6,7,8), weight=1)

label_titulo = Label(frame_registrarse, style='titulo.TLabel', text='Registrarse en el Sistema')
label_titulo.grid(column=0, row=0, columnspan=2)

label_registrarse_nombre = Label(frame_registrarse, text='Nombre *')
label_registrarse_apellido = Label(frame_registrarse, text='Apellido *')
label_registrarse_legajo = Label(frame_registrarse, text='Legajo *')
label_registrarse_email = Label(frame_registrarse, text='Email *')
label_registrarse_usuario = Label(frame_registrarse, text='Nombre de Usuario *')
label_registrarse_contraseña = Label(frame_registrarse, text='Contraseña *')
label_registrarse_repetir = Label(frame_registrarse, text='Repetir Contraseña *')

entry_registrarse_nombre = Entry(frame_registrarse, font=fuente_label)
entry_registrarse_apellido = Entry(frame_registrarse, font=fuente_label)
entry_registrarse_legajo = Entry(frame_registrarse, font=fuente_label)
entry_registrarse_email = Entry(frame_registrarse, font=fuente_label)
entry_registrarse_usuario = Entry(frame_registrarse, font=fuente_label)
entry_registrarse_contraseña = Entry(frame_registrarse, font=fuente_label)
entry_registrarse_repetir = Entry(frame_registrarse, font=fuente_label)

lista_label_registrarse = [label_registrarse_nombre, label_registrarse_apellido, label_registrarse_legajo,
label_registrarse_email, label_registrarse_usuario, label_registrarse_contraseña, label_registrarse_repetir]
lista_entry_registrarse = [entry_registrarse_nombre, entry_registrarse_apellido, entry_registrarse_legajo,
entry_registrarse_email, entry_registrarse_usuario, entry_registrarse_contraseña, entry_registrarse_repetir]

posicionar_formulario(lista_label_registrarse, lista_entry_registrarse)

button_registrarse = Button(frame_registrarse, text='Registrarse', command=registrarse, cursor='hand2')
button_registrarse.grid(column=1, row=8, padx=24, ipadx=16, ipady=6, sticky='e')

notebook_contenido.add(frame_registrarse, text='Registrarse')

#endregion

#region widgets área

frame_area = Frame(notebook_contenido)
frame_area.grid(column=0, row=0, sticky='nswe')
frame_area.columnconfigure(1, weight=1)
frame_area.rowconfigure((0,1,2,3,4), weight=1)

label_titulo = Label(frame_area, style='titulo.TLabel', text='Agregar Área')
label_titulo.grid(column=0, row=0, columnspan=2)

label_area_nombre = Label(frame_area, text='Nombre de Área *')
label_area_telefono = Label(frame_area, text='Teléfono  ')
label_area_email = Label(frame_area, text='Email  ')

entry_area_nombre = Entry(frame_area, font=fuente_label)
entry_area_telefono = Entry(frame_area, font=fuente_label)
entry_area_email = Entry(frame_area, font=fuente_label)

lista_label_area = [label_area_nombre, label_area_telefono, label_area_email]
lista_entry_area = [entry_area_nombre, entry_area_telefono, entry_area_email]

posicionar_formulario(lista_label_area, lista_entry_area)

button_area = Button(frame_area, text='Agregar', command=agregar_area, cursor='hand2')
button_area.grid(column=1, row=4, padx=24, ipadx=16, ipady=6, sticky='e')

notebook_contenido.add(frame_area, text='Áreas')

#endregion

notebook_contenido.add(Frame(), text='Crear Ticket')

ventana.mainloop()