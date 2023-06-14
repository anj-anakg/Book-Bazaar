from django.urls import path

from .views import ProductList, BookDetail, BookCheckOutView, PaymentComplete, SearchResultView, home, cart, about,add_to_cart,contact

urlpatterns = [
    path('home/', home, name='home'),
    path('list/', ProductList.as_view(), name='books'),
    path('details/<int:pk>/', BookDetail.as_view(), name='details'),
    path('checkout/<int:pk>/', BookCheckOutView.as_view(), name='checkout'),
    path('complete/', PaymentComplete, name='complete'),
    path('search/', SearchResultView.as_view(), name='search_results'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='mycart'),
    path('cart/add/<int:book_id>/',add_to_cart,name='add_to_cart'),
]
