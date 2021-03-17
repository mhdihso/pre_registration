# Generated by Django 3.1.7 on 2021-03-17 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Create_preـregistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250)),
                ('price', models.PositiveIntegerField(default=None)),
                ('school', models.CharField(max_length=150)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='extra_qu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_qu', models.TextField(choices=[('1', 'Multiple options'), ('2', 'Descriptive '), ('3', 'File'), ('4', 'Data')], default='2', max_length=1)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last name')),
                ('mobile_phone', models.CharField(max_length=11, verbose_name='phone number')),
                ('national_id', models.CharField(max_length=10, verbose_name='national ID')),
                ('birth_date', models.DateField(blank=True, verbose_name='data of birth')),
                ('profile_pic', models.ImageField(upload_to='profile-pics', verbose_name='profile picture')),
                ('father_name', models.CharField(max_length=150, verbose_name='father name')),
                ('father_phone_number', models.CharField(max_length=11, verbose_name='father phone number')),
            ],
        ),
        migrations.CreateModel(
            name='preـregistration',
            fields=[
                ('main_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pre_registration.main')),
                ('extra_qus', models.ManyToManyField(blank=True, to='pre_registration.extra_qu')),
                ('pre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pre_id', to='pre_registration.create_preـregistration')),
            ],
            bases=('pre_registration.main',),
        ),
    ]