from os import path
from tkinter import PhotoImage, IntVar, StringVar, Tk, Text, Toplevel, messagebox as mb
from tkinter.ttk import Button, Combobox, Entry, Frame, Label, Notebook, Scrollbar, Spinbox, Style, Treeview, Checkbutton
from tkinter.font import Font
from clases import *


# region funciones

def posicionar_formulario(lista_label, lista_entry, button=None, column=0, row=1):
    row_label = row
    row_entry = row
    for i in lista_label:
        i.grid(column=column, row=row_label, padx=(24, 8), ipady=3, sticky='e')
        row_label += 1
    for i in lista_entry:
        i.grid(column=column+1, row=row_entry,
               padx=(8, 24), ipady=3, sticky='ew')
        row_entry += 1
    if button != None:
        button.grid(column=column+1, row=row_entry, padx=24,
                    pady=(12, 8), ipadx=16, ipady=6, sticky='e')


def text_con_scrollbar(frame):

    frame_text = Frame(frame)
    frame_text.columnconfigure(0, weight=1)

    text = Text(frame_text, height=7, width=0, font=fuente_label)
    scrollbar = Scrollbar(frame_text, command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    text.grid(column=0, row=0, sticky='nsew')
    scrollbar.grid(row=0, column=1, sticky='ns')

    return frame_text


def vaciar_entry(lista_entry):
    for i in lista_entry:
        i.delete(0, 'end')

def validar_obligatorios(lista_variables):
    for i in lista_variables:
        if i == '':
            mb.showerror('ERROR', 'Los campos marcados con * son obligatorios')
            return False
    else:
        return True

def actualizar_treeview(clase, treeview):
    treeview.delete(*treeview.get_children())
    for i in clase.mostrar():
        treeview.insert('', 'end', values=i)


def mostrar_usuario():
    global ventana_emergente
    if ventana_emergente != None:
        ventana_emergente.top.destroy()
    ventana_emergente = VentanaEmergente()
    WidgetsModificarUsuario(ventana_emergente.top)

def mostrar_ticket():
    global ventana_emergente
    if ventana_emergente != None:
        ventana_emergente.top.destroy()
    ventana_emergente = VentanaEmergente()
    WidgetsModificarTicket(ventana_emergente.top)

def registrar_usuario():
    nombre = nombre_usuario.get().strip()
    apellido = apellido_usuario.get().strip()
    legajo = legajo_usuario.get().strip()
    email = email_usuario.get().strip()
    nombre_usuarioo = nombre_usuario_usuario.get().strip().lower() # esta variable tiene dos o porque no andaba el get del nombre
    contraseña = contraseña_usuario.get().strip()
    repetir_contraseña = repetir_contraseña_usuario.get().strip()
    
    if '@' not in email:
        mb.showerror('ERROR', 'Ingrese un email válido')
        return
    if len(contraseña) < 4:
        mb.showerror('ERROR', 'Las contraseña no debe tener menos de 4 dígitos')
        return
    if contraseña != repetir_contraseña:
        mb.showerror('ERROR', 'Las contraseñas no coinciden')
        return
    usuario = Usuario()
    for i in usuario.lista_usuarios():
        if i[0] == nombre_usuarioo:
            mb.showerror('ERROR', 'El nombre de usuario ya existe')
            return
    
    if validar_obligatorios((nombre, apellido, legajo, email, nombre_usuarioo, contraseña)):
        usuario.insertar(nombre, apellido, legajo, email, nombre_usuarioo, contraseña)
        vaciar_entry(widgets_registrarse.lista_entry)
        actualizar_treeview(usuario, widgets_usuarios.treeview)


def modificar_usuario():
    global ventana_emergente
    mensaje = mb.askyesno('Modificar Usuario', '¿Seguro desea modificar el usuario?')
    if mensaje == True:
        id_usuario = id_mod_usuario.get()
        nombre = nombre_mod_usuario.get().strip()
        apellido = apellido_mod_usuario.get().strip()
        legajo = legajo_mod_usuario.get().strip()
        email = email_mod_usuario.get().strip()
        activo = activo_mod_usuario.get()
        if validar_obligatorios((nombre, apellido, legajo, email)):
            usuario = Usuario()
            usuario.modificar(id_usuario, nombre, apellido, legajo, email, activo)
            vaciar_entry(widgets_registrarse.lista_entry)
            actualizar_treeview(usuario, widgets_usuarios.treeview)
            ventana_emergente.top.destroy()

def modificar_ticket():
    global ventana_emergente
    # id_usuario = id_mod_usuario.get()
    # nombre = nombre_mod_usuario.get()
    # apellido = apellido_mod_usuario.get()
    # legajo = legajo_mod_usuario.get()
    # email = email_mod_usuario.get()
    # activo = activo_mod_usuario.get()
    # usuario = Usuario()
    # usuario.modificar(id_usuario, nombre, apellido, legajo, email, activo)
    # vaciar_entry(widgets_registrarse.lista_entry)
    # actualizar_treeview(usuario, widgets_usuarios.treeview)
    # ventana_emergente.top.destroy()

# =========================================================================================


def agregar_area():
    nombre = nombre_area.get().strip()
    email = email_area.get().strip()
    telefono = telefono_area.get().strip()
    if validar_obligatorios((nombre,)):
        area = Area()
        area.insertar(nombre, email, telefono)
        vaciar_entry(widgets_areas.lista_entry)
        actualizar_treeview(area, widgets_areas.treeview)


def modificar_area():
    mensaje = mb.askyesno('Modificar Área', '¿Seguro desea modificar el área?')
    if mensaje == True:
        id_area = id_mod_area.get()
        nombre = nombre_mod_area.get().strip()
        email = email_mod_area.get().strip()
        telefono = telefono_mod_area.get().strip()
        if validar_obligatorios(tuple(nombre)):
            area = Area()
            area.modificar(id_area, nombre, email, telefono)
            actualizar_treeview(area, widgets_areas.treeview)


def eliminar_area():
    mensaje = mb.askyesno('Eliminar Área', '¿Seguro desea eliminar el área?')
    if mensaje == True:
        widgets_areas.button_eliminar.config(state='disabled')
        widgets_areas.button_modificar.config(state='disabled')
        id_area = id_mod_area.get()
        area = Area()
        area.eliminar(id_area)
        vaciar_entry(widgets_areas.lista_entry_mod)
        actualizar_treeview(area, widgets_areas.treeview)


def crear_ticket():
    print('crear ticket')

def iniciar_sesion():
    global usuario_actual
    nombre_usuarioo = nombre_usuario_iniciar.get().lower()
    contraseña = contraseña_iniciar.get()
    usuario = Usuario()
    for i in usuario.lista_usuarios():
        if i[0] == nombre_usuarioo:
            usuario.validar_contraseña(nombre_usuarioo, contraseña)
            break
    else:
        mb.showerror('ERROR', 'El nombre de usuario no existe')
        return
    # usuario_actual = Usuario(id_usuario, id_tipo_usuario, nombre, apellido,
    #                          legajo, email, activo, nombre_usuarioo, contraseña)

def crear_pedido():
    print('crear pedido')


def agregar_detalle_pedido():
    print('agregar detalle pedido')


lista_areas = ['Palacio', 'Administracion',
               'Computos', 'Modernizacion', 'Cultura', 'Turismo']

lista_prioridades = ['Baja', 'Media', 'Alta']

lista_tecnicos = ['Oscar', 'Camilo', 'Agustin']

lista_articulos = ['Mouse', 'Teclado', 'Monitor', 'Disco Duro', 'SSD']

lista_estados = []

# endregion

# region principal

carpeta = path.dirname(path.realpath(__file__)[0:-7])
colores = ('#251D3A', '#2A2550', '#E04D01',
           '#FF7700', 'black', 'white', '#C3C3C3')
tamaño_fuente = [1]

ventana = Tk()
# ventana.geometry(f'{ventana.winfo_screenwidth()}x{ventana.winfo_screenheight()}')
ventana.geometry('960x540')
# ventana.geometry('1280x720')
ventana.minsize(640, 480)
ventana.title('Gestión de Tickets')
ventana.config(bg=colores[0])
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)
img_municipalidad = PhotoImage(file=carpeta+'/img/logo_muni.png')
img_municipalidad = img_municipalidad.subsample(2, 2)

