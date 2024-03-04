from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tao-san-pham/', views.createProduct, name='createProduct'),
    path('chi-tiet-san-pham/<str:pk>', views.detail, name='detail'),
    
    path('create-color/', views.create_color, name='create_color'),
    path('create-size/', views.create_size, name='create_size'),
    
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout-success/', views.checkoutSuccess, name='checkoutSuccess'),
    path('shop/<str:pk_cate>/<str:pk_subcate>/', views.shop_category, name='shop_category'),

]