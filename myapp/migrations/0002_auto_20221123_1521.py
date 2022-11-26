# Generated by Django 3.0 on 2022-11-23 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mymessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('title', models.TextField(max_length=200)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='contact',
        ),
    ]
