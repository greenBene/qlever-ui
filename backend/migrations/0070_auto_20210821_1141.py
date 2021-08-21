# Generated by Django 3.2.5 on 2021-08-21 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0069_alter_backend_defaultmodetimeout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backend',
            name='ntFileLastChange',
        ),
        migrations.AddField(
            model_name='backend',
            name='apiToken',
            field=models.CharField(default='', help_text='This token needs to be provided as ?token query parameter when executing Warmup tasks through API', max_length=32, verbose_name='API token'),
        ),
    ]
