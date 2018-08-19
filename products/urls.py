from django.conf.urls import url

from products.views import (
	ProductListView,
	ProductDetailSlugView
)

urlpatterns = [
	
	url(r'^$', ProductListView.as_view(), name='list'),
	
	#slug view
	url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
	
]
