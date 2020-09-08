# Generated by Django 3.1 on 2020-08-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20200830_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=122)),
                ('confirm_password', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
