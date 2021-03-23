from django.db import models

class Review(models.Model):
    movie=models.ImageField(upload_to='images',blank=True,null=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=10000)
    releasedate=models.DateField()
    rating=models.FloatField(default=5)
    content= models.TextField()

    def __str__(self):
        return self.title

class Profile(models.Model):
    dpwebsite= models.TextField(max_length=20,blank=True,null=True)
    dpimage=models.ImageField(upload_to='images',blank=True,null=True)
    dpdescription=models.TextField(max_length=200)
    dpabout=models.TextField(max_length=20000,blank=True,null=True)
    dpyoutube=models.URLField(blank=True,null=True)
    dpinstagram=models.URLField(blank=True,null=True)
    dpyfacebook=models.URLField(blank=True,null=True)
    dptwitter=models.URLField(blank=True,null=True)
    dpgoogle=models.URLField(blank=True,null=True)
