# Generated by Django 2.1.2 on 2018-11-12 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order_dinner', '0008_auto_20181111_0217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puantity', models.IntegerField(default=0)),
                ('state', models.BooleanField(default=False)),
                ('Food', models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='Order_dinner.Food')),
            ],
        ),
    ]
