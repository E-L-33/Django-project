# Generated by Django 2.1.3 on 2018-11-13 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Order_dinner', '0001_initial'),
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_detail_number', models.IntegerField()),
                ('order_detail_money', models.IntegerField()),
                ('odate', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.IntegerField(choices=[(0, '未发送'), (1, '已发送'), (2, '确认收货')])),
                ('address_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Person.Address')),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Person.Customer')),
                ('food_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Order_dinner.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('order_money', models.IntegerField()),
                ('odate', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.IntegerField(choices=[(0, '未发送'), (1, '已发送'), (2, '确认收货')])),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Person.Customer')),
                ('food_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Order_dinner.Food')),
                ('history_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Order.History')),
                ('seller_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Order_dinner.Seller')),
            ],
        ),
        migrations.CreateModel(
            name='Order_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_detail_number', models.IntegerField()),
                ('order_detail_money', models.IntegerField()),
                ('order_num', models.IntegerField()),
                ('odate', models.DateTimeField(auto_now_add=True)),
                ('order_detail_remarks', models.CharField(max_length=40)),
                ('address_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Person.Address')),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Person.Customer')),
                ('food_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Order_dinner.Food')),
                ('history_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Order.History')),
                ('order_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Order.Order')),
                ('seller_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Order_dinner.Seller')),
            ],
        ),
        migrations.AddField(
            model_name='history',
            name='order_detail_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Order.Order_detail'),
        ),
        migrations.AddField(
            model_name='history',
            name='order_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Order.Order'),
        ),
        migrations.AddField(
            model_name='history',
            name='seller_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Order_dinner.Seller'),
        ),
    ]
