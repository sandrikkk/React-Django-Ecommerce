from django.urls import path
from product import views

urlpatterns = [
    path('latest-products/', views.LatestProductList.as_view()),
    path('', views.StoreProduts.as_view()),
    path('<slug:category_slug>/', views.StoreProduts.as_view()),
    path('<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
]