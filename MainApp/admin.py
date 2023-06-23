from django.contrib import admin
from MainApp.models import links,anime,action,romance,horror,downloadpage

# Register your models here.
class linksadmin(admin.ModelAdmin):
    list_display=['downloadlink','downloadversion','telegramlink','facebooklink','instagramlink','twitterlink']

admin.site.register(links,linksadmin)

class downloadpageadmin(admin.ModelAdmin):
    list_display=['date','changelog','changeslist']

admin.site.register(downloadpage,downloadpageadmin)

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