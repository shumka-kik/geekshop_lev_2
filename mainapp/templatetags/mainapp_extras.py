from django import template

register = template.Library()


@register.simple_tag(name='multiply')
def multiply(qty, unit_price, *args, **kwargs):

    return int(qty) * int(unit_price)


register.filter('multiply', multiply)
