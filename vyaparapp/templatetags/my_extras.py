from dbm.ndbm import library
from django import template

register = template.Library()

@register.filter(name='mul')
def mul(a,b):
    return a*b

@register.filter(name='mod')
def mod(a,b):
    return a%b