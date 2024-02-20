from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER_CHOICE = (
    ("M", "Male"),
    ("F", "Women"),
)

class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    dob = models.DateField()
    accumulate = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
STATUS_PRODUCT_CHOICE = (
    ("Best Seller", "Best Seller"),
    ("New", "New"),
    ("Normal", "Normal"),
    ("Best Sale", "Best Sale"),   
    ("Sold Out", "Sold Out"), 
)

class Size(models.Model):
    size = models.CharField(max_length=20)
    
    def __str__(self):
        return self.size
    
    
class Color(models.Model):
    color = models.CharField(max_length=20)
    
    def __str__(self):
        return self.color
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='products/', default=None)
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Color)
    rate = models.FloatField(default=0)
    price = models.IntegerField()
    price_original = models.IntegerField()
    descrip = models.CharField(max_length=500, blank=True) 
    status = models.CharField(max_length=15, choices=STATUS_PRODUCT_CHOICE, default="Normal")
    quantity_remain = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', default=None)
    
    def __str__(self):
        return self.product.name
     
       
    

STATUS_ORDER_CHOICE = (
    ("Completed", "Completed"),
    ("Pending", "Pending"),
    ("Confirmed", "Confirmed"),
    ("Cancelled", "Cancelled"),
)

STATUS_CART_CHOICE = (
    ("Bought", "Bought"),
    ("Ordered", "Ordered"),
    ("Ordering", "Ordering"),
    ("Incart", "Incart"),
)


class CardItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, default=None)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=15, choices=STATUS_CART_CHOICE, default="Incart")
    
    
PAYMENT_CHOICE = (
    ("Direct", "Direct"),
    ("BankTranfer", "BankTranfer"),
)
    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default=user.name)
    email = models.EmailField(blank=True, default=None)
    phone = models.CharField(max_length=15, default=None)
    note = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=30, default=None)
    district = models.CharField(max_length=30, default=None)
    ward = models.CharField(max_length=30, default=None)
    street = models.CharField(max_length=100, blank=True)
    order_total = models.IntegerField(default=0)
    payment = models.CharField(max_length=30, choices=PAYMENT_CHOICE, default="Direct")
    status = models.CharField(max_length=15, choices=STATUS_ORDER_CHOICE, default="Pending")
    created = models.DateField(auto_now_add=True)
    
    
class OderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, default=None)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=1)
    
    
    
    
    
    
    
