# -*- coding: utf-8 -*-

import reportlab
from reportlab.pdfgen import canvas
from svgparser import Parser
from globals import A4



#Test found
if __name__ == '__main__':
    
    #generamos informacion aleatoria para rellenar la tabla
    data = []
    for i in range(20):
        data.append(("fieldA %s" %i, "fieldB %s" %i, "fieldC %s" %i, "fieldD %s" %i, "fieldE %s" %i))
    
    #enlaces para las guia de las etiquetas
    link =[
        #(lbl_index, #data_index),
        ('text3801', 0),
        ('text3805', 1),
        ('text3809', 2),
        ('text3813', 3),
        ('text3817', 4),
    ]

    canva = canvas.Canvas('samples/test-list.pdf', pagesize=A4)
    pdf = Parser('samples/test-list.svg')
    pdf.parse()

    #las etiquetas que actuaran como indice
    indexs= [
        'text3801',
        'text3805',
        'text3809',
        'text3813',
        'text3817',
        'text3831'  #actuara como indice de fin
    ]
    pdf.set_index(indexs)
    pdf.list_parse(data, link, 'text3831', 5)
    pdf.paginate(canva)
    canva.save()
