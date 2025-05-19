from django.urls import path
from .views import RegisterView, LoginView, BusListCreateView, UserBookingView, BookingView

urlpatterns = [
    path('buses/', BusListCreateView.as_view(), name='buslist'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user-bookings/', UserBookingView.as_view(), name='user-bookings'),
    path('bookking/', BookingView.as_view(), name='booking')
]