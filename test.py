# -*- coding: utf-8 -*-

import reportlab
from reportlab.pdfgen import canvas
from svgparser import Parser
from globals import A4



#Test found
if __name__ == '__main__':
    pdf = Parser('samples/text-model.svg')
    canva = canvas.Canvas('out.pdf', pagesize=A4)
    pdf.parse()
    pdf.draw(canva)
    canva.save()
