# Generated by Django 3.2.10 on 2022-05-13 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20211015_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
    ]
