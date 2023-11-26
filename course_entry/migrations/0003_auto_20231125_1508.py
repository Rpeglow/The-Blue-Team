# Generated by Django 4.2.7 on 2023-11-25 20:08

from django.db import migrations

def insert_initial_data(apps, schema_editor):
    Image = apps.get_model('course_entry', 'Image')
    Image.objects.bulk_create([
        Image(
            id=1,
            image_url="https://upload.wikimedia.org/wikipedia/commons/1/16/5th_Floor_Lecture_Hall.jpg",
            description="Class Tracker",
            page="classtracker"
        ),
        Image(
            id=2,
            image_url="https://www.theladders.com/wp-content/uploads/resume-190724-800x450.jpg",
            description="Resume Builder",
            page="resumebuilder"
        ),
        Image(
            id=3,
            image_url="https://images.businessnewsdaily.com/app/uploads/2022/04/04081920/1554239632.jpeg",
            description="Job Search",
            page="jobsearch"
        ),
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('course_entry', '0002_image_page'),
    ]

    operations = [
        migrations.RunPython(insert_initial_data),
    ]