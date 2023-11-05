from django.contrib import admin
from home.models import Secret,register,Transaction

# Register your models here.

admin.site.register(register)
admin.site.register(Secret)
admin.site.register(Transaction)