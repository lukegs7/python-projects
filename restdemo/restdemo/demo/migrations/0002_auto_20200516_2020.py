# Generated by Django 2.2.10 on 2020-05-16 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruitentity',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fruits', to='demo.Category'),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='demo.UserEntity')),
            ],
            options={
                'verbose_name': '联系人',
                'verbose_name_plural': '联系人',
                'db_table': 'contact',
            },
        ),
    ]
