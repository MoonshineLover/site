# Generated by Django 4.1.10 on 2023-08-20 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
