# Generated by Django 4.1.3 on 2023-02-07 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Bacche',
            fields=[
                ('exam_center_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.exam_center')),
                ('name', models.CharField(max_length=20)),
                ('roll', models.IntegerField()),
            ],
            bases=('app.exam_center',),
        ),
    ]