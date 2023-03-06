from django.contrib import admin


# Register your models here we want to use in our admin portal
from .models import Finch, Feeding, Toy

admin.site.register(Finch)

# register our new feeding model
admin.site.register(Feeding)

admin.site.register(Toy)
