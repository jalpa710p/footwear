"""
URL configuration for footwear project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from footwearapp.views import *


router = DefaultRouter()
router.register(r'registers', RegisterViewSet)
router.register(r'menus', MenuModalViewSet)
router.register(r'submenus', SubMenuViewSet)
router.register(r'badges', BadgeMenuViewSet)
router.register(r'slides', SlideViewSet)
router.register(r'featured_images', FeaturedImageViewSet)
router.register(r'best_sellers', BestSellerViewSet)
router.register(r'partners', PartnerViewSet)
router.register(r'men_images', MenImageViewSet)
router.register(r'women_images', WomenImageViewSet)
router.register(r'products', ProductViewSet)
router.register(r'about_pages', AboutPageViewSet)
router.register(r'contact_infos', ContactInfoViewSet)
router.register(r'product_images', ProductImageViewSet)
router.register(r'product_reviews', ProductReviewViewSet)
router.register(r'carts', CartViewSet)
router.register(r'sellers', SellerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('footwearapp.urls'), name='footwearapp'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
