from django.views import generic
from product.models import Product, Variant, ProductVariantPrice, ProductVariant
from ..forms import ProductFilterForm
from django.db.models import Q
from django.db.models import OuterRef, Subquery
class ProductListView(generic.ListView):
	model = Product
	template_name = 'products/list.html'
	paginate_by = 2
	form_class = ProductFilterForm

	def get_queryset(self):
		queryset = super().get_queryset()
		queryset = queryset.prefetch_related('productvariantprice_set').all()

		# for product in queryset:
		# 	product_varient_price=product.productvariantprice_set.all()
		# 	product.product_varient_price = product_varient_price
		# breakpoint()
		form = self.form_class(self.request.GET)
		try:
			if form.is_valid():
				title = form.cleaned_data.get('title')
				date = form.cleaned_data.get('date')
				price_from = form.cleaned_data.get('price_from')
				price_to = form.cleaned_data.get('price_to')
				if title:
					queryset = queryset.filter(title__icontains=title)
				if date:
					queryset = queryset.filter(created_at__date=date)
				if price_from:
					# breakpoint()
					# return queryset.filter(productvariantprice__price__lte=price_from)
					# queryset = [i.productvariantprice_set.filter(price__gte=price_from) for i in queryset]
					# queryset=queryset.prefetch_related('productvariantprice_set').filter(productvariantprice__price__gte=price_from)
					# i._prefetched_objects_cache['productvariantprice_set'].filter(price__gte=price_from)
					# queryset.filter(productvariantprice_set__price__gte=price_from)
					# queryset = [variant for product in queryset for variant in product.productvariantprice_set.filter(price__gte=price_from)]
					# queryset.annotate(
					# 	prices=models.Prefetch('productvariantprice_set', queryset=Q(price__gte=price_from))
					# )
					# new_queryset = [obj for obj in queryset if
					#                 obj.productvariantprice_set.filter(price__gte=price_from)]
					# queryset = queryset.filter(pk__in=[obj.pk for obj in new_queryset])
					# breakpoint()
					# queryset = queryset.filter(productvariantprice__price__gte=price_from)
					# queryset = queryset(self.productvariantprice_set.filter(price__gte=price_from))
					# queryset = queryset.productvariantprice_set.all().filter(price__gte=price_from)
					# for i in queryset:
					# 	# breakpoint()
					# 	i.productvariantprice_set.filter(price__gte=price_from)
						# breakpoint()
					# queryset = queryset.productvariantprice_set.filter(price__gte=price_from)
				# if price_to:
				# 	for i in queryset:
				# 		i.productvariantprice_set.filter(price__lte=price_to)
					# queryset = queryset.filter(productvariantprice__price__lte=price_to)
		except Exception as e:
			pass

		# breakpoint()

		# form = self.form_class(self.request.GET)
		# breakpoint()
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# breakpoint()
		# # filter start
		# form = self.form_class(self.request.GET)
		# if form.is_valid():
		# 	title = form.cleaned_data.get('title')
		# 	if title:
		# 		queryset = self.object_list.filter(title__icontains=title)
		# 		breakpoint()

		# filter end
		# work for pagination start
		paginator = context['paginator']
		page_obj = context['page_obj']
		start_index = page_obj.start_index()
		end_index = page_obj.end_index()
		total_items = paginator.count
		context['range'] = f"Showing {start_index} to {end_index} out of {total_items}"
		# work for pagination end
		return context

