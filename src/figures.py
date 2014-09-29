# -*- coding: utf-8 -*-


from globals import *
from tools import translate_color, canvas_reset



class Figure:
    def __init__(self, _id, x, y):
        self.id = _id
        self.type = 'None'
        self.x = x * PT #posicion X
        self.y = y #posicion Y


    def is_rect(self):
        """
            Si es un objecto rectangulo
        """
        if self.type == 'Rect':
            return True
        else:
            return False


    def is_text(self):
        """
            Si es un objecto Texto
        """
        if self.type == 'Text':
            return True
        else:
            return False



class Rect(Figure):
    def __init__(self, _id, x, y, w, h, lw=LINEWEIGHT,c=COLOR, sc=STROKECOLOR, bg=BACKGROUNDCOLOR):
        """
            en cuanto a posicion y tamaño se expecifica en pt
        """
        Figure.__init__(self, _id, x, y)
        self.type = 'Rect'
        self.w = w * PT #normalizo el ancho
        self.h = h #alto
        self.lw = lw * PT #ancho de linea normalizado
        self.c = c #color
        self.sc = sc #stroke color
        self.bg = bg #color de fondo o relleno

        self.y = (HEIGHT * PX) - self.y - self.h
        self.y = self.y * PT
        self.h = self.h * PT


    def draw(self, canvas):
        canvas_reset(canvas)#reseteo colores
        #setcolors
        sc = translate_color(self.sc)
        canvas.setStrokeColorRGB(sc[R],sc[G], sc[B])
        #ancho linea
        if self.lw != 0:
            _stroke = 1
            canvas.setLineWidth(self.lw)
        else:
            _stroke=1

        #draw
        if self.bg == "none":
            canvas.rect(self.x, self.y, self.w, self.h, stroke = _stroke)
        else:
            bg = translate_color(self.bg)
            canvas.setFillColorRGB(bg[R], bg[G], bg[B])
            canvas.rect(self.x, self.y, self.w, self.h, stroke = _stroke, fill=1)


    def __str__(self):
        return "RECT(%s %s %s %s | %s %s %s)" %(self.x, self.y, self.w, self.h, self.lw, self.sc, self.bg)



class Label(Figure):
    def __init__(self, _id, x, y, text="", font=FONTFAMILY, size=12, index=False, c=COLOR, sc=STROKECOLOR, bg=BACKGROUNDCOLOR):
        """
            en cuanto a posicion y tamaño se expecifica en pt
        """
        Figure.__init__(self, _id, x, y)
        self.type = 'Text'
        self.font = font
        self.size = size #tamaño texto en pixel
        self.text = text #texto
        self.index = index #si se usara como indice de relleno no imprimira el texto
        self.c = c #color
        self.sc = sc #stroke color
        self.bg = bg #color de fondo o relleno

        self.y = (HEIGHT * PX) - self.y # - self.size
        self.y = self.y * PT
        self.size = self.size * PT


    def draw(self, canvas):
        #si es una etiqueta indice no se dibujara
        if not self.index:
            canvas_reset(canvas)#reseteo colores
            #setcolors
            sc = translate_color(self.sc)
            canvas.setStrokeColorRGB(sc[R],sc[G], sc[B])
            bg = translate_color(self.bg)
            canvas.setFillColorRGB(bg[R], bg[G], bg[B])
            #font configuration
            canvas.setFont(self.font, self.size)
            canvas.drawString(self.x, self.y, self.text)



    def __str__(self):
        return "TEXT (%s %s %s %s)" %(self.x, self.y, self.text, self.size)



class Line(Figure):
    pass



class Elipse(Figure):
    pass
