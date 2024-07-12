from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import *
from .serializers import *
from rest_framework import viewsets
# from django.http import JsonResponse


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class MenuModalViewSet(viewsets.ModelViewSet):
    queryset = MenuModal.objects.all()
    serializer_class = MenuModalSerializer

class SubMenuViewSet(viewsets.ModelViewSet):
    queryset = SubMenu.objects.all()
    serializer_class = SubMenuSerializer

class BadgeMenuViewSet(viewsets.ModelViewSet):
    queryset = BadgeMenu.objects.all()
    serializer_class = BadgeMenuSerializer

class SlideViewSet(viewsets.ModelViewSet):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer

class FeaturedImageViewSet(viewsets.ModelViewSet):
    queryset = FeaturedImage.objects.all()
    serializer_class = FeaturedImageSerializer

class BestSellerViewSet(viewsets.ModelViewSet):
    queryset = BestSeller.objects.all()
    serializer_class = BestSellerSerializer

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class MenImageViewSet(viewsets.ModelViewSet):
    queryset = MenImage.objects.all()
    serializer_class = MenImageSerializer

class WomenImageViewSet(viewsets.ModelViewSet):
    queryset = WomenImage.objects.all()
    serializer_class = WomenImageSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class AboutPageViewSet(viewsets.ModelViewSet):
    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer

class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = Productreview.objects.all()
    serializer_class = ProductReviewSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


def admin_dashboard(request):
    show_menu_table = False
    show_badge_table = False
    data = None

    if request.method == "POST":
        if request.POST.get('show_menu_table'):
            show_menu_table = True
            data = MenuModal.objects.all()
        elif request.POST.get('show_badge_table'):
            show_badge_table = True
            data = BadgeMenu.objects.all()

    context = {
        'show_menu_table': show_menu_table,
        'show_badge_table': show_badge_table,
        'data': data
    }

    return render(request, 'admin_dashboard.html', context)


def menu_table(request):
    data = MenuModal.objects.all()
    return render(request, 'menu_table.html', {'data': data})


def menu(request):
    if request.method == "POST":
        title = request.POST.get('title')
        url = request.POST.get('url')

        print(title, url)

        if MenuModal.objects.filter(title=title).exists():
            return render(request, 'menu.html', {'error': "Title already exists."})

        if MenuModal.objects.filter(url=url).exists():
            return render(request, 'menu.html', {'error': "Url already exists."})

        data = MenuModal(title=title, url=url)
        data.save()

        return redirect('menu_table')

    return render(request, 'menu.html')


def men(request):
    partners = Partner.objects.all()
    products = Product.objects.all()
    men_image = MenImage.objects.last() 
    best_sellers = BestSeller.objects.all()
    partners = Partner.objects.all()

    return render(request, 'men.html', context={'men_image': men_image,
                                                'products': products,
                                                'best_sellers': best_sellers,
                                                'partners': partners
                                                })
        
    
                                            
                                            
def women(request):
    partners = Partner.objects.all()
    best_sellers = BestSeller.objects.all()
    products = Product.objects.all()
    women_image = WomenImage.objects.last() 
    return render(request, 'women.html', context={'partners': partners,
                                                 'best_sellers': best_sellers,
                                                 'products': products,
                                                  'women_image': women_image
                                                  })

def about(request):
    about_page = AboutPage.objects.first()
    context = {
        'about_page': about_page
    }
    return render(request, 'about.html', context)


def contact(request):
    contact_info = ContactInfo.objects.first()
    return render(request, 'contact.html', {'contact_info': contact_info})


def add(request):
    Sellers = Seller.objects.all()
    cart_items = Cart.objects.all()
    return render(request, 'add-to-wishlist.html', {'sellers': Sellers ,
                                                    'cart_items': cart_items})


def cart(request):
    sellers = Seller.objects.all()
    cart_items = Cart.objects.all()
    subtotal = sum(i.total for i in cart_items)
    
    delivery = 0.00
    discount = 45.00

    total = subtotal + delivery - discount

    return render(request, 'cart.html', {'sellers': sellers,
                                        'cart_items': cart_items,
                                        'subtotal': subtotal,
                                        'delivery': delivery,
                                        'discount': discount,
                                        'total': total})



    
def remove_cart(request,id):
    Cart.objects.get(id=id).delete()
    cart_items = Cart.objects.all()
    return render(request, 'cart.html', context={'cart_items': cart_items})


