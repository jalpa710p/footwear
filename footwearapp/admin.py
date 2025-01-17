from django.contrib import admin
from .models import *


@admin.register(Register)
class RegisterUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_no', 'password', 'confirm_password']


@admin.register(MenuModal)
class MenuFormEntry(admin.ModelAdmin):
    list_display = ['id', 'title', 'url', 'icon', 'badge']


@admin.register(SubMenu)
class SubMenuEntry(admin.ModelAdmin):
    list_display = ['menu_item', 'name', 'url']


@admin.register(BadgeMenu)
class BadgeMenuEntry(admin.ModelAdmin):
    list_display = ['id', 'badge']


@admin.register(Slide)
class ImageSlide(admin.ModelAdmin):
    list_display = ['image', 'head_1', 'head_2', 'head_3', 'category', 'button_text']


@admin.register(FeaturedImage)
class ImageFeatured(admin.ModelAdmin):
    list_display = ['image', 'text']


@admin.register(BestSeller)
class ImageSeller(admin.ModelAdmin):
    list_display = ['image', 'title', 'price']


@admin.register(Partner)
class ImagePartner(admin.ModelAdmin):
    list_display = ['image']


@admin.register(Product)
class CategoryImage(admin.ModelAdmin):
    list_display = ['category', 'image']

@admin.register(MenImage)
class MenImagePage(admin.ModelAdmin):
    list_display = ['image']


@admin.register(WomenImage)
class WomenImagePage(admin.ModelAdmin):
    list_display = ['image']


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ['video_url', 'background_image', 'title', 'content']


@admin.register(ContactInfo)
class ContactInformation(admin.ModelAdmin):
    list_display = ['address', 'phone', 'email', 'website']


@admin.register(Productreview)
class ProductReviews(admin.ModelAdmin):
    list_display = ['image', 'name', 'date', ]


@admin.register(ProductImage)
class ProductImageMen(admin.ModelAdmin):
    list_display = ['image']

@admin.register(Seller)
class CartSeller(admin.ModelAdmin):
    list_display = ['image', 'title', 'price']

@admin.register(Cart)
class Cartproduct(admin.ModelAdmin):
    list_display = ['image','name', 'price', 'quantity', 'total']


