MyReport
========

Interfaz para generar reportes diseñados en SVG (con Inkscape por ejemplo) 
Mediante ReportLab 


Soporte de Figuras
==================
Por el momentos solo se soportan las siguientes figuras:

label 
rect
	

Rect
----
Figuras de Forma Rectangular, soporte casi completo

Label
-----
Las etiquetas de texto son soportadas parcialmente, el principal problema
es el uso de fuentes especificas ya que reportlab no carga automaticamente
las fuentes personalizadas solo soportan las siguiente:

Helvetica
Times
Courier

En caso de querer usuarse fuentes personalizadas definidas por el usuario
deben ser cargada en el archivo de configuracion globals.py en USER_FONTS
por el momento solo son soportadas fuente TrueType y se cargan de la
de la siguiente forma:

USER_FONTS = {
	'@familia': {
		'@style': ['@name','@path'],
	} 
}

Donde:
	@familia: es el nombre de la familia de la Fuente
	@style: Estilo de la fuente que representara puede ser uno de los 
	siguientes ('normal', 'bold', 'italic', 'bold-italic') 
	@name: nombre con el que se cargara la fuente, debe ser unico
	@path: ruta absoluta hacia la fuente
	
Un ejemplo completo:

USER_FONTS = {
    'Open Sans': {
        'normal': ['OpenSans', 'fonts/OpenSans-Regular.ttf'],
    }
}


Uso
===

La libreria usa la idea de un documento, compuestos por varias sessiones,
al menos una se debe definir, cada seccion se formatea en base a un 
archivo SVG con restriciones de que solo se dibujaran las figuras 
soportadas.

Antes de crear un documento se debe inicializar llamando al metodo 
parse.initialize() que cargara entre otras cosas las fuentes definidas 
por el usuario.

from MyReport.src import parser

parser.initialize()
doc = parser.Document('archivo.pdf')

Document
--------
El constructor del objecto Documento acepta los siguientes parametros

_file : ruta completa del archivo destino a generar
size: Tamaño de pagina, por el momento solo soporta el tamaño A4

Metodos
-------
	

No Existe soporte de z-index o posicion de capa, por lo que se debe tener 
en cuenta esta restriccion al diseñar sus plantillas.


