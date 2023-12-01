from tkinter import *
def enviar_boton(ventana,valor):
  if valor == "=":
    try:
      expression=ventana.caja_operacion.get().replace('%','/100')
      result=eval(expression)
      ventana.caja_operacion.delete(0,END)
      ventana.caja_operacion.insert(0,str(result))
      operacion=expression+" "+valor
      ventana.operacion_label.config(text=operacion)
    except Exception as a:
      ventana.caja_operacion.delete(0,END)
      ventana.caja_operacion.insert(0,"error")
      ventana.operacion_label.config(text="")
  elif valor == "C":
    ventana.caja_operacion.delete(0,END)
    ventana.operacion_label.config(text="")
  elif valor == "<":
    valor_actual=ventana.caja_operacion.get()
    if valor_actual:
      nuevo_valor=valor_actual[:-1]#elimina el ultimo caracter
      ventana.caja_operacion.delete(0,END)
      ventana.caja_operacion.insert(0,nuevo_valor)
      #actualizar la ventana que muestra la operacion
      ventana.operacion_label.config(text=nuevo_valor+" ")
  else:
    valor_actual=ventana.caja_operacion.get()
    ventana.caja_operacion.delete(0,END)
    ventana.caja_operacion.insert(0,valor_actual+valor)
    if valor == "=":
      ventana.operacion_label.config(text="")

def cambio_tema(ventana,colores):
  if ventana.tema_oscuro:
    ventana.configure(bg=colores.COLOR_FONDO_LIGHT)
    ventana.caja_operacion.config(fg=colores.COLOR_TEXTO_LIGHT,bg=colores.COLOR_CAJA_TEXTO_LIGHT)
    ventana.operacion_label.config(fg=colores.COLOR_TEXTO_LIGHT, bg=colores.COLOR_FONDO_LIGHT)
    ventana.boton_tema.configure(text="\uf185 Modo Claro", relief=SUNKEN, bg=colores.COLOR_BOTONES_ESPECIAL_LIGHT)
  else:
    ventana.configure(bg=colores.COLOR_FONDO_NEGRO)
    ventana.caja_operacion.config(fg=colores.COLOR_TEXTO_NEGRO,bg=colores.COLOR_CAJA_TEXTO_NEGRO)
    ventana.operacion_label.config(fg=colores.COLOR_TEXTO_NEGRO, bg=colores.COLOR_FONDO_NEGRO)
    ventana.boton_tema.configure(text="Modo Oscuro \uf186", relief=RAISED, bg=colores.COLOR_BOTONES_ESPECIAL_LIGHT)
  ventana.tema_oscuro=not ventana.tema_oscuro
    