from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to="profiles/", default='profiles/default.png')
    social = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Projects(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    seller = models.CharField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    featured_image = models.ImageField(upload_to='projects/%Y/%m/%d/', default="default.jpg")
    price = models.CharField(max_length=10)
    shop_o = models.CharField(max_length=200,
                              default='https://www.ozon.ru/seller/ip-valyan-a-n-675330/products/?miniapp=seller_675330',
                              editable=False)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-is_active']


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Firm(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$',
                                 message="Телефонный номер должен быть следующего формата: '+99999999'. До 15 символов.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, default='88000000000')
    email = models.EmailField(max_length=500, null=True, blank=True)
    description = models.TextField(max_length=250, null=True, blank=True)
    img_logo = models.ImageField(upload_to="firm/", default='firm/default.png')
    location = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
