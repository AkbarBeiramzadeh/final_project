# Generated by Django 4.2 on 2024-12-01 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_profile_user"),
        ("blog", "0002_alter_post_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="accounts.profile"
            ),
        ),
    ]
