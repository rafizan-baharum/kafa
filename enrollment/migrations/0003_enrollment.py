# Generated by Django 2.2.4 on 2019-08-18 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrollment.Session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrollment.Student')),
            ],
            options={
                'ordering': [],
            },
        ),
    ]
