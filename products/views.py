from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import  Product
from cart.models import  Cart

class ProductListView(ListView):
	#queryset = Product.objects.all()
	template_name = 'products/list.html'

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all()


class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = 'products/detail.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		return context
	
	def get_queryset(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		return Product.objects.filter(pk=pk)


class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = 'products/detail.html'
	
	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context['cart'] = cart_obj
		return context
	
	def get_object(self, *args, **kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		#instance = Product.objects.get_by_id(Product, slug=slug, active=True)
		try:
			instance = Product.objects.get(slug=slug, active=True)
		except Product.DoesNotExist:
			raise Http404('Product does not exist')
		except Product.MultipleObjectsReturned:
			qs = Product.objects.filter(slug=slug, active=True)
			instance = qs.first()
		except:
			raise Http404('something is wrong')
		return instance
	
	
class ProductFeaturedListView(ListView):
	# queryset = Product.objects.all()
	template_name = 'products/list.html'
	
	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
	#queryset = Product.objects.filter('featured')
	template_name = 'products/detail.html'
	
	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all().featured()
	