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



def get_font_family(family='Sans', weight='normal', style='italic'):
    """
        Obtiene una fuente que mejor se adapte de las que estan definidas en 
        globals, busca tanto entre fuentes de usuario como genericas.
    """
    user_font = False #bandera que demarca que se usa una fuente de usuario
    if family not in FONTS_FAMILY and family not in USER_FONTS: #fuente no soportada -.-
        #como la fuente no es soportada trato de asignar alguna de las por Defecto
        #que mejor se adapte
        if 'serif' in family.lower():
            family = 'Times'
        elif 'mono' in family.lower():
            family = 'Courier'
        else:
            family = 'Default'

    elif family in USER_FONTS:
        user_font = True
    
    _type = 'normal'
    if weight == 'bold':
        if style == 'italic':
            _type = 'bold-italic'
        else:
            _type = 'bold'
    if style == 'italic':
        _type = 'italic'

    
    if user_font:
        if _type not in USER_FONTS[family]: #tipo fuente solicitado no definidio
            _type = 'normal'
        return USER_FONTS[family][_type][0]

    else:
        font = FONTS_FAMILY[family]
        return FONTS[font][_type]

