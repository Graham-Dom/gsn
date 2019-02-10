# Generated by Django 2.1.5 on 2019-02-09 23:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gsndb', '0007_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_type', models.CharField(choices=[('MTL', 'Mental Health'), ('DAC', 'Drug & Alcohol/Addictions Counseling'), ('DHS', 'Social Services (Department of Human Services)'), ('YSC', 'Division of Youth Services/Corrections'), ('CPS', 'Childcare/Preschool Services'), ('FMR', 'Family Resources'), ('M/C', 'Meals/Clothing'), ('HOU', 'Housing'), ('SIP', 'Specialized School Intervention Program'), ('TRN', 'Transportation'), ('WFC', 'Work Force Center'), ('IOG', 'Interagency Oversight Group (IOG)'), ('OTH', 'Other')], max_length=3)),
                ('referral_date', models.DateField(default=django.utils.timezone.now)),
                ('reference_name', models.CharField(max_length=100, null=True)),
                ('reference_phone', models.BigIntegerField(null=True)),
                ('reference_address', models.CharField(max_length=150, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsndb.Student')),
            ],
        ),
    ]