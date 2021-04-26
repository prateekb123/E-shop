from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    if str(product.id) in cart:
        return True
    return False

@register.filter(name='quantity_in_cart')
def quantity_in_cart(product, cart):
    if str(product.id) in cart:
        return cart[str(product.id)]
    else:
        return 0

@register.filter(name='price_total')
def price_total(product, cart):
    if str(product.id) in cart:
        return product.price*cart[str(product.id)]
    else:
        return 0

@register.filter(name='total')
def total(products, cart):
    ans = 0
    for p in products:
        ans+=price_total(p, cart)

    return ans


@register.filter(name='multiply')
def multiply(n1, n2):
    return n1*n2


