# -*- coding: utf-8 -*-

from xml.dom import minidom

import figures
from globals import PT

class Parser:
    def __init__(self, file):
        self.data = minidom.parse(file)
        self.rects = []
        self.labels = []



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
            print key,value
            if key == "font-size":
                label.size = float(value[:2]) * PT

            if key == "font-weight":
                pass

            if key == "fill":
                label.bg = value

        print

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


    def draw(self, canvas):
        for rect in self.rects:
            print rect
            rect.draw(canvas)
        for label in self.labels:
            print label
            label.draw(canvas)




