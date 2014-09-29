# -*- coding: utf-8 -*-

import copy
from xml.dom import minidom

import figures
from globals import PT

class Parser:
    def __init__(self, file):
        self.data = minidom.parse(file)
        self.rects = []
        self.labels = []
        self.pages = []


    def rect_style_parse(self, rect, string):
        style = string.split(";")
        for ele in style:
            key,value = ele.split(":")

            if key == "fill": # color relleno
                rect.bg = value

            if key == "stroke":  #color de linea
                rect.sc = value

            if key == "stroke-width": #ancho de linea
                rect.lw = float(value) * PT #estandarizamos a pt

            if key == "stroke-miterlimit": #no compatible
                pass

            if key == "stroke-dasharray": #no compatible
                pass

        return rect


    def label_style_parse(self, label, string):
        style = string.split(";")
        for ele in style:
            key,value = ele.split(":")
            #print key,value
            if key == "font-size":
                label.size = float(value[:2]) * PT

            if key == "font-weight":
                pass

            if key == "fill":
                label.bg = value

        return label


    def parse_rect(self, rect):
        _id = rect.getAttribute("id")
        x = float(rect.getAttribute("x"))
        y = float(rect.getAttribute("y"))
        w = float(rect.getAttribute("width"))
        h = float(rect.getAttribute("height"))
        style = rect.getAttribute("style")
        obj = figures.Rect(_id, x, y, w, h)
        obj = self.rect_style_parse(obj, style)
        self.rects.append(obj)


    def parse_label(self, label):
        _id = label.getAttribute("id")
        x = float(label.getAttribute("x"))
        y = float(label.getAttribute("y"))
        span = label.getElementsByTagName('tspan')[0]
        txt = span.childNodes[0].toxml()
        style = label.getAttribute("style")
        obj = figures.Label(_id, x, y, txt)
        obj = self.label_style_parse(obj, style)
        self.labels.append(obj)


    def parse(self):
        for rect in self.data.getElementsByTagName("rect"):
            self.parse_rect(rect)

        for label in self.data.getElementsByTagName("text"):
            self.parse_label(label)


    def find_label_by_id(self, _id):
        """
            busca un objecto label mediante su clave, devuelve
            el primer con ella
        """
        search = True
        i = 0
        while search:
            if i == len(self.labels):
                break;

            if self.labels[i].id == _id:
                return self.labels[i]
                search = False
            #print self.labels[i].id
            i += 1
        if search:
            return None


    def set_index(self, list):
        """
            Define las Etiqueta como indice, osea etiquetas que no se dibujaran
        """
        for key in list:
            self.find_label_by_id(key).index = True



    def find_label_by_text(self, txt):
        pass


    def list_parse(self, data, link, end_id=None, space=0):
        """
            Parsea una lista de Valores creando los Elementos Correspondientes
        """
        _id = link[0][0]
        obj = self.find_label_by_id(_id)
        start = obj.y
        delta = obj.size + space
        #finaliza?
        if end_id == None:
            end = 0
        else:
            end = self.find_label_by_id(end_id).y

        objs = []
        for key in link:
            print key
            e = self.find_label_by_id(key[0])
            objs.append(e)

        #tocar con alambre esto, funciona pero no meter mano
        y  = start
        k = 0 #random.randint(1,5000)
        self.pages = [[]]
        c = 0
        for row in data:
            #probaremos solo la primera fila
            for i in range(len(objs)):
                lbl = copy.copy(objs[i])
                lbl.y = y
                lbl.id = lbl.id +'_field_'+ str(k)
                lbl.index = False
                lbl.text = row[i]
                k += 1
                self.pages[c].append(lbl)
            y = y - delta
            if y <= end:
                self.pages.append([])
                y = start
                c += 1




    def draw(self, canvas):
        for page in self.pages:
            for rect in self.rects:
                rect.draw(canvas)
            for label in self.labels:
                label.draw(canvas)
            for label in page:
                label.draw(canvas)
            canvas.showPage()

