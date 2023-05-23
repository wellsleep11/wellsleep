from django.db import models
import datetime
from tinymce.models import HTMLField
from django.contrib.auth.forms import User

# Create your models here.

class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    message=models.TextField()
    class Meta:
        db_table="contact"

class category(models.Model):
    title=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='category/')
    class Meta:
        db_table="category"
    def __str__(self):
        return self.title    

MYTAG=(
    ('best','best'),
    ('featured','featured'),
     ('latest','latest'), 
) 
AVAILABILITY=(
     ('pillows','pillows'),
    ('mattress','mattress'),
     ('curtains','curtains'), 
    ('cushions','cushions'),
    ('bed','bed'),
     ('bedsheets','bedsheets'),

)       

class products(models.Model):
    name=models.CharField(max_length=100)
    mrp=models.FloatField()
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='product/')
    photo2=models.ImageField(upload_to='product/',default="")
    categoryid=models.ForeignKey(category,on_delete=models.CASCADE,default="")
    rating=models.CharField(max_length=10,default="1")
    brandname=models.CharField(max_length=100,default="")
    material=models.CharField(max_length=100,default="")
    availability=models.CharField(max_length=50,choices=AVAILABILITY,default="")
    tag=models.CharField(max_length=50,choices=MYTAG,default="")
    class Meta:
        db_table="products"
    def __str__(self):
        return self.name 
    
class blogs(models.Model):
    STATUSS=(
        ('New','New'),
        ('Approved','Approved')
    )
    title=models.CharField(max_length=100)
    description=HTMLField()
    photo=models.ImageField(upload_to='blogs/')
    post_by=models.CharField(max_length=50,default="Admin")
    post_on=models.DateField(default=datetime.date.today())
    status=models.CharField(max_length=20,default='Approved',choices=STATUSS)
    userid=models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True, default="1")
    class Meta:
        db_table="blogs"
    def __str__(self):
        return f"{self.title}----{self.status}"
    

class Faq(models.Model):
    Question=models.TextField()
    Answer=models.TextField()
    class Meta:
        db_table="Faq"
    def __str__(self):
        return self.Question    
    

class likenow(models.Model):
    productsid=models.ForeignKey(products,on_delete=models.CASCADE,default="")
    userid=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    class Meta:
        db_table='likenow'

class subscribe(models.Model):
    email=models.CharField(max_length=50)
    class Meta:
        db_table="subscribe"
          
    
     