from django.shortcuts import render 
from django.views.generic import ListView, DetailView,TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Turf, Order
from django.urls import reverse_lazy
from django.db.models import Q # for search method
from django.http import JsonResponse
import json



class TurfListView(ListView):
    model = Turf
    template_name = 'list.html'


class TurfDetailView(DetailView):
    model = Turf
    template_name = 'detail.html'


class SearchResultsListView(ListView):
	model = Turf
	template_name = 'search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		return Turf.objects.filter(
		Q(title__icontains=query) | Q(location__icontains=query)
		)

class TurfCheckoutView(LoginRequiredMixin, DetailView):
    model = Turf
    template_name = 'checkout.html'
    login_url     = 'login'
    

class ManagerView(LoginRequiredMixin,ListView):
      model=Turf
      model1=Order
      template_name='manager_detail.html'

			
      



def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Turf.objects.get(id=body['productId'])
	Order.objects.create(
		product=product
	)
	return JsonResponse('Payment completed!', safe=False)


