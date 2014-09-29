# -*- coding: utf-8 -*-


import copy
import random
from xml.dom import minidom

import reportlab
from reportlab.pdfgen import canvas

import figures
from tools import canvas_reset
from globals import PT, A4


class Section:
    def __init__(self, _file, paginate=False):
        self.data = minidom.parse(_file)
        self.pagintate = paginate
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
                value = float(value[:-2])
                #print value
                #value = round(value)
                label.size = value * PT
                print label.text, value, PT, label.size

            if key == "font-style": #peso
                pass

            if key == "font-weight":
                pass

            if key == "fill":
                label.bg = value

            if key == "font-family":
                pass

        return label


    def parse(self):
        for rect in self.data.getElementsByTagName("rect"):
            self.parse_rect(rect)

        for label in self.data.getElementsByTagName("text"):
            self.parse_label(label)


    def parse_rect(self, xml):
        _id = xml.getAttribute("id")
        x = float(xml.getAttribute("x"))
        y = float(xml.getAttribute("y"))
        w = float(xml.getAttribute("width"))
        h = float(xml.getAttribute("height"))
        style = xml.getAttribute("style")
        obj = figures.Rect(_id, x, y, w, h)
        obj = self.rect_style_parse(obj, style)
        self.rects.append(obj)


    def parse_label(self, xml):
        _id = xml.getAttribute("id")
        x = float(xml.getAttribute("x"))
        y = float(xml.getAttribute("y"))
        span = xml.getElementsByTagName('tspan')[0]
        txt = span.childNodes[0].toxml()
        style = xml.getAttribute("style")
        obj = figures.Label(_id, x, y, txt)
        obj = self.label_style_parse(obj, style)
        self.labels.append(obj)

    
    def set_index(self, list):
        """
            Define las Etiqueta como indice, osea etiquetas que no se dibujaran
        """
        for key in list:
            self.find_label_by_id(key).index = True
    
    
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


    def paginate(self, data=[], index=[], link=[], end_id=None, space=0):
        """
            Paginar Resultado en el Documento

            data: array multidimencional con los datos a paginar
            index: ids de las etiquetas que se usaran como indices de los los
                datos a paginar
            links: diccionario guia de como enlazar los datos a paginar con los 
                indices
            end: id de etiqueta que actua como margen final de la pagina
        """
        #etiquetas que no se dibujaran su unica funcion es servir de indice 
        #para paginar resultados
        if end_id != None:
            self.set_index(index+[end_id])  
        else:
            self.set_index(index)
        
        #objs = []
        #for _id in index:
        #    objs.append(self.find_label_by_id())
        obj = self.find_label_by_id(index[0]) #tomo el primer elemento como indice
        start = obj.y #posicion inicial Y
        delta = obj.size + space #salto de cada fila vertical
        #hasta donde dibujar, el objecto con el id end_id sirve de referencia
        #sino se dibuja hasta el final de pagina
        if end_id != None:
            end = self.find_label_by_id(end_id).y
        else:
            end = 0

        objs = {} #objectos que serviran como referencia
        for key in index:
            objs[key] = self.find_label_by_id(key)
        
        pos = start #inicializo la posicion de paginacion 
        self.pages = [[]] #vacio todas las paginas y solo dejo una en blanco 
        c = 0 #indice de pagina
        eid = random.randint(1,5000) #elemnto id

        dic = {}
        for lnk in link:
            # label  -> id data
            dic[lnk[0]] = lnk[1]

        #comienzo paginado 
        for row in data:
            for key in dic:
                #obj_id = key #identificador de obj de referencia
                col = dic[key] #identificador de columna
                lbl = copy.copy(objs[key])
                lbl.y = pos
                lbl.text = row[col]
                lbl.id = "{0}_field_{1}".format(lbl.id, eid)
                lbl.index = False #el elemento se mostrara
                self.pages[c].append(lbl)
            pos -= delta
            #si llego al limite de la pagina agrego una nueva
            if pos <= end:
                self.pages.append([])
                pos = start
                c += 1


    def draw(self, canvas):
        #agrega una plantilla en blanco por que no se parsea etiquetas

        if not self.paginate:
            for rect in self.rects:
                rect.draw(canvas)
            for label in self.labels:
                label.draw(canvas)
            canvas.showPage()
        else:
            if len(self.pages) == 0:
                self.pages.append([])

            for page in self.pages:
                for rect in self.rects:
                    rect.draw(canvas)
                for label in self.labels:
                    label.draw(canvas)
                for label in page:
                    label.draw(canvas)
                canvas.showPage()



class Document:
    def __init__(self, _file, size=A4):
        #un documento se divide en varias session que pueden ser de una o 
        #varias paginas
        self.canvas = canvas.Canvas(_file, pagesize=size)
        self.sections = []
        # los diccionarios no tienen orden por lo que para mantener el orden
        # defini un diccionario exta
        self.section_indexs = {}
        
    
    def add_section(self, _file, _id, paginate=False):
        pos = len(self.sections)
        self.sections.append(Section(_file, paginate))
        self.section_indexs[_id] = pos


    def section_parse(self, _id):
        pos = self.sections_indexs[_id]
        self.sections[pos].parse()

    
    def parse(self):
        """
            Parsea Todas las sessiones
        """
        for section in self.sections:
            section.parse()

    
    def section_paginate(self, _id, data=[], index=[], link={}, end=None):
        pos = self.section_indexs[_id]
        self.sections[pos].paginate(data, index, link, end)


    def draw(self):
        """
            Dibuja todos los elementos en el documento, este metodo debe ser 
            el ultimo en ser llamado.
        """
        for section in self.sections:
            canvas_reset(self.canvas)
            section.draw(self.canvas)


    def save(self):
        """
        """
        self.canvas.save()

