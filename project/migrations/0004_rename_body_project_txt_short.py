# Generated by Django 4.1.2 on 2022-10-28 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_rename_url_project_github_url_remove_project_hunter_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='body',
            new_name='txt_short',
        ),
    ]
