# Generated by Django 4.0.2 on 2022-10-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myimag', models.ImageField(upload_to='myimg/')),
            ],
            options={
                'verbose_name': 'Мое фото',
                'verbose_name_plural': 'Мои фото',
            },
        ),
    ]
