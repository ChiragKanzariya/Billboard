# Generated by Django 2.1.5 on 2019-04-04 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('clip', models.FileField(null=True, upload_to='static/upload/')),
                ('date_to', models.DateField(null=True)),
                ('date_from', models.DateField(null=True)),
                ('message', models.CharField(blank=True, help_text="It's always nice to add specific detail here!", max_length=300, verbose_name='Message')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('from_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations_sent', to=settings.AUTH_USER_MODEL)),
                ('to_owner', models.ForeignKey(help_text='select owner to send request!', on_delete=django.db.models.deletion.CASCADE, related_name='invitations_received', to=settings.AUTH_USER_MODEL, verbose_name='Owner to request')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('clip', models.FileField(null=True, upload_to='static/upload/')),
                ('date_to', models.DateField(null=True)),
                ('date_from', models.DateField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billboard_user', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billboard_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
