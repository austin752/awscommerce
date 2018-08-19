from django.conf.urls import url

from .views import (
	cart_home,
	cart_update,
	checkout_home
)

urlpatterns = [
	
	url(r'^$', cart_home, name='home'),
	url(r'^update/$', cart_update, name='update'),
	url(r'^checkout/$', checkout_home,  name='checkout'),
	#url(r'^api/cart/', cart_detail_api_view, name='api-cart'),
	# url(r'^checkout/address/create/', checkout_address_create_view,  name='checkout_address_create_view'),
    # url(r'^checkout/address/reuse/', checkout_address_reuse_view,  name='checkout_address_reuse_view'),
]