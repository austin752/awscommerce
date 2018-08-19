from django.shortcuts import render, redirect

from orders.models import Order
from .models import Cart
from products.models import Product


# def cart_create(user=None):
# 	cart_obj = Cart.objects.create(user=None)
# 	return cart_obj

def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request) # returns cart_id.id
	return render(request, 'cart/home.html', {'cart':cart_obj})


def cart_update(request):
	product_id = request.GET.get('product_id')
	print(product_id)
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id) # product_id to be aded to cart
		except Product.DoesNotExist:
			print('product_id does not exist')
			return redirect('cart:home')
		cart_obj, new_obj = Cart.objects.new_or_get(request)  # returns cart_id
		if product_obj in cart_obj.products.all():
			cart_obj.products.remove(product_obj)
		else:
			cart_obj.products.add(product_obj) # adds product_id to cart
		request.session['cart_items'] = cart_obj.products.count()
		#return redirect(product_obj.get_absolute_url())
	return redirect('cart:home')


def checkout_home(request):
	cart_obj, cart_created = Cart.objects.new_or_get(request)  # returns cart_id.id
	#cart_items = Cart.objects.get(cart_obj)
	order_obj = None
	if cart_created or cart_obj.products.count() == 0:
		return redirect('cart:home')
	else:
		order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
	return render(request, 'cart/checkout.html', {'object':order_obj})