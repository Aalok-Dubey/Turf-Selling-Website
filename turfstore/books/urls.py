
from django.urls import path
from .views import TurfListView,TurfDetailView,TurfCheckoutView,paymentComplete, SearchResultsListView,ManagerView


urlpatterns = [
    path('', TurfListView.as_view(), name = 'list'),
    path('<int:pk>/', TurfDetailView.as_view(), name = 'detail'),
    path('<int:pk>/checkout/', TurfCheckoutView.as_view(), name = 'checkout'),
    path('complete/', paymentComplete, name = 'complete'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
    path('manager/',ManagerView.as_view(), name = 'manager'),
]