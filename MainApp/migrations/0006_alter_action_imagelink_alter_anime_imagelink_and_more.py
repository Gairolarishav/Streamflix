# Generated by Django 4.2.1 on 2023-06-21 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_alter_action_imagelink_alter_anime_imagelink_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='imagelink',
            field=models.TextField(default='https://streamapi.blob.core.windows.net/appupdates/streamflix%20v1.19.apk?sp=r&st=2023-06-07T16:25:00Z&se=2050-06-08T00:25:00Z&spr=https&sv=2022-11-02&sr=b&sig=QvtPQfeNwrG%2BInvdaJF8hKp7s16CfYkLgkDhyPwr9p0%3D', null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='imagelink',
            field=models.TextField(default='https://streamapi.blob.core.windows.net/appupdates/streamflix%20v1.19.apk?sp=r&st=2023-06-07T16:25:00Z&se=2050-06-08T00:25:00Z&spr=https&sv=2022-11-02&sr=b&sig=QvtPQfeNwrG%2BInvdaJF8hKp7s16CfYkLgkDhyPwr9p0%3D', null=True),
        ),
        migrations.AlterField(
            model_name='horrer',
            name='imagelink',
            field=models.TextField(default='https://streamapi.blob.core.windows.net/appupdates/streamflix%20v1.19.apk?sp=r&st=2023-06-07T16:25:00Z&se=2050-06-08T00:25:00Z&spr=https&sv=2022-11-02&sr=b&sig=QvtPQfeNwrG%2BInvdaJF8hKp7s16CfYkLgkDhyPwr9p0%3D', null=True),
        ),
        migrations.AlterField(
            model_name='romance',
            name='imagelink',
            field=models.TextField(default='https://streamapi.blob.core.windows.net/appupdates/streamflix%20v1.19.apk?sp=r&st=2023-06-07T16:25:00Z&se=2050-06-08T00:25:00Z&spr=https&sv=2022-11-02&sr=b&sig=QvtPQfeNwrG%2BInvdaJF8hKp7s16CfYkLgkDhyPwr9p0%3D', null=True),
        ),
    ]
