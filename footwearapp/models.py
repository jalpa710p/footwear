from django.db import models


class Register(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    phone_no = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)


class MenuModal(models.Model):
    id = models.AutoField(primary_key=True)  
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    icon = models.CharField(max_length=100, blank=True, null=True)
    badge = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


class SubMenu(models.Model):
    menu_item = models.ForeignKey(MenuModal, related_name='sub_menu', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BadgeMenu(models.Model):
    id = models.AutoField(primary_key=True)
    badge = models.CharField(max_length=100)

#  index
class Slide(models.Model):
    image = models.ImageField(upload_to='slides/')
    head_1 = models.CharField(max_length=100)
    head_2 = models.CharField(max_length=100)
    head_3 = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    button_text = models.CharField(max_length=50)

    def __str__(self):
        return self.head_1


class FeaturedImage(models.Model):
    image = models.ImageField(upload_to='featured/')
    text = models.CharField(max_length=100)



class BestSeller(models.Model):
    image = models.ImageField(upload_to='best_sellers/')
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)



class Partner(models.Model):
    image = models.ImageField(upload_to='partners/')


# MenImage
class MenImage(models.Model):
    image = models.ImageField(upload_to='menimage/')


class Product(models.Model):
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    



class AboutPage(models.Model):
    video_url = models.URLField("Video URL", max_length=200)
    background_image = models.ImageField("Background Image", upload_to='about/')
    title = models.CharField("Title", max_length=200)
    content = models.TextField("Content")

# contact
class ContactInfo(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return f"Contact Information"


#   Productdetail
class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/')


class Productreview(models.Model):
    image = models.ImageField(upload_to='review/')
    name = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField()



#wishlist
#cart

class Cart(models.Model):
    image = models.ImageField(upload_to='carts/')
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    quantity = models.IntegerField()
    
    @property
    def total(self):
        return self.price * self.quantity
    

class Seller(models.Model):
    image = models.ImageField(upload_to='sellers/')
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

  
    

