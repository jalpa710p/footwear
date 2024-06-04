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


@admin.register(ViewAllProduct)
class ImageSeller(admin.ModelAdmin):
    list_display = ['image', 'title', 'price']


@admin.register(Product)
class CategoryImage(admin.ModelAdmin):
    list_display = ['category', 'image']


@admin.register(MenImage)
class MenImage(admin.ModelAdmin):
    list_display = ['name', 'image']


@admin.register(WomenImage)
class WomenImage(admin.ModelAdmin):
    list_display = ['name', 'image']


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ['video_url', 'background_image', 'title', 'content']


@admin.register(ContactInfo)
class ContactInformation(admin.ModelAdmin):
    list_display = ['address', 'phone', 'email', 'website']


@admin.register(GetInTouch)
class GetInTouchContact(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'email', 'subject', 'message']


@admin.register(ProductDetail)
class ProductDetailMen(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'rating']


@admin.register(ProductImage)
class ProductImageMen(admin.ModelAdmin):
    list_display = ['image']

@admin.register(Seller)
class CartSeller(admin.ModelAdmin):
    list_display = ['image', 'title', 'price']

@admin.register(AddImage)
class AddWishlist(admin.ModelAdmin):
    list_display = ['image', 'title', 'price']
