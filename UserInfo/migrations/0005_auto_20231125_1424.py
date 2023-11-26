# Generated by Django 4.2.7 on 2023-11-24 22:25

from django.db import migrations, models

def insert_initial_data(apps, schema_editor):
    UserInformation = apps.get_model('UserInfo', 'UserInformation')
    UserInformation.objects.create(
        id=1,
        first_name="Robert",
        last_name="Paulson",
        middle_initial=None,
        address="123 E. Main street",
        city="Anytown",
        state="Anystate",
        zip_code="74158",
        phone="812-867-5309",
        email="a@a.com",
        tagline="A person who does things."
    )

class Migration(migrations.Migration):

    dependencies = [
        ('UserInfo', '0004_alter_userinformation_id'),
    ]

    operations = [
        migrations.RunPython(insert_initial_data),
    ]