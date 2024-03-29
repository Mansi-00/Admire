# Generated by Django 3.2.3 on 2021-06-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='t1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Student Name')),
                ('s_eno', models.PositiveIntegerField(default='0', verbose_name='Student Enrollment')),
                ('s_email', models.EmailField(blank=True, default='', max_length=200, null=True, verbose_name='Student Email ID')),
                ('s_con', models.IntegerField(default='0', verbose_name='Student Contact Number')),
                ('s_add', models.TextField(default='', verbose_name='Student Address')),
            ],
        ),
    ]
