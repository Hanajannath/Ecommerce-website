"""
URL configuration for EcommerceProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import auth_views, cart_views, order_views, product_views,profile_views

urlpatterns = [
    path('home',auth_views.home,name='home'),
    path('',auth_views.welcome,name='welcome'),
    path('register/', auth_views.register, name='register'),
    path('login/', auth_views.login, name='login'),

    path('cart/', cart_views.view_cart, name='view_cart'),
    path("add/<int:product_id>/", cart_views.add_to_cart, name="add_to_cart"),
    path("update/<int:item_id>/", cart_views.update_cart, name="update_cart"),
    path("remove/<int:item_id>/", cart_views.remove_from_cart, name="remove_from_cart"),
    # path('cart/remove/<int:product_id>/', cart_views.remove_from_cart, name='remove_from_cart'),
    # path('checkout/', cart_views.checkout, name='checkout'),


    path('orders/', order_views.my_orders, name='my_orders'),
    path('orders/manage/', order_views.manage_orders, name='manage_orders'),
    path('orders/update/<int:order_id>/', order_views.update_order_status, name='update_order_status'),
    path('orders/delete/<int:order_id>/', order_views.delete_order, name='delete_order'),
#    path('place_cartorder',cart_views.place_cart_order,name='placecartorder'),
   
    path('products/', product_views.product_list, name='product_list'),
    path('products/create/', product_views.create_product, name='create_product'),
    path('products/update/<int:product_id>/', product_views.update_product, name='update_product'),
    path('products/delete/<int:product_id>/', product_views.delete_product, name='delete_product'),
   
    path('cards/',product_views.userproducts,name='cards'),
    path('logout/',auth_views.logout_view,name='logout'),
    path('admin-dashboard/', auth_views.dashboard, name='admin_dashboard'),
    path('product/<int:product_id>/', product_views.product_detail, name='product_detail'),
    path('recently-viewed/', product_views.recently_viewed, name='recently_viewed'),
    path('order-now/<int:product_id>/', order_views.place_order_direct, name='order_now'),
    path('profile/', profile_views.view_profile, name='view_profile'),
    path('profile/edit/', profile_views.edit_profile, name='edit_profile'),

    path('placeorder/',order_views.place_order,name='place_order'),
    path('ordersuccess/',order_views.order_success,name='order_success'),
]
