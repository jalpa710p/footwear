from rest_framework import serializers
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register  # Corrected this line
        fields = ['id', 'username', 'email', 'phone_no', 'password', 'confirm_password']


class MenuModalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuModal
        fields = ['id', 'title', 'url', 'icon', 'badge']

class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu
        fields = ['id', 'manu_item', 'name', 'url']

class BadgeMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = BadgeMenu
        fields = ['id', 'badge']

class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = ['id', 'image', 'head_1', 'head_2', 'head_3', 'category', 'button_text']

class FeaturedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedImage
        fields = ['id', 'image', 'text']

class BestSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestSeller
        fields = ['id', 'image', 'title', 'price']

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'image']

class MenImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenImage
        fields = ['id', 'image']

class WomenImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WomenImage
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'image']

class AboutPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPage
        fields = ['id', 'video_url', 'background_image', 'title', 'content']

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['id', 'address', 'phone', 'email', 'website']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productreview
        fields = ['id', 'image', 'name', 'date', 'description']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'image', 'name', 'price', 'quantity', 'total']

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'image', 'title', 'price']
