from django.contrib import admin
from user_auth.models import User

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    list_filter = ('username', 'password')
    
admin.site.register(User, userAdmin)