fuente_titulo = Font(family='Segoe UI', size=int(18*tamaño_fuente[0]), slant='italic')
fuente_subtitulo = Font(family='Segoe UI', size=int(14*tamaño_fuente[0]))
fuente_pie = Font(family='Segoe UI', size=int(8*tamaño_fuente[0]))
fuente_button = Font(family='Segoe UI', size=int(12*tamaño_fuente[0]), weight='bold')
fuente_label = Font(family='Segoe UI', size=int(12*tamaño_fuente[0]))
fuente_notebook = Font(family='Segoe UI', size=int(14*tamaño_fuente[0]), weight='bold')

estilo = Style()
estilo.theme_use('alt')

estilo.configure('TCombobox', foreground=colores[4], arrowsize=15, arrowcolor=colores[0])
ventana.option_add('*TCombobox*Font', fuente_label)
ventana.option_add('*TCombobox*Listbox*Font', fuente_label)
estilo.configure('TEntry', foreground=colores[4])
ventana.option_add('*TEntry*Font', fuente_label)
estilo.configure('TFrame', background=colores[0])
estilo.configure(
    'TLabel', background=colores[0], foreground=colores[5], font=fuente_label)
estilo.configure(
    'titulo.TLabel', background=colores[0], foreground=colores[6], font=fuente_titulo, justify='center')
