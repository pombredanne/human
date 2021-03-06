from django import template
import locale

locale.setlocale(locale.LC_ALL, 'en_US.utf8')
register = template.Library()

@register.filter
def currencyformat (value):
    num = 0.0 
    try:
        num = float(value)
    except ValueError:
        pass
    
    return locale.currency(num, grouping=True)
