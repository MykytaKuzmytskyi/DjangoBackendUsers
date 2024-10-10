from django.db import migrations
from django.contrib.auth import get_user_model


def create_users(apps, schema_editor):
    if not get_user_model().objects.filter(username='admin').exists():
        get_user_model().objects.create_superuser(
            username='admin',
            email='admin@admin.com',
            password='AzNvbA8583'
        )

    regular_users = [
        {'username': 'john_doe', 'email': 'john.doe@example.com', 'password': 'john_password'},
        {'username': 'jane_smith', 'email': 'jane.smith@example.com', 'password': 'jane_password'},
    ]

    for user_data in regular_users:
        if not get_user_model().objects.filter(username=user_data['username']).exists():
            get_user_model().objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password']
            )


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_users),
    ]