estilo.configure(
    'subtitulo.TLabel', background=colores[0], foreground=colores[5], font=fuente_subtitulo, justify='center')
estilo.configure(
    'pie.TLabel', background=colores[0], foreground=colores[3], font=fuente_pie)
estilo.configure(
    'TButton', background=colores[2], foreground=colores[5], focuscolor='none', font=fuente_button)
estilo.map('TButton', background=[('active', colores[3])])
estilo.configure('peligro.TButton', background='red',
                 foreground=colores[5], focuscolor='none', font=fuente_button)
estilo.map('peligro.TButton', background=[('active', colores[3])])
estilo.configure('TNotebook', background=colores[1], borderwidth=0)
estilo.configure(
    'TNotebook.Tab', foreground=colores[1], focuscolor='none', font=fuente_button)
estilo.map('TNotebook.Tab', background=[('selected', colores[0]), ('active', colores[5])],
           foreground=[('selected', colores[6])], font=[('selected', fuente_notebook)])
estilo.configure(
    'Treeview', background=colores[5], foreground=colores[4], font=fuente_label)
estilo.configure('Treeview.Heading', background=colores[6], font=fuente_button)
estilo.configure('TScrollbar', arrowsize=15, arrowcolor=colores[0])
estilo.configure(
    'TSpinbox', foreground=colores[4], arrowsize=15, arrowcolor=colores[0])
ventana.option_add('*TSpinbox*Font', fuente_label)
estilo.configure(
    'TCheckbutton', background=colores[0], foreground=colores[4], font=fuente_label)
estilo.map('TCheckbutton', background=[('active', colores[0])])


notebook_contenido = Notebook(ventana)
notebook_contenido.grid(column=0, row=0, sticky='nsew')

label_pie = Label(ventana, style='pie.TLabel',
                  text='Municipalidad de Villa Carlos Paz')
label_pie.grid(column=0, row=1, columnspan=2, sticky='w')

# endregion

# region variables

usuario_actual = None
#=============================
nombre_area = StringVar()
email_area = StringVar()
telefono_area = StringVar()
id_mod_area = IntVar()
nombre_mod_area = StringVar()
email_mod_area = StringVar()
telefono_mod_area = StringVar()
# ===================================
id_mod_usuario = IntVar()
nombre_usuario = StringVar()
apellido_usuario = StringVar()
legajo_usuario = StringVar()
email_usuario = StringVar()
nombre_usuario_usuario = StringVar()
contraseña_usuario = StringVar()
repetir_contraseña_usuario = StringVar()
nombre_mod_usuario = StringVar()
apellido_mod_usuario = StringVar()
legajo_mod_usuario = StringVar()
email_mod_usuario = StringVar()
nombre_usuario_mod_usuario = StringVar()
contraseña_mod_usuario = StringVar()
activo_mod_usuario = IntVar()
# ==========================================
nombre_usuario_iniciar = StringVar()
contraseña_iniciar = StringVar()
# endregion

# region widgets


