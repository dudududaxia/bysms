# Generated by Django 3.1.7 on 2022-06-06 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_medicine_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderMedicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.medicine')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='medicines',
            field=models.ManyToManyField(through='common.OrderMedicine', to='common.Medicine'),
        ),
    ]
