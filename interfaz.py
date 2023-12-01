#importamos todo tkinter
from tkinter import *
#importamos font de tkinter
from tkinter import font
#importamos nuestras constantes de colores del archivo config
import config as cons
#importamos las funciones
from funciones import *

#creamos nuestra clase heredando la clase tk para hacer uso de sus metohodod y atributos
class InterfazCalculadora(Tk):
  #inicializmaos construyendo el padre
  def __init__(self):
    super().__init__()
    #aqui tenemos que llamar todos los metodos que vamos a queres que se auto ejecuten al iniciar el proyecto
    self.configura_ventana()
    self.construir_widget()
    self.boton_cambio_tema()
  #definimos nuestor metodo que configura nuestra ventana principal de la calculadora
  def configura_ventana(self):
    #configuracion inical de mi ventana
    # le damos un titulo
    self.title("Calculadora Avanzada")
    #configuramos el color con nuestras constantes del archivo config
    #color de fondo
    self.configure(bg=cons.COLOR_FONDO_NEGRO)
    self.resizable(0,0)
    #vamos a asignarle una transparencia
    self.attributes("-alpha", 0.96)
    w,h=370,570
    cons.centrar_ventana(self,w,h)
  #creacion de widgets elementos dentro de la ventana
  def construir_widget(self):
    #etiqueta que mostrara toda la operacion
    self.operacion_label = Label(self,text="",font=('Arial',16),fg=cons.COLOR_TEXTO_NEGRO,bg=cons.COLOR_FONDO_NEGRO,justify='right')
    self.operacion_label.grid(row=0, column=3,padx=10,pady=10)

    #caja de texto donde se realizara las operaciones
    self.caja_operacion=Entry(self, width=12,font=('Arial',40),bd=0,fg=cons.COLOR_TEXTO_NEGRO,bg=cons.COLOR_FONDO_NEGRO,justify='right')
    self.caja_operacion.grid(row=1,column=0,columnspan=4,padx=10,pady=10)

    #creacion de botones
    #los generamos a partir de una matriz ya que los botones tienen las mismos espacion y medidas
    botones=[
      "C","%","<","/",
      "7","8","9","*",
      "4","5","6","-",
      "1","2","3","+",
      "0",".","=",
    ]
    row_ini=2 #comenzamos de la fila 2
    col_ini=0
    #configramos tipo de fuente para los botones
    robot_font=font.Font(family="Roboto",size=16)

    #le asignamos en cada iteracion la creacion de un boton en base a nuestra matriz botones
    for boton in botones:
      #diferenciar los botones especiales d elos normales para asignarles un estilo distinto
      if boton in ["=","*","/","-","+","C","<","%"]:
        color_fondo=cons.COLOR_BOTONES_ESPECIAL_NEGRO
        boton_font=font.Font(size=16,weight='bold')
      else:
        color_fondo=cons.COLOR_BOTONES_NEGRO
        boton_font=robot_font
      # ahcer que nuestro boton de igual abraque dos columna
      if boton == "=":
        Button(self, text=boton, width=11,height=2,command=lambda b=boton:enviar_boton(self,b),bg=color_fondo,fg=cons.COLOR_TEXTO_NEGRO,relief=FLAT,font=boton_font,padx=5,pady=5,bd=0,borderwidth=0,highlightthickness=0,overrelief='flat').grid(row=row_ini,column=col_ini,columnspan=2,pady=5)
        col_ini += 1
      else:
        Button(self, text=boton, width=5,height=2,command=lambda b=boton:enviar_boton(self,b),bg=color_fondo,fg=cons.COLOR_TEXTO_NEGRO,relief=FLAT,font=boton_font,padx=5,pady=5,bd=0,borderwidth=0,highlightthickness=0,overrelief='flat').grid(row=row_ini,column=col_ini,pady=5)
        col_ini += 1
      if col_ini>3:
        col_ini=0
        row_ini += 1
  #boton modo oscuro
  def boton_cambio_tema(self):
    self.tema_oscuro=True
    font_icono=font.Font(family='FontAwesone',size=12)
    self.boton_tema=Button(self,text="Modo Oscuro \uf186",width=13,font=font_icono, bd=0, borderwidth=0,highlightthickness=0, relief=FLAT, command=lambda:cambio_tema(self,cons),bg=cons.COLOR_BOTONES_ESPECIAL_LIGHT)
    self.boton_tema.grid(row=0,column=0,columnspan=2,pady=0,padx=0, sticky='nw')