class WidgetsRegistrarse:
    def __init__(self):

        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure((1, 2, 3, 4, 5, 6, 7), weight=1)

        self.label_img_municipalidad = Label(
            self.frame, image=img_municipalidad)
        self.label_img_municipalidad.grid(column=2, row=1, rowspan=8)

        self.label_titulo = Label(
            self.frame, style='titulo.TLabel', text='Registrarse en el Sistema')
        self.label_titulo.grid(column=0, row=0, columnspan=3)

        self.lista_label = [
            Label(self.frame, text='Nombre *'),
            Label(self.frame, text='Apellido *'),
            Label(self.frame, text='Legajo *'),
            Label(self.frame, text='Email *'),
            Label(self.frame, text='Nombre de Usuario *'),
            Label(self.frame, text='Contraseña *'),
            Label(self.frame, text='Repetir Contraseña *')
        ]
        self.lista_entry = [
            Entry(self.frame, textvariable=nombre_usuario),
            Entry(self.frame, textvariable=apellido_usuario),
            Entry(self.frame, textvariable=legajo_usuario),
            Entry(self.frame, textvariable=email_usuario),
            Entry(self.frame, textvariable=nombre_usuario_usuario),
            Entry(self.frame, show='*', textvariable=contraseña_usuario),
            Entry(self.frame, show='*', textvariable=repetir_contraseña_usuario)
        ]

        self.button_registrarse = Button(
            self.frame, text='Registrarse', command=registrar_usuario, cursor='hand2')

        posicionar_formulario(
            self.lista_label, self.lista_entry, self.button_registrarse)

        notebook_contenido.add(self.frame, text='Registrarse')


class WidgetsIniciarSesion:
    def __init__(self):

        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure((1, 2, 3, 4, 5), weight=1)

        self.label_img_municipalidad = Label(self.frame, image=img_municipalidad)
        self.label_img_municipalidad.grid(column=2, row=1, rowspan=8)

        self.label_titulo = Label(self.frame, style='titulo.TLabel', text='Registrarse en el Sistema')
        self.label_titulo.grid(column=0, row=0, columnspan=3)

        self.lista_label = [
            Label(self.frame),
            Label(self.frame, text='Nombre de Usuario *'),
            Label(self.frame, text='Contraseña *'),
            Label(self.frame),
            Label(self.frame)
        ]
        self.lista_entry = [
            Label(self.frame),
            Entry(self.frame, textvariable=nombre_usuario_iniciar),
            Entry(self.frame, show='*', textvariable=contraseña_iniciar),
            Label(self.frame),
            Label(self.frame)
        ]

        self.button_iniciar_sesion = Button(self.frame, text='Iniciar Sesión', command=iniciar_sesion, cursor='hand2')

        posicionar_formulario(
            self.lista_label, self.lista_entry, self.button_iniciar_sesion)

        notebook_contenido.add(self.frame, text='Iniciar Sesión')


