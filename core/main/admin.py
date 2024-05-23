from django.contrib import admin
from .models import Logo, HomeInfo,Intro,Explain, Project, Picture, Contact, ContactUs

# Register your models here.
admin.site.register(Logo)
admin.site.register(HomeInfo)
admin.site.register(Intro)
admin.site.register(Explain)
admin.site.register(Project)
admin.site.register(Picture)
admin.site.register(Contact)
admin.site.register(ContactUs)