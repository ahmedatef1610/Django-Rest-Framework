from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view(), name="product-list"),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name="product-detail"),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name="product-edit"),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view()),
    
    # path('', views.ProductMixinView.as_view()),
    # path('<int:pk>/', views.ProductMixinView.as_view()),
    # path('<int:pk>/update/', views.ProductMixinView.as_view()),
    # path('<int:pk>/delete/', views.ProductMixinView.as_view()),
    
    # path('', views.product_alt_view),
    # path('<int:pk>/', views.product_alt_view),
]
