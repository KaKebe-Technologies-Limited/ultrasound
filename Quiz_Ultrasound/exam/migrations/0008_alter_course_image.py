# Generated by Django 4.2.2 on 2023-06-17 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/Student/'),
        ),
    ]
