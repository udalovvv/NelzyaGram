from django.contrib import admin

from Profile.models import User, Publication


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   list_display = ['nickname', 'name', 'photo']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
   list_display = ['id', 'image_of_publication']