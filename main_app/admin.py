from django.contrib import admin


# Register your models here we want to use in our admin portal
from .models import Finch

admin.site.register(Finch)
