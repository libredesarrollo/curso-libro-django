from django import template

register = template.Library()

@register.filter(name='my_name')
def name(value):
    if value:
        return "Andrés Cruz Yoris"


@register.simple_tag(name='my_connection')
def connection_db(tabla, columna):
    return "Estoy leyendo la Base de Datos entre otras operaciones."