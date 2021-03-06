# Generated by Django 2.0.7 on 2018-07-20 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoe_app', '0002_shoe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoe', models.ForeignKey(on_delete='cascade', related_name='purchases', to='shoe_app.Shoe')),
                ('user', models.ForeignKey(on_delete='cascade', related_name='purchases', to='shoe_app.User')),
            ],
        ),
    ]
