from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('business-detail/<slug:slug>/',views.business_detail,name='business_detail'),
    # Sub-subcategory route (deepest first to avoid conflict)
    path('<slug:location>/<slug:grandparent_slug>/<slug:parent_slug>/<slug:slug>/', views.category_detail, name='sub_subcategory_detail'),

    # Subcategory route
    path('<slug:location>/<slug:parent_slug>/<slug:slug>/', views.category_detail, name='subcategory_detail'),

    # Top-level category
    path('<slug:location>/<slug:slug>/', views.category_detail, name='category_detail'),

    path('business/<int:business_id>/reviews/', views.business_reviews, name='business_reviews'),
    path('business/<int:business_id>/reviews/load/', views.load_more_reviews, name='load_more_reviews'),
    path('business/<int:business_id>/reviews/add/', views.add_review, name='add_review'),
    path('search/', views.search_business, name='search_business'),
    path('submit-enquiry/', views.submit_enquiry, name='submit_enquiry'),
    
]
