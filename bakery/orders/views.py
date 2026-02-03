from django.shortcuts import redirect, render, get_object_or_404
from products.models import Product
from django.contrib import messages

# Create your views here.

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)
    cart[product_id] = cart.get(product_id, 0) + 1
    messages.success(request, "Product added to cart.")

    request.session['cart'] = cart
    return redirect('cart_detail')

def decrease_cart_item(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] -= 1
        if cart[product_id] <= 0:
            del cart[product_id]

    request.session['cart'] = cart
    return redirect('cart_detail')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)
    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart
    return redirect('cart_detail')


def cart_detail(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        total += subtotal

        items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'orders/cart_detail.html', {
        'items': items,
        'total': total
    })