def checkout(request):
    cart_items = Cart.objects.all()
    subtotal = sum(i.total for i in cart_items)
    delivery = 0.00
    discount = 45.00

    total = subtotal + delivery - discount

    return render(request, 'checkout.html',context={'cart_items': cart_items,
                                                    'subtotal': subtotal,
                                                    'delivery': delivery,
                                                    'discount': discount,
                                                    'total': total})


def order(request):
    return render(request, 'order-complete.html')


def product_detail(request):
    images = ProductImage.objects.all()
    review =Productreview.objects.all()
    return render(request, 'product_detail.html', context={
                                                           'images': images,
                                                           'review': review})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = authenticate(username=username, password=password)
        if obj:
            return redirect('admin_dashboard')
        else:
            return render(request, 'login.html', {'error': f"Invalid username and password"})
    return render(request, 'login.html')


def index(request):
    slides = Slide.objects.all()
    featured = FeaturedImage.objects.all()
    best_sellers = BestSeller.objects.all()
    partners = Partner.objects.all()
    return render(request, 'index.html', {
                                                    'slides': slides,
                                                    'featured_images': featured,
                                                    'best_sellers': best_sellers,
                                                    'partners': partners
    })

def user_dashboard(request):
    return render(request, 'user_dashboard.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print(username, email, phone_no, password, confirm_password)

        if Register.objects.filter(username =username).exists():
            error = "Username already exists."
            return render(request, 'register.html', {'error': error})

        if Register.objects.filter(email=email).exists():
            error = "Email already exists."
            return render(request, 'register.html', {'error': error})

        if password == confirm_password:
            data = Register(username=username, email=email, phone_no=phone_no, password=password, confirm_password=confirm_password)
            data.save()
            return redirect('user-dashboard')
        else:
            error = "password not match."
            return render(request, 'register.html', {'error': error})
    return render(request, 'register.html')


def forgot_password(request):
    return render(request, 'forgot_password.html')


def edit_menu(request, id):
    data = MenuModal.objects.get(id=id)
    if request.method == 'POST':
        data.title = request.POST.get('title')
        data.url = request.POST.get('url')
        print(data.title, data.url)
        data.save()
        data = MenuModal.objects.all()
        return render(request, template_name='admin_dashboard.html', context={'data': data})
    return render(request, template_name='edit_menu.html', context={'data': data})


def delete_menu(request,id):
    MenuModal.objects.get(id=id).delete()
    data = MenuModal.objects.all()
    return render(request, 'admin_dashboard.html', {'data': data})


def header(request):
    menu_items = MenuModal.objects.all()
    badges = BadgeMenu.objects.all()
    context = {'menu_items': menu_items, 'badges': badges}
    return context


def sub_menu(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        url = request.POST.get('url')
        menu_form_id = request.POST.get('menu_form')

        if not (name and url and menu_form_id):
            return render(request, 'sub_menu.html',
                          {'error_message': 'Please provide all required information.'})

        try:
            menu_form = MenuModal.objects.get(pk=menu_form_id)
        except MenuModal.DoesNotExist:
            return render(request, 'sub_menu.html',
                          {'error_message': 'Invalid menu form selected.', 'menu_form': menu_form})

        submenu = SubMenu(name=name, url=url, menu_item=menu_form)
        submenu.save()
        return redirect('admin_dashboard')
    else:
       menu_forms = MenuModal.objects.all()
       return render(request, 'sub_menu.html', {'menu_forms': menu_forms})


def badge(request):
    if request.method == "POST":

        badge = request.POST.get('badge')
        print(badge)


        data = BadgeMenu(badge=badge)
        data.save()

        return redirect('badge_table')
    badges = BadgeMenu.objects.all()
    return render(request, 'badge.html', context={'badges': badges})


def badge_table(request):
    data = BadgeMenu.objects.all()
    return render(request, 'badge_table.html', {'data': data})


def edit_badge(request, id):
    data = BadgeMenu.objects.get(id=id)
    if request.method == 'POST':
        badge_name = request.POST.get('badge')
        data.badge = badge_name
        data.save()
        return redirect('badge_table')
    return render(request, 'edit_badge.html', {'data': data})


def delete_badge(request,id):
    BadgeMenu.objects.get(id=id).delete()
    data = BadgeMenu.objects.all()
    return render(request, 'admin_dashboard.html', {'data': data})


