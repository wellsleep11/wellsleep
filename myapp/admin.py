from django.contrib import admin
from myapp.models import*
# Register your models here.

@admin.register(contact)
class contactadmin(admin.ModelAdmin):
    list_display=('name','email','phone','message',)

@admin.register(category)
class categoryadmin(admin.ModelAdmin):
    pass    

@admin.register(products)
class productadmin(admin.ModelAdmin):
    pass

@admin.register(blogs)
class blogsadmin(admin.ModelAdmin):
    pass

@admin.register(Faq)
class Faqadmin(admin.ModelAdmin):
    pass


