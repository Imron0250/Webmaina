from django.db import models

class Info(models.Model):
    logo = models.ImageField()
    adres = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    desc = models.TextField()

class Advantege(models.Model):
    name = models.CharField(max_length=255)


class About(models.Model):
    rigth = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    advantege = models.ManyToManyField(Advantege)
    img = models.ImageField()

class API(models.Model):
    text = models.CharField(max_length=255)
    web = models.CharField(max_length=255)
    android = models.CharField(max_length=255)
    ios = models.CharField(max_length=255)
    document = models.CharField(max_length=255)

class Webmain(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255)

class text(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

class Blog(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField()
    mini_text = models.CharField(max_length=255)
    text = models.TextField()

class Blog_Text(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    title2 = models.CharField(max_length=255)
    text2 = models.TextField()
class worker(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=255)
    mini_name = models.CharField(max_length=255)
    text = models.TextField()

class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

class Digital_Info(models.Model):
    adres = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    desc = models.TextField()

class About_us(models.Model):
    img = models.ImageField()
    text = models.TextField()
    title = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    text2 = models.CharField(max_length=255)

class Backround(models.Model):
    img = models.ImageField()

class Youtube(models.Model):
    youtube = models.CharField(max_length=255)

class Width(models.Model):
    titile = models.CharField(max_length=255)
    text = models.TextField()
    titile5 = models.CharField(max_length=255)

class Result(models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    title3 = models.CharField(max_length=255)
    title4 = models.CharField(max_length=255)

class Blog_site(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.TextField()
    mini_title = models.CharField(max_length=255)

