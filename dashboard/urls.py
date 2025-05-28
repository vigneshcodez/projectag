from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='dashboard_index'),
    path('business_list/', views.user_business_list, name='user_business_list'),
    path('user_business_enquires/', views.user_business_enquires, name='user_business_enquires'),
    path('business/create/', views.business_create, name='business_create'),
    path('business/edit/<int:id>/', views.business_edit, name='business_edit'),
    path('business/delete/<int:id>/', views.delete_business, name='business_delete'),
    path('enquiry/delete/<int:id>/', views.delete_enquiry, name='delete_enquiry'),
    path('iyer/create/', views.create_iyer_profile, name='create_iyer_profile'),
    path('iyer/update/', views.update_iyer_profile, name='update_iyer_profile'),
    path('iyer/orders/', views.orders, name='orders_page'),
    path('iyer/bookings/', views.bookings, name='bookings_page'),

]