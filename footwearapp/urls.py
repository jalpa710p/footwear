from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(views.index, name='index'),
    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('add/', views.add, name='add'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/', views.order, name='order'),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user-dashboard'),
    path('menu/', views.menu, name='menu'),
    path('edit_menu/<int:id>/', views.edit_menu, name='edit_menu'),
    path('delete_menu/<int:id>/', views.delete_menu, name='delete_menu'),
    path('header/', views.header, name='header'),
    path('sub_menu/', views.sub_menu, name='sub_menu'),
    path('badge/', views.badge, name='badge'),
    path('badge_table/', views.badge_table, name='badge_table'),
    path('edit_badge/<int:id>/', views.edit_badge, name='edit_badge'),
    path('delete_badge/<int:id>/', views.delete_badge, name='delete_badge'),
    path('menu_table/', views.menu_table, name='menu_table'),

]

