from django.db import models
from datetime import date
from solo.models import SingletonModel

class SiteConfig(SingletonModel):
    site_logo = models.ImageField(verbose_name='Site Logo', upload_to='site_conf')
    site_logo_text = models.CharField(max_length=255, default='text')
    site_name = models.CharField(max_length=255, default='Site name')
    site_descr = models.TextField(default='Site description')
    site_key_words = models.TextField(default='Site key words')
    phone = models.BigIntegerField(max_length=20, default='Company phone')
    phone2 = models.BigIntegerField(max_length=20, default='Company phone2')
    address = models.CharField(max_length=255, default='Company address')
    email = models.EmailField(max_length=50, default='Company email')
    insta = models.CharField(max_length=255, default='Company instagram')
    about_title = models.CharField(max_length=255, default='About title')
    about_text = models.TextField(default='About text')
    map_html1 = models.TextField(default='Map iframe1')
    map_html2 = models.TextField(default='Map iframe2')

class Blog(models.Model):
    STATUS_CHOICES = [
        ('public', 'Published')
    ]
    image = models.ImageField(verbose_name='image', upload_to='blog', default='blog/default.png')
    title = models.CharField('title', max_length=150, null=False)
    slug = models.SlugField('slug', max_length=150, unique=True)
    text = models.TextField('text')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date = models.DateField(default=date.today())

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Blog'

class Comments(models.Model):
    STATUS_CHOICES = [
        ('public', 'Published')
    ]
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField('author', max_length=150, null=False)
    text = models.TextField('text', null=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date = models.DateField(default=date.today())

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Partners(models.Model):
    title = models.CharField('title', max_length=150, null=False)
    logo = models.ImageField(verbose_name='Logo', upload_to='partners')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'

class Portfolio(models.Model):
    image = models.ImageField(verbose_name='image', upload_to='portfolio', null=False)
    title = models.CharField('title', max_length=150, null=False)
    descr = models.TextField('description', null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'

class Services(models.Model):
    title = models.CharField('title', max_length=150, null=False)
    img = models.ImageField(verbose_name='Image', upload_to='services')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
