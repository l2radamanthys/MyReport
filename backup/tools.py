# -*- coding: utf-8 -*-

from globals import *


def translate_color(color="#000000"):
    """
        Define el color del usando un formato hexadecimal
        retorna una tupla (r,g,b)
    """
    if len(color) == 6: # -> RRGGBB sin almohadilla
        #conversion a entero
        r = int(color[:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        #convertimos a flotante
        r = round(float(r) / 255, 3)
        g = round(float(g) / 255, 3)
        b = round(float(b) / 255, 3)
        return (r, g, b)

    elif len(color) == 7:  # -> #RRGGBB
        color = color[1:]
        #conversion a entero
        r = int(color[:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        #convertimos a flotante
        r = round(float(r) / 255, 3)
        g = round(float(g) / 255, 3)
        b = round(float(b) / 255, 3)
        return (r, g, b)

    else:
        #en caso de error retorna negro
        return (0, 0, 0)




def canvas_reset(canvas):
    #resetea las configuraciones
    sc = translate_color(STROKECOLOR)
    canvas.setStrokeColorRGB(sc[R],sc[G], sc[B])
    bg = translate_color(BACKGROUNDCOLOR)
    canvas.setFillColorRGB(bg[R], bg[G], bg[B])
    canvas.setLineWidth(LINEWEIGHT * PT)
    canvas.setFont(FONTFAMILY, FONTSIZE)