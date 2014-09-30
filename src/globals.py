# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4

#Valores Por Defecto

PT = 0.8 #equivalente en puntos(PT) a un pixel (PX)
PX = 1.25 #equivalente en pixeles (PX) a un punto (PT)
R = 0
G = 1
B = 2 

PAGE_SIZE = A4
WIDTH, HEIGHT = A4
COLOR = '#000000' #Negro
STROKECOLOR = '#000000' #Negro
BACKGROUNDCOLOR = '#000000' #Negro
FONTSIZE = 12
LINEWEIGHT = 1.25 #esta expresada en pixels

#Listado de Fuentes y Alias
FONTS_FAMILY = {
    'Helvetica': 'Helvetica',
    'Times': 'Times',
    'Courier': 'Courier',
    'Symbol': 'Symbol',

    'Sans': 'Helvetica',
    'Serif': 'Times',
    'Monospaced': 'Courier',

    'Times New Roman': 'Times',
    'Default': 'Helvetica', #fuente por defecto
}

#Fuentes precargadas por ReportLab
FONTS = {
    'Helvetica': {
        'normal': 'Helvetica',
        'bold': 'Helvetica-Bold',
        'italic': 'Helvetica-Oblique',
        'bold-italic': 'Helvetica-BoldItalic'
    },
    'Times': {
        'normal': 'Times-Roman',
        'bold': 'Times-Bold',
        'italic': 'Times-Italic',
        'bold-italic': 'TImes-BoldItalic',
    },
    'Courier': {
        'normal': 'Courier',
        'bold': 'Courier-Bold',
        'italic': 'Courier-Italic',
        'bold-italic': 'Courier-BoldItalic',
    },
    'Symbol': {
        'normal': 'Symbol',
        'bold': 'Symbol',
        'italic': 'Symbol',
        'bold-italic': 'Symbol',
    }
}

#Fuentes definidas por el Usuario
USER_FONTS = {
    'Open Sans': {
        'normal': ['OpenSans', 'fonts/OpenSans-Regular.ttf'],
    }
}

#Fuente por Defecto deprecate 
#FONTFAMILY = FONTS['Helvetica']['bold'] #Fuente Por Defecto

