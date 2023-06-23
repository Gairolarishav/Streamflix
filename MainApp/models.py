from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class links(models.Model):
    downloadlink=models.TextField()
    downloadversion=models.TextField(null=True)
    telegramlink=models.TextField( null=True)
    facebooklink=models.TextField( null=True)
    instagramlink=models.TextField( null=True)
    twitterlink=models.TextField( null=True)

class downloadpage(models.Model):
    date=models.TextField()
    changelog=models.TextField( null=True,default='Changelog')
    changeslist=HTMLField( null=True)

class action(models.Model):
    image=models.TextField()
    imagelink=models.TextField(null=True, default="https://streamapi.blob.core.windows.net/appupdates/streamflix%20v1.19.apk?sp=r&st=2023-06-07T16:25:00Z&se=2050-06-08T00:25:00Z&spr=https&sv=2022-11-02&sr=b&sig=QvtPQfeNwrG%2BInvdaJF8hKp7s16CfYkLgkDhyPwr9p0%3D")

class anime(models.Model):
    image=models.TextField()
    imagelink=models.TextField(null=True, default="https://streamapi.blob.core.windows.net/appupdates/streamflix%20v1.19.apk?sp=r&st=2023-06-07T16:25:00Z&se=2050-06-08T00:25:00Z&spr=https&sv=2022-11-02&sr=b&sig=QvtPQfeNwrG%2BInvdaJF8hKp7s16CfYkLgkDhyPwr9p0%3D")

class horror(models.Model):
    image=models.TextField()
    imagelink=models.TextField(null=True, default="https://streamapi.blob.core.windows.net/appupdates/streamflix%20v1.19.apk?sp=r&st=2023-06-07T16:25:00Z&se=2050-06-08T00:25:00Z&spr=https&sv=2022-11-02&sr=b&sig=QvtPQfeNwrG%2BInvdaJF8hKp7s16CfYkLgkDhyPwr9p0%3D")

class romance(models.Model):
    image=models.TextField()
    imagelink=models.TextField( null=True,default="https://streamapi.blob.core.windows.net/appupdates/streamflix%20v1.19.apk?sp=r&st=2023-06-07T16:25:00Z&se=2050-06-08T00:25:00Z&spr=https&sv=2022-11-02&sr=b&sig=QvtPQfeNwrG%2BInvdaJF8hKp7s16CfYkLgkDhyPwr9p0%3D")