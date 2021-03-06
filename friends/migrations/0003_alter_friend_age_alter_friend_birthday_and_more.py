# Generated by Django 4.0.3 on 2022-04-21 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_alter_friend_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='age',
            field=models.IntegerField(default=0, verbose_name='年齢'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='birthday',
            field=models.DateField(verbose_name='誕生日'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='mail',
            field=models.EmailField(max_length=255, verbose_name='メール'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='male',
            field=models.BooleanField(verbose_name='性別'),
        ),
    ]
