from django.contrib import admin
from MainApp.models import links,anime,action,romance,horror

# Register your models here.
class linksadmin(admin.ModelAdmin):
    list_display=['downloadlink','telegramlink','facebooklink','instagramlink','twitterlink']

admin.site.register(links,linksadmin)

class actionadmin(admin.ModelAdmin):
    list_display=['imagelink','image']

admin.site.register(action,actionadmin)

class animeadmin(admin.ModelAdmin):
    list_display=['imagelink','image']

admin.site.register(anime,animeadmin)

class horroradmin(admin.ModelAdmin):
    list_display=['imagelink','image']

admin.site.register(horror,horroradmin)

class romanceadmin(admin.ModelAdmin):
    list_display=['imagelink','image']

admin.site.register(romance,romanceadmin)