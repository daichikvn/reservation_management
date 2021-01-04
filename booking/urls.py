from django.urls import path
from . import views


app_name = 'booking'

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<str:year>/<str:month>/<str:day>', views.details, name='details'),
    path('create/', views.BookingCreateView.as_view(), name='booking_create'),
    path('create_done/', views.create_done, name='create_done'),
    path('update/<int:pk>/', views.BookingUpdateView.as_view(), name='booking_update'),
    path('update_done/', views.update_done, name='update_done'),
    path('delete/<int:pk>/', views.BookingDeleteView.as_view(), name='booking_delete'),
    path('delete_done/', views.delete_done, name='delete_done'),
]