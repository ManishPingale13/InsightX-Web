# Generated by Django 4.2.3 on 2023-08-05 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0003_rename_name_machinerecord_machine_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="machinerecord",
            name="status",
            field=models.CharField(default="No Failure", max_length=30),
            preserve_default=False,
        ),
    ]
