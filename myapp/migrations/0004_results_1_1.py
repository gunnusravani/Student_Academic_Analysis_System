# Generated by Django 4.1 on 2022-09-15 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_student_roll_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results_1_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subcode', models.CharField(max_length=200)),
                ('Subname', models.CharField(max_length=250)),
                ('Grade', models.CharField(max_length=200)),
                ('Credits', models.FloatField()),
                ('Grade_points', models.IntegerField(null=True)),
                ('exam_type', models.CharField(max_length=10, null=True)),
                ('Htno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
            options={
                'unique_together': {('Htno', 'Subcode')},
            },
        ),
    ]
