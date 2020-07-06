# Generated by Django 3.0.7 on 2020-06-29 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('symbol', models.CharField(max_length=100, unique=True)),
                ('price', models.FloatField()),
                ('change_percent', models.FloatField(default=0.0)),
                ('favorite', models.BooleanField(default=False)),
                ('is_fund', models.BooleanField(default=False)),
                ('is_etf', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=50)),
                ('operation', models.CharField(choices=[('Compra', 'Compra'), ('Compra e Venda', 'Compra e Venda'), ('Venda', 'Venda')], max_length=25)),
                ('document', models.FileField(upload_to='', verbose_name='documents/pdfs')),
                ('date', models.DateField(verbose_name='Data da transação')),
                ('broker', models.CharField(choices=[('Agora - Caco', 'Agora - Caco'), ('BB - Ricardo', 'BB - Ricardo'), ('BB - Itala', 'BB - Itala'), ('BB - Thayssa', 'BB - Thayssa')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment', models.FloatField()),
                ('money_amount', models.FloatField()),
                ('stock_amount', models.IntegerField()),
                ('buy_price', models.FloatField()),
                ('owner', models.CharField(choices=[('Agora - Caco', 'Agora - Caco'), ('BB - Ricardo', 'BB - Ricardo'), ('BB - Itala', 'BB - Itala'), ('BB - Thayssa', 'BB - Thayssa')], default='Caco', max_length=20)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Stock')),
            ],
            options={
                'unique_together': {('owner', 'stock')},
            },
        ),
    ]