# class ProductListView(generic.ListView):
# 	# model = Product
# 	template_name = 'products/list.html'
# 	# paginate_by = 10  # Adjust the number of products per page
#
# 	# context_object_name = "book_list"
# 	def get_queryset(self):
# 		self.product = Product.objects.all()
# 		# self.productWithVariantPrice = ProductVariantPrice.objects.filter(product=[i for i in self.product])
# 		# import pdb;pdb.set_trace()
# 		self.productVariantPrice = ProductVariantPrice.objects.all()
#
# 		# varient_group start
# 		# self.product_variantlist = ProductVariant.objects.all().values_list('variant_title')
# 		self.variant = Variant.objects.all()
# 		self.product_variantlist = ProductVariant.objects.all()
# 		self.varient_group = {}
# 		for i in self.variant:
# 			self.varient_title_name = []
# 			for j in self.product_variantlist:
# 				if i == j.variant:
# 					self.varient_title_name.append(j.variant_title)
# 				# print(i.title)
# 				# print(j.variant_title)
# 				self.varient_title_name = list(set(self.varient_title_name))
# 				# i.__dict__.update({i.title:self.varient_title_name})
# 				self.varient_group.update({i.title: self.varient_title_name})
# 		# import pdb;
# 		# pdb.set_trace()
#
# 		# varient_group end
# 		# product_list = {}
#
# 		for i in self.product:
# 			self.product_varient = []
# 			for j in self.productVariantPrice:
# 				if i == j.product:
# 					self.product_varient.append(j)
# 				# import pdb;pdb.set_trace()
# 				# i.updates.key()
# 				# print(i.add_to_class(self.product_list))
# 			# i=i.__dict__
# 			i.__dict__.update({'products': self.product_varient})
# 		# print(self.product_varient)
# 		# pass
# 		# product_list.update(i)
#
# 	# import pdb;pdb.set_trace()
#
# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
#
# 		if self.request.GET.get('title'):
# 			title = self.request.GET.get('title')
# 			self.product = self.product.filter(title__icontains=title)
# 			# import pdb;pdb.set_trace()
# 			for i in self.product:
# 				self.product_varient = []
# 				for j in self.productVariantPrice:
# 					if i == j.product:
# 						self.product_varient.append(j)
# 					# import pdb;pdb.set_trace()
# 					# i.updates.key()
# 					# print(i.add_to_class(self.product_list))
# 				# i=i.__dict__
# 				i.__dict__.update({'products': self.product_varient})
#
# 		if self.request.GET.get('variant'):
# 			variant = self.request.GET.get('variant')
# 			self.productVariantPrice = self.productVariantPrice.filter(
# 				Q(product_variant_one__variant_title=variant) | Q(product_variant_two__variant_title=variant) | Q(
# 					product_variant_three__variant_title=variant))
# 			for i in self.product:
# 				self.product_varient = []
# 				for j in self.productVariantPrice:
# 					if i == j.product:
# 						self.product_varient.append(j)
# 					# self.product = self.product.filter(id=i.id)
# 					# print(self.product)
# 				i.__dict__.update({'products': self.product_varient})
# 				if not i.products:
# 					self.product = self.product.exclude(id=i.id)
#
# 			for i in self.product:
# 				self.product_varient = []
# 				for j in self.productVariantPrice:
# 					if i == j.product:
# 						self.product_varient.append(j)
# 				i.__dict__.update({'products': self.product_varient})
#
# 		if self.request.GET.get('price_from') and self.request.GET.get('price_to'):
# 			price_from = self.request.GET.get('price_from')
# 			price_to = self.request.GET.get('price_to')
# 			self.productVariantPrice = self.productVariantPrice.filter(price__range=(price_from, price_to))
# 			for i in self.product:
# 				self.product_varient = []
# 				for j in self.productVariantPrice:
# 					if i == j.product:
# 						self.product_varient.append(j)
# 					# self.product = self.product.filter(id=i.id)
# 					# print(self.product)
# 				i.__dict__.update({'products': self.product_varient})
# 				if not i.products:
# 					self.product = self.product.exclude(id=i.id)
#
# 			for i in self.product:
# 				self.product_varient = []
# 				for j in self.productVariantPrice:
# 					if i == j.product:
# 						self.product_varient.append(j)
# 				i.__dict__.update({'products': self.product_varient})
#
# 		if self.request.GET.get('date'):
# 			date = self.request.GET.get('date')
# 			self.product = self.product.filter(created_at__date=date)
#
# 			for i in self.product:
# 				self.product_varient = []
# 				for j in self.productVariantPrice:
# 					if i == j.product:
# 						self.product_varient.append(j)
# 					# import pdb;pdb.set_trace()
# 					# i.updates.key()
# 					# print(i.add_to_class(self.product_list))
# 				# i=i.__dict__
# 				i.__dict__.update({'products': self.product_varient})
#
# 		# import pdb;pdb.set_trace()
#
# 		# context['product_variantlist'] = list(set(self.product_variantlist))
# 		context['product_variantlist'] = self.varient_group
# 		# import pdb;pdb.set_trace()
# 		context['product_list'] = self.product
# 		return context