class WidgetsUsuarios:
    def __init__(self):

        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

        self.label_titulo = Label(self.frame, style='titulo.TLabel', text='Usuarios')
        self.label_titulo.grid(column=0, row=0)

        self.frame_treeview = Frame(self.frame)
        self.frame_treeview.grid(
            column=0, row=1, padx=24, pady=(12, 8), sticky='nsew')
        self.frame_treeview.columnconfigure(0, weight=1)
        self.frame_treeview.rowconfigure(0, weight=1)

        self.columnas = ('id', 'tipo_usuario', 'nombre', 'apellido', 'legajo',
                         'email', 'activo', 'nombre_usuario')

        self.treeview = Treeview(self.frame_treeview, columns=self.columnas, height=20, show='headings')

        self.treeview.heading('id', text='ID')
        self.treeview.heading('tipo_usuario', text='Tipo de usuario')
        self.treeview.heading('nombre', text='Nombre')
        self.treeview.heading('apellido', text='Apellido')
        self.treeview.heading('legajo', text='Legajo')
        self.treeview.heading('email', text='Email')
        self.treeview.heading('activo', text='Activo')
        self.treeview.heading('nombre_usuario', text='Nombre de Usuario')

        self.treeview.column('id', minwidth=40, width=0)
        self.treeview.column('tipo_usuario', minwidth=40, width=0)
        self.treeview.column('nombre', minwidth=40, width=0)
        self.treeview.column('apellido', minwidth=40, width=0)
        self.treeview.column('legajo', minwidth=40, width=0)
        self.treeview.column('email', minwidth=40, width=0)
        self.treeview.column('activo', minwidth=40, width=0)
        self.treeview.column('nombre_usuario', minwidth=40, width=0)

        self.treeview.grid(column=0, row=0, sticky='nsew')

        self.scrollbar = Scrollbar( self.frame_treeview, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        self.button_modificar = Button(self.frame, text='Modificar', command=mostrar_usuario, state='disabled', cursor='hand2')
        self.button_modificar.grid(column=0, row=2, padx=24, pady=(12, 8), ipadx=16, ipady=6, sticky='e')

        actualizar_treeview(Usuario(), self.treeview)

        self.lista_variables_mod = [None, None, nombre_mod_usuario, apellido_mod_usuario, legajo_mod_usuario,
                                    email_mod_usuario, activo_mod_usuario, nombre_usuario_mod_usuario]

        def item_seleccionado(event):
            self.button_modificar.config(state='normal')
            try:
                for i in self.treeview.selection():
                    item = self.treeview.item(i)
                    record = item['values']
                    id_mod_usuario.set(record[0])
                for i in range(len(self.lista_variables_mod)):
                    if self.lista_variables_mod[i] != None:
                        self.lista_variables_mod[i].set(record[i])
            except:
                pass

        self.treeview.bind('<<TreeviewSelect>>', item_seleccionado)

        notebook_contenido.add(self.frame, text='Usuarios')


class WidgetsModificarUsuario:
    def __init__(self, toplevel):

        self.frame = Frame(toplevel)
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure((1, 2, 3, 4, 5, 6), weight=1)

        self.label_img_municipalidad = Label(
            self.frame, image=img_municipalidad)
        self.label_img_municipalidad.grid(column=2, row=1, rowspan=8)

        self.label_titulo = Label(self.frame, style='titulo.TLabel', text='Modificar Usuario')
        self.label_titulo.grid(column=0, row=0, columnspan=3)
        self.label_nombre_usuario = Label(self.frame, style='subtitulo.TLabel', text=nombre_usuario_mod_usuario.get())
        self.label_nombre_usuario.grid(column=0, row=1, columnspan=3)

        self.lista_label = [
            Label(self.frame, text='Nombre *'),
            Label(self.frame, text='Apellido *'),
            Label(self.frame, text='Legajo *'),
            Label(self.frame, text='Email *'),
            Label(self.frame, text='Activo *')

        ]
        self.lista_entry = [
            Entry(self.frame, textvariable=nombre_mod_usuario),
            Entry(self.frame, textvariable=apellido_mod_usuario),
            Entry(self.frame, textvariable=legajo_mod_usuario),
            Entry(self.frame, textvariable=email_mod_usuario),
            Checkbutton(self.frame, text='',
                        variable=activo_mod_usuario)

        ]

        self.button_aceptar = Button(
            self.frame, text='aceptar', command=modificar_usuario, cursor='hand2')

        posicionar_formulario(self.lista_label, self.lista_entry, self.button_aceptar, row=2)


class WidgetsAreas:
    def __init__(self):

        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure(0, weight=5)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure((1, 2, 3, 4, 7, 8, 9), weight=1)

        self.label_titulo = Label(self.frame, style='titulo.TLabel', text='Áreas')
        self.label_titulo.grid(column=0, row=0, columnspan=3)

        self.frame_treeview = Frame(self.frame)
        self.frame_treeview.grid(column=0, row=1, rowspan=10, padx=24, pady=(12, 8), sticky='nsew')
        self.frame_treeview.columnconfigure(0, weight=1)
        self.frame_treeview.rowconfigure(0, weight=1)

        self.columnas = ('id', 'nombre', 'email', 'telefono')

        self.treeview = Treeview(self.frame_treeview, columns=self.columnas, height=20, show='headings')

        self.treeview.heading('id', text='ID')
        self.treeview.heading('nombre', text='Nombre')
        self.treeview.heading('email', text='Email')
        self.treeview.heading('telefono', text='Teléfono')

        self.treeview.column('id', minwidth=40, width=0)
        self.treeview.column('nombre', minwidth=40, width=0)
        self.treeview.column('email', minwidth=40, width=0)
        self.treeview.column('telefono', minwidth=40, width=0)

        self.treeview.grid(column=0, row=0, sticky='nsew')

        self.scrollbar = Scrollbar(self.frame_treeview, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        # 2ª columna

        self.lista_label_mod = [
            Label(self.frame, text='Nombre de Área *'),
            Label(self.frame, text='Email  '),
            Label(self.frame, text='Teléfono  ')
        ]
        self.lista_entry_mod = [
            Entry(self.frame, textvariable=nombre_mod_area),
            Entry(self.frame, textvariable=email_mod_area),
            Entry(self.frame, textvariable=telefono_mod_area)
        ]

        self.frame_button = Frame(self.frame)
        self.frame_button.columnconfigure((0, 1), weight=1)

        self.button_modificar = Button(self.frame_button, text='Modificar', command=modificar_area, state='disabled', cursor='hand2')
        self.button_modificar.grid(column=1, row=0, ipadx=16, ipady=6, sticky='e')
        self.button_eliminar = Button(self.frame_button, style='peligro.TButton', text='Eliminar', command=eliminar_area, state='disabled', cursor='hand2')
        self.button_eliminar.grid(column=0, row=0, ipadx=16, ipady=6, sticky='w')

        posicionar_formulario(self.lista_label_mod, self.lista_entry_mod, self.frame_button, column=1)

        self.label_nueva = Label( self.frame, style='titulo.TLabel', text='Nueva Área')
        self.label_nueva.grid(column=1, row=6, columnspan=2)

        self.lista_label = [
            Label(self.frame, text='Nombre de Área *'),
            Label(self.frame, text='Email  '),
            Label(self.frame, text='Teléfono  ')
        ]
        self.lista_entry = [
            Entry(self.frame, textvariable=nombre_area),
            Entry(self.frame, textvariable=email_area),
            Entry(self.frame, textvariable=telefono_area)
        ]

        actualizar_treeview(Area(), self.treeview)

        self.lista_variables_mod = [
            None, nombre_mod_area, email_mod_area, telefono_mod_area]

        def item_seleccionado(event):
            try:
                for i in self.treeview.selection():
                    item = self.treeview.item(i)
                    record = item['values']
                    id_mod_area.set(record[0])
                for i in range(len(self.lista_variables_mod)):
                    if self.lista_variables_mod[i] != None:
                        self.lista_variables_mod[i].set(record[i])
                self.button_eliminar.config(state='normal')
                self.button_modificar.config(state='normal')
            except:
                pass

        self.treeview.bind('<<TreeviewSelect>>', item_seleccionado)

        self.button_agregar = Button(
            self.frame, text='Agregar', command=agregar_area, cursor='hand2')

        posicionar_formulario(self.lista_label, self.lista_entry,
                              self.button_agregar, column=1, row=7)

        notebook_contenido.add(self.frame, text='Áreas')


class WidgetsCrearTicket:
    def __init__(self):

        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure((1, 2), weight=1)
        self.frame.rowconfigure((1, 2, 3, 4, 5, 6), weight=1)

        self.label_titulo = Label(
            self.frame, style='titulo.TLabel', text='Nuevo Ticket')
        self.label_titulo.grid(column=0, row=0, columnspan=2)

        self.lista_label = [
            Label(self.frame, text='Asunto *'),
            Label(self.frame, text='Área *'),
            Label(self.frame, text='Prioridad *'),
            Label(self.frame, text='Código Hardware  '),
            Label(self.frame, text='Técnico  '),
            Label(self.frame, text='Detalle *')
        ]

        self.lista_entry = [
            Entry(self.frame),
            Combobox(self.frame, values=lista_areas, state='readonly'),
            Combobox(self.frame, values=lista_prioridades, state='readonly'),
            Entry(self.frame),
            Combobox(self.frame, values=lista_tecnicos, state='readonly'),
            text_con_scrollbar(self.frame)
        ]

        self.button_crear = Button(
            self.frame, text='Crear', command=crear_ticket, cursor='hand2')

        posicionar_formulario(
            self.lista_label, self.lista_entry, self.button_crear)

        notebook_contenido.add(self.frame, text='Crear Ticket')


class WidgetsMostrarTickets:
    def __init__(self):
        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

        self.label_titulo = Label(
            self.frame, style='titulo.TLabel', text='Tickets')
        self.label_titulo.grid(column=0, row=0, columnspan=2)

        self.frame_treeview = Frame(self.frame)
        self.frame_treeview.grid(
            column=0, row=1, padx=24, pady=(12, 8), sticky='nsew')
        self.frame_treeview.columnconfigure(0, weight=1)
        self.frame_treeview.rowconfigure(0, weight=1)

        self.columnas = ('numero', 'nombre', 'area', 'asunto',
                         'estado', 'fecha_inicio', 'ultima_respuesta')

        self.treeview = Treeview(
            self.frame_treeview, columns=self.columnas, height=20, show='headings')

        self.treeview.heading('numero', text='Nº')
        self.treeview.heading('nombre', text='Nombre')
        self.treeview.heading('area', text='Área')
        self.treeview.heading('asunto', text='Asunto')
        self.treeview.heading('estado', text='Estado')
        self.treeview.heading('fecha_inicio', text='Fecha Inicio')
        self.treeview.heading('ultima_respuesta', text='Última Respuesta')

        self.treeview.column('numero', minwidth=40, width=0)
        self.treeview.column('nombre', minwidth=40, width=0)
        self.treeview.column('area', minwidth=40, width=0)
        self.treeview.column('asunto', minwidth=40)
        self.treeview.column('estado', minwidth=40, width=0)
        self.treeview.column('fecha_inicio', minwidth=40, width=0)
        self.treeview.column('ultima_respuesta', minwidth=40, width=0)

        # datos ejemplo
        ejemplos = []
        for i in range(1, 101):
            ejemplos.append((f'#{i}', f'Nombre {i}', f'Área {i}', f'Asunto {i}',
                            f'Estado {i}', f'Fecha Inicio {i}', f'Última Modificación {i}'))
        for i in ejemplos:
            self.treeview.insert('', 'end', values=i)

        def item_seleccionado(event):
            self.button_modificar.config(state='normal')
            try:
                for i in self.treeview.selection():
                    item = self.treeview.item(i)
                    record = item['values']
                    print(', '.join(record))
            except:
                pass

        self.treeview.bind('<<TreeviewSelect>>', item_seleccionado)

        self.treeview.grid(column=0, row=0, sticky='nsew')

        self.scrollbar = Scrollbar(self.frame_treeview, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        self.button_modificar = Button(self.frame, text='Modificar', command=mostrar_ticket, state='disabled', cursor='hand2')
        self.button_modificar.grid(column=0, row=2, padx=24, pady=(12, 8), ipadx=16, ipady=6, sticky='e')

        notebook_contenido.add(self.frame, text='Mostrar Tickets')


class WidgetsModificarTicket:
    def __init__(self, toplevel):

        self.frame = Frame(toplevel)
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure(1, weight=2)
        self.frame.columnconfigure((1,3,5), weight=1)
        self.frame.rowconfigure((1,2,3,4,5,6,7,8,9,10,11,12), weight=1)

        self.label_titulo = Label(self.frame, style='titulo.TLabel', text='Modificar Ticket')
        self.label_titulo.grid(column=0, row=0, columnspan=6)

        self.label_asunto = Label(self.frame, style='subtitulo.TLabel', text='No me funciona el monitor ahhh')
        self.label_asunto.grid(column=0, row=1, columnspan=4, padx=24)

        self.label_fecha = Label(self.frame, text='22/07/2022 10:35')
        self.label_fecha.grid(column=4, row=1, padx=(24,8))

        self.combobox_estado = Combobox(self.frame, state='readonly')
        self.combobox_estado.grid(column=5, row=1, padx=(8,24), ipady=3, sticky='ew')

        self.lista_label = [
            Label(self.frame, text='Usuario *'),
            Label(self.frame, text='Área *')
        ]
        self.lista_entry = [
            Entry(self.frame, textvariable=nombre_mod_usuario),
            Entry(self.frame, textvariable=apellido_mod_usuario)
        ]
        self.lista_label_2 = [
            Label(self.frame, text='Tipo Problema *'),
            Label(self.frame, text='Código Hardware  ')
        ]
        self.lista_entry_2 = [
            Entry(self.frame, textvariable=nombre_mod_usuario),
            Entry(self.frame, textvariable=apellido_mod_usuario)
        ]
        self.lista_label_3 = [
            Label(self.frame, text='Prioridad *'),
            Label(self.frame, text='Técnico  ')
        ]
        self.lista_entry_3 = [
            Entry(self.frame, textvariable=nombre_mod_usuario),
            Entry(self.frame, textvariable=apellido_mod_usuario)
        ]
        self.button_aceptar = Button(
            self.frame, text='aceptar', command=modificar_ticket, cursor='hand2')

        posicionar_formulario(self.lista_label, self.lista_entry, row=2)
        posicionar_formulario(self.lista_label_2, self.lista_entry_2, column=2, row=2)
        posicionar_formulario(self.lista_label_3, self.lista_entry_3, column=4, row=2)


class WidgetsCrearPedido():
    def __init__(self):

        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure((1, 3), weight=1)
        self.frame.rowconfigure((1, 2, 3, 4, 5, 6), weight=1)

        self.label_titulo = Label(
            self.frame, style='titulo.TLabel', text='Nuevo Pedido de Abastecimiento')
        self.label_titulo.grid(column=0, row=0, columnspan=4)

        self.lista_label = [
            Label(self.frame, text='Artículo *'),
            Label(self.frame, text='Modelo *'),
            Label(self.frame, text='Cantidad *'),
            Label(self.frame, text='Descripción  ')
        ]

        self.frame_descripcion = Frame(self.frame)
        self.frame_descripcion.columnconfigure(0, weight=1)

        self.lista_entry = [
            Combobox(self.frame, values=lista_articulos, state='readonly'),
            Entry(self.frame),
            Spinbox(self.frame, from_=1, to=9999),
            text_con_scrollbar(self.frame)
        ]

        self.button_agregar_detalle = Button(
            self.frame, text='Agregar', command=agregar_detalle_pedido, cursor='hand2')

        posicionar_formulario(self.lista_label, self.lista_entry,
                              self.button_agregar_detalle, row=3)

        # 2ª columna

        self.lista_label_detalle = [
            Label(self.frame, text='Ticket Nº'),
            Label(self.frame, text='Código de Pedido *')
        ]

        self.lista_entry_detalle = [
            Entry(self.frame, state='readonly'),
            Entry(self.frame)
        ]

        posicionar_formulario(self.lista_label_detalle,
                              self.lista_entry_detalle, column=2, row=1)

        self.frame_detalle = Frame(self.frame)
        self.frame_detalle.grid(
            column=2, row=3, columnspan=2, rowspan=4, padx=24, pady=(12, 8), sticky='nsew')
        self.frame_detalle.columnconfigure(0, weight=1)
        self.frame_detalle.rowconfigure(0, weight=1)

        self.columnas = ('articulo', 'modelo', 'cantidad', 'descripcion')

        self.treeview = Treeview(
            self.frame_detalle, columns=self.columnas, height=0, show='headings')

        self.treeview.heading('articulo', text='Artículo')
        self.treeview.heading('modelo', text='Modelo')
        self.treeview.heading('cantidad', text='Cantidad')
        self.treeview.heading('descripcion', text='Descripción')

        self.treeview.column('articulo', minwidth=40, width=0)
        self.treeview.column('modelo', minwidth=40, width=0)
        self.treeview.column('cantidad', minwidth=40, width=0)
        self.treeview.column('descripcion', minwidth=40)

        def item_seleccionado(event):
            for i in self.treeview.selection():
                item = self.treeview.item(i)
                record = item['values']
                print(', '.join(record))

        self.treeview.bind('<<TreeviewSelect>>', item_seleccionado)

        self.treeview.grid(column=0, row=0, sticky='nsew')

        self.scrollbar = Scrollbar(
            self.frame_detalle, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        self.button_crear = Button(
            self.frame, text='Crear', command=crear_pedido, cursor='hand2')
        self.button_crear.grid(column=3, row=7, padx=24, pady=(
            12, 8), ipadx=16, ipady=6, sticky='e')

        notebook_contenido.add(self.frame, text='Crear Pedido')


class VentanaEmergente:
    def __init__(self):
        self.top = Toplevel(ventana)
        self.top.config()
        self.top.geometry('800x600')
        self.top.title('Modificacion Usuario')
        self.top.columnconfigure(0, weight=1)
        self.top.rowconfigure(0, weight=1)

class UsuarioActual:
    def __init__(self, id_usuario, id_tipo_usuario, nombre, apellido,
                 legajo, email, activo, nombre_usuario, contraseña):
        self.id_usuario = id_usuario
        self.id_tipo_usuario = id_tipo_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.email = email
        self.activo = activo
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

# endregion

ventana_emergente = None
widgets_iniciar_sesion = WidgetsIniciarSesion()
widgets_registrarse = WidgetsRegistrarse()
widgets_areas = WidgetsAreas()
widgets_crear_ticket = WidgetsCrearTicket()
widgets_mostrar_tickets = WidgetsMostrarTickets()
widgets_crear_pedido = WidgetsCrearPedido()
widgets_usuarios = WidgetsUsuarios()

ventana.mainloop()
